from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from . views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('game/', game, name='game'),
    path('game/detail/<str:id>', Detail_berita, name='detail_berita'),
    path('login/', login, name='login'),
    path('logout/', logout_views, name='logout'),
    path('ng/', include('blog.urls')),
    path('ngame/', ngame, name='ngame'),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)