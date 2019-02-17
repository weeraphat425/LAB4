from django.urls import include, path
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path('todo/', include('todo.urls')),
    path('admin/', admin.site.urls),
    path('',  RedirectView.as_view(url='/todo/')),
]