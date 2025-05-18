from django.contrib import admin
from .models import Cliente, Reserva, Calendario

admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Calendario)