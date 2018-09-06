from django.db import models

# Create your models here.
class Risk(models.Model):
    id = models.IntegerField(primary_key=True, db_column='rid',verbose_name='risk_id')
    name = models.CharField(max_length=20,db_column='rname',verbose_name='risk_name')
    level = models.IntegerField(default=0,db_column='rlevel',verbose_name='risk_level')
    desp = models.CharField(max_length=50, db_column='rdesp', verbose_name='risk_description')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_risk'

class Area(models.Model):
     id = models.IntegerField(primary_key=True, db_column='aid',verbose_name='area_id')
     name = models.CharField(max_length=20,db_column='aname',verbose_name='area_name')
     risk = models.ForeignKey(Risk,db_column='rid',on_delete=models.PROTECT,verbose_name='risk_level')

     def __str__(self):
        return self.name

     class Meta:
         db_table = 't_area'