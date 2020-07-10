import json
import os
from datetime import datetime, timedelta

import boto3
import pytz
import schedule
import time
import sensor
import weather

AWS_PROFILE = os.getenv('AWS_PROFILE')
SQS_QUEUE_URL = os.getenv('SQS_QUEUE_URL')


def send_data_to_data_firehose():
    # polish timestamp
    current_time = datetime.now(pytz.UTC)
    current_time -= timedelta(seconds=current_time.second, microseconds=current_time.microsecond)

    # sensor readings
    payload = {
        'timestamp': current_time.isoformat().replace('+00:00', 'Z')
    }
    payload.update(sensor.get_sensor_readings())
    payload.update(weather.get_weather_data())

    # send data to Firehose
    session = boto3.Session(profile_name=AWS_PROFILE)
    sqs = session.client('firehose')
    sqs.put_record(
        DeliveryStreamName='sensor-readings',
        Record={
            'Data': json.dumps(payload)
        }
    )


schedule.every().minute.at(':00').do(send_data_to_data_firehose)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(0.9)
