from django.contrib import admin

from .models import State
from .models import City
from .models import Citizen
from .models import Officer
from .models import Ngo


admin.site.register(State)
admin.site.register(City)
admin.site.register(Citizen)
admin.site.register(Officer)
admin.site.register(Ngo)
