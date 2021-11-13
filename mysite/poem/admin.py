from django.contrib import admin
from .models import poem
from .models import poet

admin.site.register(poem)
admin.site.register(poet)