# Generated by Django 3.2 on 2024-08-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0011_remove_tickets_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='ticket_id',
            field=models.CharField(default=1234, max_length=20),
            preserve_default=False,
        ),
    ]
