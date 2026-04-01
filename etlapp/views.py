from django.shortcuts import render, redirect
import csv
from django.core.files.storage import FileSystemStorage
from .etl import run_etl
from .models import StudentReport

def upload_and_run(request):
    if request.method == "POST":
        file = request.FILES['csvfile']
        
        with open("students.csv", "wb+") as f:
            for chunk in file.chunks():
                f.write(chunk)
                
        run_etl()
        
        return redirect("success")
    return render(request, "upload.html")

def success(request):
    reports = StudentReport.objects.all()
    return render(request, "success.html", {"reports": reports})
