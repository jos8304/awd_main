from typing import Any
from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = 'database'

    def handle(self, *args, **kwargs):
        #add one data
        dataset = [
            {'roll_no': 1002, 'name': 'mike1','age': 21},
            {'roll_no': 1003, 'name': 'mike2','age': 22},
            {'roll_no': 1005, 'name': 'mike5','age': 50},
        ]
        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()

            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll no {roll_no}'))
        self.stdout.write(self.style.SUCCESS('Data success'))