from django.contrib import admin
from INDIGGator.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(KYCData)
admin.site.register(Question)
admin.site.register(NoOfWeeks)