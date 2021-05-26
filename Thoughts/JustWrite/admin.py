from django.contrib import admin
from .models import add_blog, user_profile

# Register your models here.
admin.site.register(add_blog)
admin.site.register(user_profile)
