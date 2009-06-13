from django.db import models

# Create your models here.

class Tests(models.Model):
    #ID = models.AutoField(primary_key=True)
    name = models.TextField(default = '')
    created = models.DateTimeField()
    comment = models.TextField(default = '')
    localId = models.IntegerField(default = 0)

    class Meta:
        db_table = 'Tests'
    
    def __unicode(self):
        return self.name

class Results(models.Model):
    testID = models.IntegerField(null = False, default = 0)
    metricName = models.CharField(max_length = 512,default = '')
    value = models.FloatField(default = 0)
    negativeEnd = models.TextField(default = '')
    positiveEnd = models.TextField(default = '')

    class Meta:
        db_table = 'Results'

    def __unicode(self):
        return self.negativeEnd

class Parameters(models.Model):
    name = models.CharField(max_length = 256)
    value = models.IntegerField(null = False)
    testID = models.IntegerField(null = False, default = 1)

    class Meta:
        db_table = 'Parameters'

    def __unicode(self):
        return self.name

class CommunicationTimes(models.Model):
    testID = models.IntegerField(null = False, default = 0)
    fromApp = models.CharField(max_length = 50)
    toApp = models.CharField(max_length = 50)
    value = models.IntegerField(null = False, default = 0)

    class Meta:
        db_table = 'CommunicationTimes'


    def __unicode(self):
        return self.testID

class Plot(models.Model):
    startTestID = models.IntegerField(null = False, default = 0)
    endTestID = models.IntegerField(null = False, default = 0)
    imageName = models.TextField(default='')

    class Meta:
        db_table = 'Plots'
    
    def __unicode(self):
        return self.plotAddr
