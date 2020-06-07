from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('ID', 'nickName', 'name', 'surname', 'email',)



admin.site.register(Person, PersonAdmin)
