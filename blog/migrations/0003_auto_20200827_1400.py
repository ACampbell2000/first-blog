# Generated by Django 2.2.15 on 2020-08-27 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='grades',
            field=models.TextField(default='Enter Grades'),
        ),
        migrations.AddField(
            model_name='cv',
            name='personal_statement',
            field=models.TextField(default='Enter Personal Statement'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
