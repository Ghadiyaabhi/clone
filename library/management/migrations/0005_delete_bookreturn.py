# Generated by Django 5.0.3 on 2024-03-22 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_returningbook_borrower'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookReturn',
        ),
    ]