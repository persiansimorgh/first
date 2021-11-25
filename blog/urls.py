from django.urls import path
from . import views
from django.urls import path, include
from django.conf.urls import url
from blog.views import dashboard
from blog.views import dashboard, register
from blog import views as core_views

from blog.views import upload_video,display

from django.conf.urls.static import static
from django.conf import  settings



urlpatterns = [
    url(r"^register/", views.register, name="register"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path("post/listing", core_views.listing, name="listing"),
    path("view_blog/<int:blog_id>/", core_views.view_blog, name="view_blog"),
    path("user_info/", core_views.user_info),
    path("private_place/", core_views.private_place),
    path("accounts/", include("django.contrib.auth.urls")),
    path("staff_place/", core_views.staff_place),
    path('upload/',upload_video,name='upload'),
    path('videos/',display,name='videos'),
    
]
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
