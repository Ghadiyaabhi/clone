# Generated by Django 5.0.3 on 2024-03-28 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_forgetpassword_forgotpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(blank=True, max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
