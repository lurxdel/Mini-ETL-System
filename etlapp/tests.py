from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import StudentReport

class ETLTestCase(TestCase):
    def test_etl_upload(self):
        csv_content = b"id,name,course\n2023001,Juan Dela Cruz,BSIT\n2023002,,BSCS\n2023003,Ana Lopez,\n"
        csv_file = SimpleUploadedFile("students.csv", csv_content, content_type="text/csv")
        
        response = self.client.post('/etl/', {'csvfile': csv_file}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(StudentReport.objects.count(), 3)
        self.assertContains(response, "ETL Run Successful")
