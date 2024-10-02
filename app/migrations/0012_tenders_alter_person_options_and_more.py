# Generated by Django 5.0.6 on 2024-09-19 05:22

import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_person_persontranslation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.IntegerField(blank=True, null=True)),
                ('end_time', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Tender',
                'verbose_name_plural': 'Tenders',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'Persons'},
        ),
        migrations.AlterModelOptions(
            name='persontranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'Person Translation'},
        ),
        migrations.CreateModel(
            name='TendersTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=1000, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='app.tenders')),
            ],
            options={
                'verbose_name': 'Tender Translation',
                'db_table': 'app_tenders_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
