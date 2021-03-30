from django.urls import re_path, path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'crud'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='crud/login.html'),
                                                            name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^add/$', views.add, name='add'),
    re_path(r'^delete/$', views.delete, name='delete'),
    #path('<int:pk>/update/', views.MemberUpdate.as_view(), name='update'),
    re_path(r'^edit/(?P<editing_id>\d+)/$', views.edit, name='edit'),
    
]