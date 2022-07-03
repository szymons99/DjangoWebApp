from django.contrib import admin

from .models import Item
from .models import Comment
from .models import Ability
from .models import Champion
from .models import Category
from .models import Property
from .models import Update
from .models import Shop

admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(Ability)
admin.site.register(Champion)
admin.site.register(Category)
admin.site.register(Property)
admin.site.register(Update)
admin.site.register(Shop)
