
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView 
from my_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegistrationAPIView.as_view(), name='registration'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('api/user-info/', GetInfoUser.as_view(), name='info'),
    path('api/user-info/update/', UpdateProfileAPIView.as_view(), name='update'),
    path('api/schedule/', GetSchedule.as_view(), name='schedule'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/grades/', GetGrades.as_view(), name='grades'),
    path('api/payment/', GetPayment.as_view(), name='payment'),
    path('api/attendance/', GetAttendance.as_view(), name='attendance'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  