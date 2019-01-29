from django.shortcuts import render
from django.http import HttpResponse
from .models import Message, Sensor
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import json


@csrf_exempt
def index(request):
	if request.method=='PUT':
		dir(request.body)
		print("Received %s" % request.body.decode('utf-8'))
		data = json.loads(request.body.decode('utf-8'))
		print ("Got json: %s" % data)
		#sensor = Sensor.objects.get(name = data['DEVICE_NAME'])
		sensor = Sensor.objects.get(name="DDF_RPI_1")
		print(sensor)
		newMessage = Message()
		newMessage.Sensor = sensor
		newMessage.LOB = data['LOB'] #LOB = models.CharField(max_length=3)
		newMessage.LOBAVG = data['LOBAVG'] #LOBAVG = models.FloatField()
		newMessage.RATIO = data['RATIO'] #RATIO = models.FloatField()
		newMessage.SDEU = data['SDEU'] #SDEU = models.FloatField()
		newMessage.AGE = data['AGE'] #AGE = models.FloatField()
		newMessage.DATE = data['DATE'] #DATE = models.CharField(max_length=50)
		newMessage.DATETIMESTAMP = data['DATETIMESTAMP'] #DATETIMESTAMP = models.FloatField()
		newMessage.LONG = data['LONG'] #LONG = models.FloatField()
		newMessage.DEVICE_NAME = data['DEVICE_NAME'] #DEVICE_NAME = models.CharField(max_length=10)
		newMessage.COMPASS = data['COMPASS'] #COMPASS = models.FloatField()
		newMessage.NS = data['NS'] #NS = models.IntegerField()
		newMessage.YAW = data['YAW'] #YAW = models.FloatField()
		newMessage.PITCH = data['PITCH'] #PITCH	= models.FloatField()
		newMessage.HEIGHT = data['HEIGHT'] #HEIGHT = models.FloatField()
		newMessage.Q = data['Q'] #Q= models.IntegerField()
		newMessage.Y = data['Y'] #Y= models.FloatField()
		newMessage.X = data['X'] #X= models.FloatField()
		newMessage.Z = data['Z'] #Z= models.FloatField()
		newMessage.SDU = data['SDU'] #SDU= models.FloatField()
		newMessage.SDNE = data['SDNE'] #SDNE= models.FloatField()
		newMessage.SDUN = data['SDUN'] #SDUN= models.FloatField()
		newMessage.SDE = data['SDE'] #SDE= models.FloatField()
		newMessage.TIME = data['TIME'] #TIME = models.CharField(max_length=50)
		newMessage.LAT = data['LAT'] #LAT = models.FloatField()
		newMessage.SDN = data['SDN'] #SDN = models.FloatField()
		newMessage.ROLL = data['ROLL'] #ROLL = models.FloatField()
		if(newMessage.save()=='None'):
			response='received'
		else:
			response = 'problem detected'
	else:
		response='SEGLOGGER MAIN'
	messages_list = list(Message.objects.order_by('DATETIMESTAMP'))
	context = {'Messages': messages_list}
	#return data['DEVICE_NAME']#return HttpResponse("Hello, world. You're at the polls index.")
	#return HttpResponse(messages_list)
	template = loader.get_template('rfvisapp/index.html')
	return HttpResponse(template.render(context, request))

def detail(request):
	try:
		message_list = Message.objects.all
		context = {'message', message_list}
	except:
		raise Http404("Message does not exist")
	return render(request, 'rfvisapp/detail.html', context)
