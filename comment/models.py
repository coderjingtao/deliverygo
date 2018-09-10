from django.db import models
from django.db.models import PROTECT

# Create your models here.
class City(models.Model):
    id = models.AutoField(primary_key=True, db_column='city_id', verbose_name='city_id')
    name = models.CharField(max_length=50, db_column='city_name', verbose_name='city_name')
    parent = models.CharField(max_length=50, db_column='parent_city', verbose_name='parent_city',default="Melbourne")
    state = models.CharField(max_length=50, db_column='state', verbose_name='state',default="Victoria")
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta(object):
        db_table = 't_city'
        verbose_name = 'city'
        verbose_name_plural = 'cities'

class Suburb(models.Model):
    id = models.AutoField(primary_key=True, db_column='suburb_id', verbose_name='suburb_id')
    name = models.CharField(max_length=50, db_column='suburb_name', verbose_name='suburb_name')
    postcode = models.CharField(max_length=4, db_column='postcode', verbose_name='postcode')
    city = models.ForeignKey(City, db_column='city_id', on_delete=PROTECT, related_name='+', verbose_name='city')
    good_count = models.IntegerField(default=0, db_column='good_count', verbose_name='good_count')
    bad_count = models.IntegerField(default=0, db_column='bad_count', verbose_name='bad_count')
    star_total = models.FloatField(default=0, db_column='star_total',verbose_name='star_total')
    star_count = models.IntegerField(default=0, db_column='star_count',verbose_name='star_count')

    def _averageStar(self):
        if self.star_count != 0 :
            return round( (self.star_total / self.star_count),2 )
        else:
            return 0
    rating = property(_averageStar)

    objects = models.Manager()

    class Meta(object):
        db_table = 't_suburb'
        verbose_name = 'suburb'
        verbose_name_plural = 'suburbs'

class CityRisk(models.Model):
    id = models.AutoField(primary_key=True, db_column='city_id', verbose_name='city_id')
    name = models.CharField(max_length=50, db_column='city_name', verbose_name='city_name')
    c1a = models.IntegerField(default=0, db_column='c1a', verbose_name='c1a')
    c2a = models.IntegerField(default=0, db_column='c2a', verbose_name='c2a')
    c3a = models.IntegerField(default=0, db_column='c3a', verbose_name='c3a')
    c4a = models.IntegerField(default=0, db_column='c4a', verbose_name='c4a')
    c5a = models.IntegerField(default=0, db_column='c5a', verbose_name='c5a')
    c6a = models.IntegerField(default=0, db_column='c6a', verbose_name='c6a')
    c7a = models.IntegerField(default=0, db_column='c7a', verbose_name='c7a')
    c8a = models.IntegerField(default=0, db_column='c8a', verbose_name='c8a')
    c9a = models.IntegerField(default=0, db_column='c9a', verbose_name='c9a')
    c10a = models.IntegerField(default=0, db_column='c10a', verbose_name='c10a')
    c11a = models.IntegerField(default=0, db_column='c11a', verbose_name='c11a')
    c12a = models.IntegerField(default=0, db_column='c12a', verbose_name='c12a')
    c1p = models.IntegerField(default=0, db_column='c1p', verbose_name='c1p')
    c2p = models.IntegerField(default=0, db_column='c2p', verbose_name='c2p')
    c3p = models.IntegerField(default=0, db_column='c3p', verbose_name='c3p')
    c4p = models.IntegerField(default=0, db_column='c4p', verbose_name='c4p')
    c5p = models.IntegerField(default=0, db_column='c5p', verbose_name='c5p')
    c6p = models.IntegerField(default=0, db_column='c6p', verbose_name='c6p')
    c7p = models.IntegerField(default=0, db_column='c7p', verbose_name='c7p')
    c8p = models.IntegerField(default=0, db_column='c8p', verbose_name='c8p')
    c9p = models.IntegerField(default=0, db_column='c9p', verbose_name='c9p')
    c10p = models.IntegerField(default=0, db_column='c10p', verbose_name='c10p')
    c11p = models.IntegerField(default=0, db_column='c11p', verbose_name='c11p')
    c12p = models.IntegerField(default=0, db_column='c12p', verbose_name='c12p')
    objects = models.Manager()

    class Meta(object):
        db_table = 't_cityrisk'
        verbose_name = 'cityrisk'
        verbose_name_plural = 'cityrisks'