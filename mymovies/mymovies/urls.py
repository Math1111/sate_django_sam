#mymovies\urls.py
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static#
from django.contrib.auth import views as auth_views
from movies.views import SignUpView


#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('accounts/', include('django.contrib.auth.urls')),  # Добавьте эту строку
#    path('', include('movies.urls')),
#]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('', include('movies.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)