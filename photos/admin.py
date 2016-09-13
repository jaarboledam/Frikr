from django.contrib import admin
from photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_name', 'license', 'visibility')
    list_filter = ('license', 'visibility')
    search_fields = ('name', 'description')

    fieldsets = (
        ('Name and description', {
            'fields': ('name', 'description',)
        }),
        ('Author', {
           'fields': ('owner',)
        }),
        ('URL', {
            'fields': ('url',)
        }),
        ('License and visibility', {
            'fields': ('license', 'visibility',),
            'classes': ('wide', 'collapse',)
        }),
    )

    def owner_name(self, photo):
        return "{0} {1}".format(photo.owner.first_name, photo.owner.last_name)
    owner_name.admin_order_field = 'owner'
    owner_name.short_description = 'Propietario'

admin.site.register(Photo, PhotoAdmin)
