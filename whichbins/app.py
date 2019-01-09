import json
import datetime

from whichbins.schedule import Schedule
from whichbins.notifications import send_sms

def get_schedule():
    schedule = Schedule()

    with open('./bins.json') as binsData:
        bins = json.loads(binsData.read())

    for collection in bins:
        schedule.add(collection['date'], collection['bins'])
    
    return schedule

def lambda_handler(event, context):
    bins = []
    
    schedule = get_schedule()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)

    collections = schedule.onDate(tomorrow.strftime("%Y-%m-%d"))

    if collections:
        message = bins_message(collections)
        send_sms(message, "+440000000000")

    return {
        "statusCode": 200,
        "body": json.dumps(
            collections
        ),
    }

def bins_message(collections):
    bins = []
    for binColour in collections:
        if collections[binColour]:
            bins.append(binColour.capitalize())

    return "It's bin night! Put these out: %s." % ",".join(bins)