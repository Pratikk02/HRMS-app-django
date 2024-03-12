# Generated by Django 5.0.3 on 2024-03-12 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms_app', '0007_emp_end_date_emp_reason_emp_start_date_emp_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='emp_code',
            field=models.IntegerField(unique=True),
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('number_days', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('full', 'Full'), ('half', 'Half')], max_length=10)),
                ('reason', models.TextField()),
                ('ecode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrms_app.emp', to_field='emp_code')),
            ],
        ),
    ]
