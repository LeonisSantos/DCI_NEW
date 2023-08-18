from django.contrib import admin
from dci.models import EtpOnline, OesDci, OtsDCI, DciGerada


class ListandoEtps(admin.ModelAdmin):
    list_display = ('id', 'etp', 'elaborador', 'vendor')
    list_display_links = ('id', 'etp')
    search_fields = ('etp', )
    list_per_page = 50


class ListandoOes(admin.ModelAdmin):
    list_display = ('id', 'oe_id', 'num_oe', 'descricao', 'status')
    list_display_links = ('oe_id', 'num_oe', 'descricao')
    search_fields = ('descricao', )
    search_fields = ('etp_vinculada', )
    list_filter = ('status', )
    list_per_page = 50


class ListandoOts(admin.ModelAdmin):
    list_display = ('id', 'etp_vinculada', 'ots_id',
                    'num_ots', 'sigla', 'proprietario')
    list_display_links = ('ots_id', 'num_ots', 'etp_vinculada')
    search_fields = ('etp_vinculada', )
    list_per_page = 50


class ListandoDci(admin.ModelAdmin):
    list_display = ('id', 'etp_value', 'hora_geracao')
    list_display_links = ('id', 'etp_value')
    search_fields = ('etp_value', )
    list_per_page = 50


admin.site.register(EtpOnline, ListandoEtps)

admin.site.register(OesDci, ListandoOes)

admin.site.register(OtsDCI, ListandoOts)

admin.site.register(DciGerada, ListandoDci)
