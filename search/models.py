from django.db import models

class Release(models.Model):
    number = models.CharField(max_length=50)
    notes = models.CharField(max_length=50)
    changes = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.number



class Metamodule(models.Model):
    name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    release = models.ForeignKey(Release)
    owner = models.CharField(max_length=50)
    createdate = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    metamodules = models.ManyToManyField(Metamodule,related_name='metaname',blank=True)
    createdate = models.DateTimeField(auto_now=True)
    manager = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)


    def __unicode__(self):
        return self.name

   
class Moduledep(models.Model):
    modulename = models.ManyToManyField(Module,related_name='modlname',blank=True)
    dependent = models.CharField(max_length=50)

    def __unicode__(self):
        return self.dependent
