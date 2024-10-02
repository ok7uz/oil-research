# Generated by Django 5.0.6 on 2024-09-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_financialdata_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialdata',
            name='values',
            field=models.ManyToManyField(through='app.FinancialYearData', to='app.year'),
        ),
    ]
