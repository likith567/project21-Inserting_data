from app.forms import WebpageForm, studentForm
from django.contrib import admin
from app.models import Topic

# Register your models here.
from app.models import *

admin.site.register(Topic)
admin.site.register(Webpage)