import os
from django.conf import settings




CSV_FOLDER = os.path.join(settings.BASE_DIR, "")



STATUS_CSV_PATH = os.path.join(CSV_FOLDER, "csv_data/store status.csv")
BUSINESS_HOURS_CSV_PATH = os.path.join(CSV_FOLDER, "csv_data/Menu hours.csv")
TIMEZONE_STORE_CSV_PATH = os.path.join(CSV_FOLDER, "csv_data/bq-results-20230125-202210-1674678181880.csv")



print(STATUS_CSV_PATH)