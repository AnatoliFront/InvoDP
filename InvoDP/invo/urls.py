from rest_framework import routers
from .api import RequestViewSet


router = routers.DefaultRouter()
router.register('api/invo', RequestViewSet, 'invo')

urlpatterns = router.urls
