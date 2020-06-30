
from django.contrib import admin
from django.urls import path, include
from ysl import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ysl/', include('ysl.urls')),
    path('ysl/', views.index, name='index'),
    path('ysl/<int:question_id>/', views.detail, name='detail'),
    path('ysl/<int:question_id>/vote', views.vote, name='vote'),
    path('ysl/<int:question_id>/results/', views.results, name='result'),

]
