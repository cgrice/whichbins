import json
import datetime

from schedule import Schedule

def lambda_handler(event, context):
    bins = []
    schedule = Schedule()

    with open('./bins.json') as binsData:
        bins = json.loads(binsData.read())

    

    for collection in bins:
        schedule.add(collection['date'], collection['bins'])

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    collections = schedule.onDate(tomorrow.strftime("%Y-%m-%d"))

    return {
        "statusCode": 200,
        "body": json.dumps(
            { "message": collections }
        ),
    }

if __name__ == '__main__':
     lambda_handler(None, None)