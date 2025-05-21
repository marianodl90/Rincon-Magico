from django.contrib import admin
from .models import Cliente, Plaza, Reserva

admin.site.register(Cliente)
admin.site.register(Plaza)
admin.site.register(Reserva)