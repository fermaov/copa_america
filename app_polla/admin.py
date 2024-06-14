from django.contrib import admin

from .models import Fase, Equipo, Partido, Finalistas, Marcador, Estado


admin.site.register(Fase)
admin.site.register(Equipo)
admin.site.register(Partido)
admin.site.register(Finalistas)
admin.site.register(Marcador)
admin.site.register(Estado)
