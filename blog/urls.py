from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^article$', views.article, name='article'),
    url(r'^editArticle$', views.editor, name='edit'),
    url(r'^test', views.test, name='test'),
]