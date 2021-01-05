from django.contrib import admin
from news.models import Articles
# Register your models here.
admin.sites.site.register(Articles)