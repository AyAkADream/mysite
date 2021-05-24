from django.contrib import admin
from .models import study_Post
from adminsortable.admin import SortableAdmin
# Register your models here.
admin.site.register(study_Post)