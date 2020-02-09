from django.contrib import admin
from .models import GamePurchase, GameData

# Register your models here.
admin.site.register(GamePurchase)
admin.site.register(GameData)