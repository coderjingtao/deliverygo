# Generated by Django 2.1 on 2018-08-24 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0002_risk_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(db_column='aname', max_length=20, verbose_name='area_name'),
        ),
    ]
