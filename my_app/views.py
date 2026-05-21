from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .serializers import *


class UpdateProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user

        serializer = UserUpdateSerializer(
            user,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response({
                "user": serializer.data
            }, status=200)

        return Response(serializer.errors, status=400)


class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = request.data

            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            student_class = data.get('student_class')

            if not username or not email or not password:
                return Response(
                    {'message': 'Нужен username, email и пароль'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user_exist = Users.objects.filter(username=username).exists()
            email_exist = Users.objects.filter(email=email).exists()

            if user_exist:
                return Response(
                    {'message': 'Пользователь уже существует'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if email_exist:
                return Response(
                    {'message': 'E-mail уже существует'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # 🔥 ВАЖНО: create_user вместо create
            user = Users.objects.create_user(
                username=username,
                email=email,
                password=password,
                student_class=student_class
            )

            refresh = RefreshToken.for_user(user)

            return Response({
                "message": "Регистрация прошла успешно",
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            print("REGISTER ERROR:", str(e))

            return Response({
                "error": str(e)
            }, status=500)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')

            if not email or not password:
                return Response(
                    {'message': 'Нужен email и пароль'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user = Users.objects.filter(email=email).first()

            if not user:
                return Response(
                    {'message': 'Пользователь не найден'},
                    status=status.HTTP_404_NOT_FOUND
                )

            # 🔥 ПРАВИЛЬНО для AbstractBaseUser
            if not user.check_password(password):
                return Response(
                    {'message': 'Неверный пароль'},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            refresh = RefreshToken.for_user(user)

            return Response({
                "message": "Успешный вход",
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            })

        except Exception as e:
            print("LOGIN ERROR:", str(e))

            return Response({
                "error": str(e)
            }, status=500)


class GetInfoUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user

            serializer = UserSerializer(
                user,
                context={'request': request}
            )

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        except Exception as e:
            print("USER INFO ERROR:", str(e))

            return Response({
                "error": str(e)
            }, status=500)


class GetSchedule(APIView):
    def get(self, request):
        student_class = request.query_params.get('student_class')

        if not student_class:
            return Response(
                {"error": "Не передан student_class"},
                status=status.HTTP_400_BAD_REQUEST
            )

        schedule_student = Schedule.objects.filter(
            class_name=student_class
        ).order_by('start_time')

        serializer = ScheduleSerializer(schedule_student, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

class GetGrades(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        grades_student = Grades.objects.filter(
            student=request.user  # уже правильно
        )

        serializer = GradesSerializer(
            grades_student,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )   


class GetPayment(APIView):
    def get(self, request):
        username = request.query_params.get('username')

        if not username:
            return Response(
                {"error": "Не передан username"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            payment_student = Payment.objects.filter(
                student__username=username
            ).order_by('date_pay')

            serializer = PaymentSerializer(
                payment_student,
                many=True
            )

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print("PAYMENT ERROR:", str(e))
            return Response({"error": str(e)}, status=500)


class GetAttendance(APIView):
    def get(self, request):
        username = request.query_params.get('username')

        if not username:
            return Response(
                {"error": "Не передан username"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            attendance_student = Attendance.objects.filter(
                student__username=username
            ).order_by('date')

            serializer = AttendanceSerializer(
                attendance_student,
                many=True
            )

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print("ATTENDANCE ERROR:", str(e))
            return Response({"error": str(e)}, status=500)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')

            if not refresh_token:
                return Response(
                    {'error': 'Нужен refresh token'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {'success': 'Выход успешен'},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            print("LOGOUT ERROR:", str(e))

            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )