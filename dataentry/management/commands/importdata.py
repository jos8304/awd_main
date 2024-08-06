from django.core.management.base import BaseCommand, CommandParser
from dataentry.models import Student
import csv

class Command(BaseCommand):
    help = "Import data from CVS file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Name of the model')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        model = None
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                Student.objects.create(**row)
            #     roll_no = data['roll_no']
            #     existing_record = Student.objects.filter(roll_no=roll_no).exists()    
                
            # if not existing_record:
            #     Student.objects.create(**row)
            # else:
            #     self.stdout.write(self.style.WARNING(f'Student with roll no {roll_no}'))
        self.stdout.write(self.style.SUCCESS("Success"))