from django.db import models


class Zone(models.Model):
    domain_name = models.CharField(max_length=30)

    primary_name_server = models.CharField(max_length=30) #e.g., ns1.globo.com
    #--------------------
    child_domain = models.CharField(max_length=30) #YES/NO REMOVE THIS FIELD
    #--------------------
    parent_domain = models.CharField(max_length=30) #e.g. globo.com/NA


class Records(models.Model):
    host_name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    content = models.CharField(max_length=30)
    domain = models.CharField(max_length=30)