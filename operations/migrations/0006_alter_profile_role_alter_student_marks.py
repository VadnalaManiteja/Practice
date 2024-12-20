# Generated by Django 5.1.2 on 2024-11-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0005_alter_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('employee', 'Employee'), ('student', 'Student'), ('staff', 'Staff')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='marks',
            field=models.CharField(max_length=3),
        ),
    ]
