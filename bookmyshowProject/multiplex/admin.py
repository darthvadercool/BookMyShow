from django.contrib import admin

from .models import State, Country, City, Multiplex, Screen

admin.site.register(Country)
admin.site.register(State)

admin.site.register(City)
admin.site.register(Multiplex)
admin.site.register(Screen)
