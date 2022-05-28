from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('',Home,name='home'),
    path('checkKyc/<str:walletAddresss>/',isKycVerified_1,name='checkKyc'),
    path('uploadKyc/<str:walletAddress>/',kycFileUploadDone,name='kycFileUploadDone'),
    path('userpage/<str:walletAddress>/',UserPage,name='userpage')
    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)