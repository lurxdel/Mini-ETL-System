from django.shortcuts import render, redirect
import csv
from django.core.files.storage import FileSystemStorage
from .etl import run_etl
from .models import ETLRecord

from django.conf import settings
import os

def upload_and_run(request):
    if request.method == "POST":
        file = request.FILES['csvfile']
        
        csv_path = os.path.join(settings.BASE_DIR, 'students.csv')
        with open(csv_path, "wb+") as f:
            for chunk in file.chunks():
                f.write(chunk)
                
        run_etl()
        
        return redirect("success")
    return render(request, "upload.html")

def success(request):
    records = ETLRecord.objects.all()
    headers = []
    rows = []
    
    if records.exists():
        # Use the first record to determine the column order
        headers = list(records[0].data.keys())
        for r in records:
            # Create a list of values in the same order as the headers
            rows.append([r.data.get(h, "") for h in headers])
            
    return render(request, "success.html", {
        "headers": headers,
        "rows": rows
    })
