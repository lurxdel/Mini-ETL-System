import csv
from .models import ETLRecord
from django.conf import settings
import os

def run_etl():
    # Clear existing records first
    ETLRecord.objects.all().delete()
    
    csv_path = os.path.join(settings.BASE_DIR, 'students.csv')
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            records = []
            for row in reader:
                # Filter out empty keys (like the index column in user's CSV)
                clean_row = {k.strip(): v.strip() for k, v in row.items() if k and k.strip()}
                
                # Basic transformation: fix missing values in ANY field
                for key, value in clean_row.items():
                    if not value:
                        clean_row[key] = f"Unknown {key.capitalize()}"
                
                records.append(ETLRecord(data=clean_row))
            
            # Bulk create for performance if the file is large
            ETLRecord.objects.bulk_create(records)
            
    except FileNotFoundError:
        print(f"Error: {csv_path} not found.")
    except Exception as e:
        print(f"ETL Error: {e}")
