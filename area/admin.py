from django.contrib import admin
from area.models import Ostan, Shahrestan, Bakhsh, Dehestan

class OstanAdmin(admin.ModelAdmin):
	list_display = ('position', 'title', "active")
	list_display_links = (['position'])
	list_editable = ("active",)
	list_filter = (['active'])
	search_fields = ('title',)


admin.site.register(Ostan, OstanAdmin)



class ShahrestanAdmin(admin.ModelAdmin):
	list_display = ('position', 'title', 'ostan', "active")
	list_display_links = (['position'])
	list_editable = ("active",)
	list_filter = (['active'])
	search_fields = ('title', 'ostan')


admin.site.register(Shahrestan, ShahrestanAdmin)




class BakhshAdmin(admin.ModelAdmin):
	list_display = ('position', 'title', 'shahrestan', "active")
	list_display_links = (['position'])
	list_editable = ("active",)
	list_filter = (['active'])
	search_fields = ('title', 'shahrestan')


admin.site.register(Bakhsh, BakhshAdmin)




class DehestanAdmin(admin.ModelAdmin):
	list_display = ('position', 'title', 'bakhsh', "active")
	list_display_links = (['position'])
	list_editable = ("active",)
	list_filter = (['active'])
	search_fields = ('title', 'bakhsh')


admin.site.register(Dehestan, DehestanAdmin)

