import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mini_etl.settings')
django.setup()

from django.test import Client

def run_test():
    c = Client()
    with open('test_students.csv', 'rb') as f:
        response = c.post('/etl/', {'csvfile': f})
        
    print("Response status:", response.status_code)
    try:
        print("Response redirect URL:", response.url)
    except AttributeError:
        pass
        
    response2 = c.get('/etl/success/')
    print("Success view output:")
    print(response2.content.decode('utf-8'))

if __name__ == '__main__':
    run_test()
