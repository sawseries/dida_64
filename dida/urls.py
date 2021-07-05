from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView 

from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts
from django.contrib.auth.views import LoginView, LogoutView

from crudapp import views as crudapp

urlpatterns = [
    path('', crudapp.show),
    path('show/',crudapp.show,name='show'),  
    path('admin/', admin.site.urls),
    path('citizen/edit/<int:pk>/', crudapp.edit, name='edit'),
    path('citizen/create/', crudapp.create, name='create'),
    path('citizen/detail/<int:id>/', crudapp.detail, name='detail'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('citizen/search/', crudapp.search, name='search')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)