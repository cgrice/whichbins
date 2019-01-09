import json
import datetime
from unittest.mock import patch

from whichbins.app import lambda_handler
from whichbins.schedule import Schedule

@patch('whichbins.app.get_schedule')
def test_handler_returns_none(get_schedule):
    mockSchedule = Schedule()
    get_schedule.return_value = mockSchedule
    expectedResponse = {
        "statusCode": 200,
        "body": json.dumps(
            None
        ),
    }
    assert lambda_handler(None, None) == expectedResponse

@patch('whichbins.app.get_schedule')
@patch('whichbins.app.send_sms')
def test_handler_returns_bins(send_sms, get_schedule):
    mockSchedule = Schedule()
    tomorrow = str(datetime.date.today() + datetime.timedelta(days=1))
    mockSchedule.add(tomorrow, { "black": True, "blue": False })
    get_schedule.return_value = mockSchedule
    expectedResponse = {
        "statusCode": 200,
        "body": json.dumps(
            {
                "black": True,
                "blue": False,
                "brown": False,
                "green": False
            }
        ),
    }
    assert lambda_handler(None, None) == expectedResponse

@patch('whichbins.app.get_schedule')
@patch('whichbins.app.send_sms')
def test_message_is_sent(send_sms, get_schedule):
    mockSchedule = Schedule()
    tomorrow = str(datetime.date.today() + datetime.timedelta(days=1))
    mockSchedule.add(tomorrow, { "black": True, "blue": False })
    get_schedule.return_value = mockSchedule
    lambda_handler(None, None)
    send_sms.assert_called_with("It's bin night! Put these out: Black.", "+0161555555")
    