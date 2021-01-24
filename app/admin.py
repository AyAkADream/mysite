from django.contrib import admin
from .models import Profile , Work , Experience , Education , Software , Technical ,Dream, Skill
from adminsortable.admin import SortableAdmin
# Register your models here.

class WorksAdmin(SortableAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Profile)
admin.site.register(Dream)
admin.site.register(Skill)
admin.site.register(Work, WorksAdmin)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Software)
admin.site.register(Technical)
