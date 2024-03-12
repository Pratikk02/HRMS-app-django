from .views import *
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', login, name = 'login'),
    path('check/', check, name = 'check'),
    path('register/', register, name = 'register'),
    path('create_new/', create_new, name = 'create_new'),
    path('home/', home, name = 'home'),
    path('logout/', logout, name = 'logout'),
    path('emp_detail/', emp_detail, name = 'emp_detail'),
    path('leave/', leave, name = 'leave'),
    path('ileave/', ileave, name = 'ileave'),
    path('issue/', issue, name = 'issue'),
    path('master_list/', master_list, name = 'master_list'),
    path('change_pass/', change_pass, name = 'change_pass'),
    path('change/', change, name = 'change'),
    path('upload/', upload, name = 'upload'),
    path('fupload/', fupload, name = 'fupload'),
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)