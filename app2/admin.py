from django.contrib import admin
from app1.models import *
from app2.models import *

# Register your models here.
admin.site.register(Country)
admin.site.register(Capital)
admin.site.register(Topic)