import csv
from .models import StudentReport

def run_etl():
    try:
        with open('students.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                student_id = row.get('id', '').strip()
                name = row.get('name', '').strip()
                course = row.get('course', '').strip()
                
                if not name:
                    name = "Unknown Name"
                if not course:
                    course = "Unknown Course"
                    
                if student_id:
                    StudentReport.objects.update_or_create(
                        student_id=student_id,
                        defaults={'name': name, 'course': course}
                    )
    except FileNotFoundError:
        pass
