from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px" />'.format(object.photo.url)) #dinh dang avatar

    thumbnail.short_description = 'Photo'
    list_display = ('id','thumbnail', 'first_name', 'designation', 'created_date')  #danh sach nhan vien
    list_display_links = ('id','thumbnail', 'first_name',)                                      #click vao id hoac ten nhan vien se  toi trang ModelAdmin
    search_fields = ('first_name','last_name','designation')                        #tao thanh tim kiem
    list_filter = ('designation',)
admin.site.register(Team, TeamAdmin)
