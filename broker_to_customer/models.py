from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField

# Create your models here.
class User_Devices(models.Model):
    user_id = models.CharField(db_index=True, max_length=255)
    device_id = models.CharField(db_index=True, max_length=255)

    class Meta:
        db_table = 'user_devices_hack17'

class User_Details(models.Model):
    user_id = models.CharField(db_index=True, max_length=255)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'user_details_hack17'

class User_Requirements(models.Model):
    user_id = models.CharField(db_index=True, max_length=255)
    requirements = JSONField()
    requirement_id = models.IntegerField()

    class Meta:
        db_table = 'user_requirements_hack17'
