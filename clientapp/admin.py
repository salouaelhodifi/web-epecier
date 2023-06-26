from django.contrib import admin
from .models import Client,ClientAdmin
admin.site.register(Client,ClientAdmin)

