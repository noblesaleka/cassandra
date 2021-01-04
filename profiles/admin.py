from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_phone_number',
        'default_email',
        'default_street_address1',
       
    )


admin.site.register(UserProfile, UserProfileAdmin)