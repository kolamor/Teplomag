from django.contrib import admin
from ticket.models import Scont, IndexPrimary, About, PriceUslugi, Tag
from ticket.models import CatSchetchic, VodTepSchetchic, Schetchic, Du


class SchetchicAdmin(admin.ModelAdmin):
	
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title',  )


# Register your models here.



# admin.site.register(Scont)
# admin.site.register(IndexPrimary)
# admin.site.register(About)
# admin.site.register(PriceUslugi)

admin.site.register(CatSchetchic, SchetchicAdmin)
admin.site.register(VodTepSchetchic, SchetchicAdmin)
admin.site.register(Schetchic, SchetchicAdmin)
admin.site.register(Du, SchetchicAdmin)

admin.site.register(Tag)
