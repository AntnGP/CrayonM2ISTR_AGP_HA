from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Ville)
admin.site.register(models.Local)
admin.site.register(models.Siege)
admin.site.register(models.Machine)
admin.site.register(models.Usine)


