from django.conf.urls import url, include
from django.views.generic import RedirectView
from .views import upload
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/docs')),
    url(r'^upload/', upload),
    url(r'^docs/', include('rest_framework_swagger.urls', namespace='docs')),
]
