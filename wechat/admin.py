from django.contrib import admin

# Register your model here.
from wechat.models import User,Topic,Profession

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Profession)
