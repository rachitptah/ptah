from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin
from .models import Workshop
from .models import Venue
from .models import Registration
from .models import Discount

class DiscoutnInline(NestedTabularInline):
	extra = 0
	model = Discount
	


class RegistrationInline(NestedStackedInline):
    model = Registration
    extra = 1
    inlines = [DiscoutnInline]
    

class WorkshopAdmin(NestedModelAdmin):
    inlines = [RegistrationInline]

admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Venue)
admin.site.register(Registration)
admin.site.register(Discount)