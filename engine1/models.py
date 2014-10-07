from django.db import models

class Keyword(models.Model):
    name=models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

class Website(models.Model):
    name=models.CharField(max_length=30)
    url=models.URLField(max_length=50)
    number=models.DecimalField(max_digits=5, decimal_places=4)
    words=models.ManyToManyField(Keyword)
    references=models.ManyToManyField('self',symmetrical=False,related_name="+")
    referenced_by=models.ManyToManyField('self',symmetrical=False,related_name="+")

    def __unicode__(self):
        return '%s %s' %(self.name, self.url)
