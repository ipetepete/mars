import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from .models import AuditRecord

class AuditRecordTable(tables.Table):
    class Meta:
        model = AuditRecord
        fields = ('instrument',
                  'notReceived',
                  'rejected',
                  'accepted' )


class ProgressTable(tables.Table):
    # TODO: link ObsDay to admin/schedule/slot (date,tele,instrument)
    #!ObsDay = tables.DateColumn(short=True, verbose_name='CALDAT')
    #!ObsDay =  tables.LinkColumn(verbose_name='CALDAT',
    #!                            viewname='admin:schedule_slot_changelist',
    #!                            kwargs={"obsdate__exact": A('ObsDay')})
    ObsDay =  tables.TemplateColumn(verbose_name='CALDAT',
                                     template_code='<a href="http://localhost:8000/admin/schedule/slot/?obsdate__exact={{record.ObsDay}}">{{record.ObsDay}}</a>')
                                         
    Telescope = tables.Column()
    Instrument = tables.Column()

    #!Ground_Truth = tables.Column()    
    #!Database = tables.Column()    
    #!Delta = tables.Column()    
    #!Updated = tables.DateTimeColumn(short=True)    
    Propid = tables.TemplateColumn('<a href="http://www.noao.edu/noaoprop/abstract.mpl?{{record.Propid}}">{{record.Propid}}</a>')

    # These are "jammed" counts;
    # TODO: link to admin/audit page filtered to the N records that contribute to the aggregate
    # TODO: render negative as red
    # TODO: add jammed at Mountain
    dome = tables.Column(verbose_name='Truth')
    notReceived = tables.Column(verbose_name='Mtn/Dome Jam') # jammed at dome + jammed at mtn
    rejected =  tables.Column(verbose_name='Ingest Rejected')
    #!rejected =  tables.LinkColumn(verbose_name='Ingest Rejected',
    #!                              viewname='schedule:getpropid',
    #!                              args=[A('Telescope'), A('Instrument'), A('ObsDay')])
    rejected =  tables.TemplateColumn(verbose_name='Ingest Rejected',
                                     template_code='<a href="http://localhost:8000/admin/audit/auditrecord/?instrument__exact={{record.Instrument}}&obsday__exact={{record.ObsDay}}&success__exact=0">{{record.rejected}}</a>')

    accepted =  tables.Column(verbose_name='Ingested')
    # TODO: add columns; sent from Dome, received Mtn, received Valley, Submitted to Archive

    
    class Meta:
        attrs = {'class': 'progress'}
        row_attrs = {
            'class': lambda record: 'day-even' if (int(str(record['ObsDay'])[-1]) % 2) == 0 else 'day-odd'
            #'row-odd': 3
            }
