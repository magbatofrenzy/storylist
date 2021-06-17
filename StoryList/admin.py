from django.contrib import admin
from .models import Reader, Category, Stories, List, Remarks

admin.site.register(Reader)
admin.site.register(Category)
admin.site.register(Stories)
admin.site.register(List)
admin.site.register(Remarks)
# Register your models here.
