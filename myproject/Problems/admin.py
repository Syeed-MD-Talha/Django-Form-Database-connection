from django.contrib import admin
from .models import online_judge
# Register your models here.

class online_judgeAdmin(admin.ModelAdmin):
    list_display=('id','judge_name','total_problem','handle_name')
    ordering=('id',)
    

admin.site.register(online_judge,online_judgeAdmin)