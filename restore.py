import bson
import logging
import os

import pymongo

from config_reader import config
from constants import CONNECTION_STRING

logger = logging.getLogger(__name__)


def restore(path):
    """Функция загрузки тестовых данных"""

    db_client = pymongo.MongoClient(
        CONNECTION_STRING.format(
            username=config.MONGO_INITDB_ROOT_USERNAME,
            password=config.MONGO_INITDB_ROOT_PASSWORD.get_secret_value(),
            host=config.DB_HOST,
            port=config.DB_PORT,
        ),
        authSource="admin"
    )
    db = db_client[config.DB_NAME]
    for coll in os.listdir(path):
        if coll.endswith('.bson'):
            with open(os.path.join(path, coll), 'rb+') as f:
                db[coll.split('.')[0]].insert_many(
                    bson.decode_all(f.read()), ordered=False
                )
    logger.info('Данные импортированны')


def main():
    restore('./test_data/')


if __name__ == "__main__":
    main()
