from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name

class Tickets(models.Model):
    ticket_id = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    station_id = models.CharField(max_length=20)
    sent_a_report_to_WMATA = models.CharField(max_length=20)
    mezzanine_id = models.CharField(max_length=20)
    mezzanine_name = models.CharField(max_length=20)
    incident_description = models.CharField(max_length=100)
    maximo = models.CharField(max_length=20)
    requester_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    incident_date = models.DateField(null=True)
    faregate_no = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    related_parts = models.CharField(max_length=20)
    priority = models.CharField(max_length=20)
    old_serial_no = models.CharField(max_length=20)
    new_serial_no = models.CharField(max_length=20)
    received_by = models.CharField(max_length=20)
    Technician = models.CharField(max_length=20)
    related_system = models.CharField(max_length=20)
    action_logs = models.CharField(max_length=500)
    date = models.DateField(null=True)
    modified_date = models.DateField(null=True)
    modified_by = models.CharField(max_length=500)


    def __str__(self):
        return self.ticket_id

class Employee(models.Model) :
    employee_id = models.IntegerField()
    employee_name = models. CharField(max_length=25)
    designation = models.CharField(max_length=25)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    retirement = models.DecimalField(max_digits=10, decimal_places=2)
    other_benefits = models.DecimalField(max_digits=10, decimal_places=2)
    total_benefits = models.DecimalField(max_digits=10, decimal_places=2)
    total_compensation = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.employee_name+' - '+ self.designation