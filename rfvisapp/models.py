from django.db import models

# Create your models here.
class  Sensor(models.Model):
	name = models.CharField(max_length=10)
	def __str__(self):
		return (self.name)

class Message(models.Model):
	Sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
	LOB 		= models.CharField(max_length=3)
	LOBAVG 		= models.FloatField()
	RATIO 		= models.FloatField()
	SDEU 		= models.FloatField()
	AGE 		= models.FloatField()
	DATE 		= models.CharField(max_length=50)
	DATETIMESTAMP 	= models.FloatField()
	LONG 		= models.FloatField()
	DEVICE_NAME  	= models.CharField(max_length=10)
	COMPASS 	= models.FloatField()
	NS		= models.IntegerField()
	YAW		= models.FloatField()
	PITCH		= models.FloatField()
	HEIGHT          = models.FloatField()
	Q		= models.IntegerField()
	Y= 	models.FloatField()
	X= 	models.FloatField()
	Z= 	models.FloatField()
	SDU= 	models.FloatField()
	SDNE= 	models.FloatField()
	SDUN= 	models.FloatField()
	SDE= 	models.FloatField()
	TIME = 	models.CharField(max_length=50)
	LAT = 	models.FloatField()
	SDN = 	models.FloatField()
	ROLL = 	models.FloatField()

class Target(models.Model):
	Name = models.CharField(max_length=10)
	LAT = models.FloatField()
	LON = models.FloatField()
	HEIGHT= models.FloatField()
	Power = models.FloatField()
	Freq = models.FloatField()
