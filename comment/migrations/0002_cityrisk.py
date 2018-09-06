# Generated by Django 2.1 on 2018-08-29 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityRisk',
            fields=[
                ('id', models.AutoField(db_column='city_id', primary_key=True, serialize=False, verbose_name='city_id')),
                ('name', models.CharField(db_column='city_name', max_length=50, verbose_name='city_name')),
                ('c1a', models.IntegerField(db_column='c1a', default=0, verbose_name='c1a')),
                ('c2a', models.IntegerField(db_column='c2a', default=0, verbose_name='c2a')),
                ('c3a', models.IntegerField(db_column='c3a', default=0, verbose_name='c3a')),
                ('c4a', models.IntegerField(db_column='c4a', default=0, verbose_name='c4a')),
                ('c5a', models.IntegerField(db_column='c5a', default=0, verbose_name='c5a')),
                ('c6a', models.IntegerField(db_column='c6a', default=0, verbose_name='c6a')),
                ('c7a', models.IntegerField(db_column='c7a', default=0, verbose_name='c7a')),
                ('c8a', models.IntegerField(db_column='c8a', default=0, verbose_name='c8a')),
                ('c9a', models.IntegerField(db_column='c9a', default=0, verbose_name='c9a')),
                ('c10a', models.IntegerField(db_column='c10a', default=0, verbose_name='c10a')),
                ('c11a', models.IntegerField(db_column='c11a', default=0, verbose_name='c11a')),
                ('c12a', models.IntegerField(db_column='c12a', default=0, verbose_name='c12a')),
                ('c1p', models.IntegerField(db_column='c1p', default=0, verbose_name='c1p')),
                ('c2p', models.IntegerField(db_column='c2p', default=0, verbose_name='c2p')),
                ('c3p', models.IntegerField(db_column='c3p', default=0, verbose_name='c3p')),
                ('c4p', models.IntegerField(db_column='c4p', default=0, verbose_name='c4p')),
                ('c5p', models.IntegerField(db_column='c5p', default=0, verbose_name='c5p')),
                ('c6p', models.IntegerField(db_column='c6p', default=0, verbose_name='c6p')),
                ('c7p', models.IntegerField(db_column='c7p', default=0, verbose_name='c7p')),
                ('c8p', models.IntegerField(db_column='c8p', default=0, verbose_name='c8p')),
                ('c9p', models.IntegerField(db_column='c9p', default=0, verbose_name='c9p')),
                ('c10p', models.IntegerField(db_column='c10p', default=0, verbose_name='c10p')),
                ('c11p', models.IntegerField(db_column='c11p', default=0, verbose_name='c11p')),
                ('c12p', models.IntegerField(db_column='c12p', default=0, verbose_name='c12p')),
            ],
            options={
                'verbose_name': 'cityrisk',
                'verbose_name_plural': 'cityrisks',
                'db_table': 't_cityrisk',
            },
        ),
    ]
