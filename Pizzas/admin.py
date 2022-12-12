from django.contrib import admin

# Register your models here.
from .models import Pizza, Topping, Profile, Comment, MyImages

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(MyImages)
