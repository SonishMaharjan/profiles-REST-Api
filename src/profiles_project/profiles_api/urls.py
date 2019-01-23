from django.conf.urls import url
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hello-veiwset",views.HelloViewSet,base_name="hello-viewset")
#base_name not requird for model viewset
router.register("profile",views.UserProfileViewSet)

urlpatterns =[

    url(r'^hello-view',views.HellooApiView.as_view()),
    url(r'',include(router.urls)),
]
