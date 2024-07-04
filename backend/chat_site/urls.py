from django.contrib import admin
from django.urls import path, include
from chat_site import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_auth.urls')),
    path('permission/', include('permissions.urls')),
    path('restaurent/', include('restaurent.urls')),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 