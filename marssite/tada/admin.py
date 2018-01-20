from django.contrib import admin

#from natica.models import Site,Telescope,Instrument
#from .models import ObsType, ProcType, ProdType
from .models import RawKeywords, FilenameKeywords
from .models import IngestKeywords, IngestRecommendedKeywords
from .models import SupportKeywords, FloatKeywords, HdrFunc
from .models import ErrorCode


#!@admin.register(Site)
#!class SiteAdmin(admin.ModelAdmin):
#!    pass
#!
#!@admin.register(Telescope)
#!class TelescopeAdmin(admin.ModelAdmin):
#!    pass
#!
#!@admin.register(Instrument)
#!class InstrumentAdmin(admin.ModelAdmin):
#!    list_display = ('name',)    
#!



@admin.register(IngestRecommendedKeywords)
class IngestRecommendedKeywordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment')


admin.site.register(RawKeywords)
admin.site.register(FilenameKeywords)
admin.site.register(IngestKeywords)
admin.site.register(SupportKeywords)
admin.site.register(FloatKeywords)

@admin.register(HdrFunc)
class HdrFuncAdmin(admin.ModelAdmin):
    list_display = ('name', 'documentation', 'inkeywords', 'outkeywords')


@admin.register(ErrorCode)
class ErrorCodeAdmin(admin.ModelAdmin):
    list_display = ('name','regexp', 'shortdesc')
    
