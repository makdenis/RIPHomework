"""lab5 URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from labApp.views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    #url(r'^$', home),url(r'^prodact/$', ProdactsView.as_view(), name='prodacts_url'),
    url(r'^customers/$', CustomerView.as_view(), name='customers_url'),
url(r'^item-(?P<pk>[A-Za-z0-9- ]+)$',
        OneItem.as_view(), name='item_view'),
    url(r'^registration/$', registration, name='registration'),
url(r'^add/$', add, name='add'),
    url(r'^authorization/$', authorization, name='authorization'),
    url(r'^logout/$', logout_view, name='logout'),
url(r'^orders/$', OrdersView.as_view()),
url(r'^$', ItemsView.as_view()),
    # url(r'^success_authorization_form$', success_authorization_form, name='success_authorization_form'),
    url(r'^success_authorization$', success_authorization, name='success_authorization'),
    url(r'^admin/', include(admin.site.urls))
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)