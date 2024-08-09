from awd_main.celery import app
from django.core.management import call_command
import time
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import send_email_notification,generate_csv_file

@app.task
def celery_test_task():
    time.sleep(10)
    #send an email
    mail_subject = 'Test subject'
    message = 'This is a test'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = settings.DEFAULT_TO_EMAIL
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.send()
    return "Task successfully"

@app.task
def import_data_task(file_path, model_name):
    try:
        call_command('importdata',file_path, model_name)
    except Exception as e:
        raise e    
    mail_subject = 'Import Data Completed'
    message = 'You data import has been successful'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email)
    return 'Data imported successfully'

@app.task
def export_data_task(model_name):
    try:
        call_command('exportdata',model_name)
    except Exception as e:
        raise e
    
    file_path = generate_csv_file(model_name)
    
    mail_subject = 'Export Data Completed'
    message = 'You data export has been successful'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email, attachment = file_path )
    return 'Data exported successfully'