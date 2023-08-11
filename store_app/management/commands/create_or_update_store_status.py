import csv
from datetime import datetime, timezone
from dateutil.parser import parse

from django.core.management.base import BaseCommand

from store_app.models import StoreStatus
from store_app.constants import STATUS_CSV_PATH



class Command(BaseCommand):

    def handle(self, *args, **options):
        print(STATUS_CSV_PATH)
        try:
            data = []
            with open(STATUS_CSV_PATH, 'r') as store_status_file:
                store_records = csv.DictReader(store_status_file)
                for record in store_records:
                    timestamp_utc = datetime.utcfromtimestamp(parse(record.pop("timestamp_utc")).timestamp())
                    store_status, status = StoreStatus.objects.update_or_create(**record, timestamp_utc=timestamp_utc)


        except FileNotFoundError:
            print(f"Error: store status file not found.")

        except ValueError as e:
            print(f"Error: CSV file contains invalid data. {str(e)}")