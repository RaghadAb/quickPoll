from django.contrib import admin
from .models import Poll
# Register your models here.
# the . simply means that the import is from the same directory

admin.site.register(Poll)
