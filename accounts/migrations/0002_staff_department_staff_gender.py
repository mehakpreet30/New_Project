# Generated by Django 4.1 on 2022-08-16 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.CharField(max_length=100, null=True, verbose_name='Department'),
        ),
        migrations.AddField(
            model_name='staff',
            name='gender',
            field=models.CharField(max_length=10, null=True, verbose_name='Gender'),
        ),
    ]