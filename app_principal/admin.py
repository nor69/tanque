from django.contrib import admin

from estadisticas.models import Estadistica
from repeticiones.models import Repeticione
from .models import*


class EstadisticaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "pais", "nivel",
                    "batallas", "victorias", "experiencia", "win8", "subtotal", "total", "garaje", "premium")
    search_fields = ("nombre", "tipo", "pais", "nivel", "garaje", "premium")
    list_filter = ("tipo", "pais", "nivel", "garaje", "premium")


class RepeticioneAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "pais", "destruidos",
                    "causado", "bloqueado", "detectado", "aturdimiento", "video", "premium")
    search_fields = ("nombre", "tipo", "pais", "destruidos", "premium")
    list_filter = ("tipo", "pais", "destruidos", "premium")


class RankingAdmin(admin.ModelAdmin):
    list_display = ("mejor", "actual", "peor")


class Win8Admin(admin.ModelAdmin):
    list_display = ("mejor", "actual", "peor")


class TanquesAdmin(admin.ModelAdmin):
    list_display = ("numero",)


admin.site.register(Estadistica, EstadisticaAdmin)
admin.site.register(Repeticione, RepeticioneAdmin)
admin.site.register(Ranking, RankingAdmin)
admin.site.register(Win8, Win8Admin)
admin.site.register(Tanque, TanquesAdmin)
