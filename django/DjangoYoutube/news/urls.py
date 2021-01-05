from django.urls import include, path, re_path
from django.views.generic import ListView, DetailView
from django import views
from news.models import Articles

urlpatterns = [
   re_path(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by('-date')[:20],template_name='news/posts.html')),
   path('<int:pk>/', DetailView.as_view(model=Articles, template_name="news/post.html")),
   path(r'^<int:pk>/otziv/$', views.testoviy_otziv, name='testoviy_otziv')
]
