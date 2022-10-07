from django.contrib import admin
from django.utils.html import format_html

from bbsadmin.models.UserModel import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    用户admin
    """
    search_fields = ['username', 'name']
    list_display = ['head_image_display', 'username', 'name', 'sex', 'login_at', 'disable', 'create_at', 'update_at']
    list_display_links = ['username']
    list_filter = ['sex', 'disable']
    date_hierarchy = 'create_at'

    def head_image_display(self, obj):
        """头像展示"""
        html = f'<img src="{obj.head_image}" style="width: 50px">' if obj.head_image else '-'
        return format_html(html)

    head_image_display.short_description = '头像'
