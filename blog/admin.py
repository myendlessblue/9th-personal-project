from django.contrib import admin

# Register your models here.
from .models import Blog, Comment, HashTag
# *는 all 의 의미로 사용된다 Blog, Comment

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(HashTag)

# admin.site.register(*)로 쓸 수 있음