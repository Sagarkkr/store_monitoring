import csv
from datetime import datetime, timezone
from dateutil.parser import parse

from django.core.management.base import BaseCommand

from store_app.models import Store
from store_app.constants import TIMEZONE_STORE_CSV_PATH



class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            data = []
            with open(TIMEZONE_STORE_CSV_PATH, 'r') as store_status_file:
                store_records = csv.DictReader(store_status_file)
                for record in store_records:
                    data.append(Store(**record))
            Store.objects.bulk_create(data)


        except FileNotFoundError:
            print(f"Error: store status file not found.")

        except ValueError as e:
            print(f"Error: CSV file contains invalid data. {str(e)}")