# Generated by Django 3.0.3 on 2020-07-23 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_procurement_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procurement',
            name='file',
        ),
        migrations.AlterField(
            model_name='procurementfiles',
            name='files',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Procurement'),
        ),
    ]
