from django.core.management.base import BaseCommand
from django.apps import apps
import csv
from dataentry.utils import check_csv_errors


class Command(BaseCommand):
    help = "Import data from CVS file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Name of the model')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()       
        
        model = check_csv_errors(file_path, model_name)

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)       
            for row in reader:
                model.objects.create(**row)           
        self.stdout.write(self.style.SUCCESS("Success"))