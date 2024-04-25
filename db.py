from datetime import datetime

from motor.motor_asyncio import AsyncIOMotorClient
from pandas import date_range

from config_reader import config
from constants import CONNECTION_STRING, DATE_INTERVAL, GROUP_FORMAT


async def aggregate(data):
    """Функция получения и агрегирования данных"""
    dt_from = data["dt_from"]
    dt_upto = data["dt_upto"]
    group_type = data["group_type"]
    dt_from = datetime.fromisoformat(dt_from)
    dt_upto = datetime.fromisoformat(dt_upto)

    date_list = (
        date_range(dt_from, dt_upto, freq=DATE_INTERVAL[group_type])
        .strftime(GROUP_FORMAT[group_type])
        .tolist()
    )

    pipeline = [
        {"$match": {"dt": {"$gte": dt_from, "$lte": dt_upto}}},
        {
            "$group": {
                "_id": {
                    "$dateToString": {
                        "format": GROUP_FORMAT[group_type],
                        "date": "$dt"
                    }
                },
                "total_value": {"$sum": "$value"},
            }
        },
        {"$sort": {"_id": 1}},
        {
            "$group": {
                "_id": None,
                "results": {"$push": {"k": "$_id", "v": "$total_value"}},
            }
        },
        {"$replaceRoot": {"newRoot": {"$arrayToObject": "$results"}}},
    ]

    db_client = AsyncIOMotorClient(
        CONNECTION_STRING.format(
            username=config.MONGO_INITDB_ROOT_USERNAME,
            password=config.MONGO_INITDB_ROOT_PASSWORD.get_secret_value(),
            host=config.DB_HOST,
            port=config.DB_PORT,
        )
    )
    current_db = db_client[config.DB_NAME]
    collection = current_db[config.COLLECTION_NAME]

    result = await collection.aggregate(pipeline).to_list(length=None)
    result = {date: result[0].get(date, 0) for date in date_list}

    return result
