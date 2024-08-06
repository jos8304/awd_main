import csv
from django.core.management.base import BaseCommand
from dataentry.models import Student
import datetime

class Command(BaseCommand):
    help ="Export data from Student model to CSV"

    def handle(self, *args,**kwargs):
        students = Student.objects.all()        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
        file_path = f'exported_students_data_{timestamp}.csv'

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(['Rool No','name','Age'])

            for student in students:
                writer.writerow([student.roll_no, student.name, student.age])
        self.stdout.write(self.style.SUCCESS("Success"))       