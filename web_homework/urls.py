"""web_homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^login', views.login),
                  url(r'^reg', views.reg),
                  url(r'^index/', views.index),
                  url(r'^home/', views.home),
                  url(r'^logout/', views.logout),
                  url(r'^file_share/', views.file_share),
                  url(r'^user/(.*)/', views.user_home),  # user
                  url(r'^user_guanli', views.user_guanli),
                  url(r'^project_gl/', views.project_guanli),
                  url(r'^project_add/', views.project_add),
                  url(r'^project_user_edit/(.*)/', views.project_user_edit),  # todo 3
                  url(r'^project_edit/(.*)/', views.project_edit),     # todo 2
                  url(r'^qndxx', views.qndxx),
                  url(r'^$', views.index),

                  # url(r'', views.wu),             #
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
