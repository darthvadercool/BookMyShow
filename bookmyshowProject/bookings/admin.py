from django.contrib import admin

from .models import Seattype, Seats, Shows, Showtiming, Booking, Ticket

admin.site.register(Seattype)
admin.site.register(Seats)
admin.site.register(Showtiming)
admin.site.register(Shows)
admin.site.register(Booking)
admin.site.register(Ticket)
