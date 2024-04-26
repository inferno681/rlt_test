import pytest
from json import dumps

from constants import (
    TEST_INVALID_DATE_MESSAGES,
    TEST_INVALID_GROUP_TYPE_MESSAGES,
    TEST_INVALID_KEY_MESSAGES,
    TEST_INVALID_STRUCTURE_MESSAGES_1,
    TEST_INVALID_STRUCTURE_MESSAGES_2,
    TEST_VALID_MESSAGES_1,
    TEST_VALID_MESSAGES_2,
    TEST_VALID_MESSAGES_3,
)
from db import aggregate
from validation import input_check


@pytest.mark.asyncio
@pytest.mark.parametrize("input_message, output_message", (
    TEST_VALID_MESSAGES_1,
    TEST_VALID_MESSAGES_2,
    TEST_VALID_MESSAGES_3,
))
async def test_valid_requests(input_message, output_message):
    aggregation_result = await aggregate(input_message)
    result = dumps({
        "dataset": list(aggregation_result.values()),
        "labels": list(aggregation_result.keys())
    })
    assert result == dumps(output_message)


@pytest.mark.parametrize("input_message, output_message", (
    TEST_INVALID_DATE_MESSAGES,
    TEST_INVALID_GROUP_TYPE_MESSAGES,
    TEST_INVALID_KEY_MESSAGES,
    TEST_INVALID_STRUCTURE_MESSAGES_1,
    TEST_INVALID_STRUCTURE_MESSAGES_2))
def test_invalid_requests(input_message, output_message):
    check_message = input_check(dumps(input_message))
    assert not check_message[0]
    assert check_message[1] == output_message
