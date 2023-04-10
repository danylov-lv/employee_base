# Generated by Django 4.2 on 2023-04-10 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_base_app', '0003_auto_20230406_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee_base_app.employee', verbose_name='Boss'),
        ),
    ]
