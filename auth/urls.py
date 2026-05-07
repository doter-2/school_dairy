
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView 
from my_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegistrationAPIView.as_view()),
    path('api/login/', LoginAPIView.as_view()),
    path('api/user-info/', GetInfoUser.as_view()),
    path('api/user-info/update/', UpdateProfileAPIView.as_view()),
    path('api/schedule/', GetSchedule.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/grades/', GetGrades.as_view()),
    path('api/payment/', GetPayment.as_view()),
    path('api/attendance/', GetAttendance.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
