from django.contrib import admin
from website import models
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('email',)
    search_fields = ('message', 'subject')

admin.site.register(models.Contact, ContactAdmin)