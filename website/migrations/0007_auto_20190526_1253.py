# Generated by Django 2.2 on 2019-05-26 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_company_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_area',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
