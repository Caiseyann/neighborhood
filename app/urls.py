from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^add/strip$', views.add_strip, name='add_strip'),
    url(r'^join_strip/(\d+)', views.join_strip, name='join_strip'),
    url(r'^leave_strip/(\d+)', views.leave_strip, name='leave_strip'),
    url(r'^add/business$', views.add_business, name='add_business'),
    url(r'^add/post$', views.new_post, name='new_post'),
    url(r'^search_results/', views.search_results, name='search_results'),
    url(r'^user/(?P<username>\w+)', views.user_profile, name='user_profile'),
    url(r'^new/profile$', views.add_profile, name='add_profile'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

                          
