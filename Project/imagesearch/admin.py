from django.contrib import admin

from .models import *

class PersonAdmin(admin.ModelAdmin):
  list_display = (
    'ID', 'Name', 'Age', 'AddressID', 'Email', 'Phone', 
    'TemplateEncoding', 'IsInvisible'
  )

class AddressAdmin(admin.ModelAdmin):
  list_display = (
    'ID', 'Address1', 'Address2', 'CityID'
  )

class CityAdmin(admin.ModelAdmin):
  list_display = (
    'ID', 'Name', 'State', 'Zip'
  )

class MessageAdmin(admin.ModelAdmin):
  list_display = (
    'ID', 'From', 'To', 'Content'
  )

class PhotoAdmin(admin.ModelAdmin):
  list_display = (
    'ID', 'EventID', 'Filename'
  )

class EventAdmin(admin.ModelAdmin):
  list_display = (
    'ID', 'Name'
  )

class EventAttendedAdmin(admin.ModelAdmin):
  list_display = (
    'PersonID', 'EventID'
  )

class PhotoOfAdmin(admin.ModelAdmin):
  list_display = (
    'PersonID', 'PhotoID'
  )

admin.site.register(Person, PersonAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventAttended, EventAttendedAdmin)
admin.site.register(PhotoOf, PhotoOfAdmin)
