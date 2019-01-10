import json
import datetime
import boto3
import os

from whichbins.schedule import Schedule
from whichbins.notifications import send_sms

def get_schedule():
    schedule = Schedule()

    bucket = os.environ.get("WHICHBINS_CONFIG_BUCKET", "whichbins-config")
    key = os.environ.get("WHICHBINS_CONFIG_FILE", "bins.json")
    s3 = boto3.resource("s3")
    obj = s3.Object(bucket, key)
    binsData = obj.get()["Body"].read().decode("utf-8")
    bins = json.loads(config)

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
        send_sms(message)

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