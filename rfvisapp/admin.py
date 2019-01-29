from django.contrib import admin

# Register your models here.

from .models import Sensor
from .models import Message
from .models import Target
admin.site.register(Sensor)
admin.site.register(Message)
admin.site.register(Target)
