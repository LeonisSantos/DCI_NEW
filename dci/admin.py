from django.contrib import admin
from dci.models import DciOnline, OesDci


class ListandoEtps(admin.ModelAdmin):
    list_display = ('id', 'etp', 'elaborador', 'vendor')
    list_display_links = ('id', 'etp')
    search_fields = ('etp', )
    list_per_page = 50


class ListandoOes(admin.ModelAdmin):
    list_display = ('id', 'oe_id', 'num_oe', 'descricao')
    list_display_links = ('oe_id', 'num_oe', 'descricao')
    search_fields = ('descricao', )
    list_per_page = 50


admin.site.register(DciOnline, ListandoEtps)

admin.site.register(OesDci, ListandoOes)
