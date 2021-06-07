from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from account.models import User


class UserAdmin(UserAdmin):
    fieldsets = (
        ("اطلاعات کاربری", {'fields': ('username', 'password', 'pass_per_save')}),
        ("اطلاعات مکانی", {'fields': ('ostan', 'shahrestan', 'bakhsh', 'dehestan')}),
        ("سطوح دسترسی", {'fields': ('ozv_faal', 'moshaver', 'naeb_moodir', 'dabir', 'modir', 'kode_moarefy')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'gender', 'meli_code', 'shenasname_code', 'birthday', 'moaref', 'email', 'image')}),
        ("اطلاعات ثبت نام", {'fields': ('custom_user_id', 'code_send', 'resend_time', 'email_sended', 'phone_number')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ("pass_per_save",)
    add_fieldsets = (
        ("اطلاعات کاربری", {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    # form = UserChangeForm
    # add_form = UserCreationForm
    # change_password_form = AdminPasswordChangeForm
    list_display = ('username', 'phone_number', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser',)
    list_display_links = ('username', 'phone_number')
    list_filter = ('is_staff', 'is_superuser', 'is_active',)
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
		
admin.site.register(User, UserAdmin)
