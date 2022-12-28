from django.contrib import admin
from .models import User, Toplist, BurgerPlace

admin.site.register(User)
admin.site.register(Toplist)
admin.site.register(BurgerPlace)
