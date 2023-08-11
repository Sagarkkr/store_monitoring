import csv

from store_app.constants import STATUS_CSV_PATH, BUSINESS_HOURS_CSV_PATH, TIMEZONE_STORE_CSV_PATH

from store_app.models import StoreStatus 
 

def update_status():
    with open(STATUS_CSV_PATH, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for store in csv_reader:
            StoreStatus.objects.update_or_create(**store)

