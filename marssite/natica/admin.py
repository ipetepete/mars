from django.contrib import admin
from .models import Site,Telescope,Instrument,TacInstrumentAlias
from .models import FilePrefix
from .models import ObsType, ProcType, ProdType

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass

@admin.register(Telescope)
class TelescopeAdmin(admin.ModelAdmin):
    pass

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    pass

@admin.register(TacInstrumentAlias)
class TacInstrumentAliasAdmin(admin.ModelAdmin):
    list_display = ('tac','hdr')


@admin.register(FilePrefix)
class FilePrefixAdmin(admin.ModelAdmin):
    #!list_display = ('site__name', 'telescope__name','instrument__name', 'prefix', 'comment')
    list_display = ('site', 'telescope','instrument', 'prefix', 'comment')

@admin.register(ObsType)
class ObsTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(ProcType)
class ProcTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(ProdType)
class ProdTypeAdmin(admin.ModelAdmin):
    pass
