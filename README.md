# School Diary (Fullstack)

Веб-приложение электронного школьного дневника.

Проект состоит из:
- Frontend (React + Vite)
- Backend (Django REST Framework)


##  Функционал

### Пользователи
- Регистрация и авторизация (JWT)
- Обновление access токена (refresh token)
- Профиль пользователя
- Загрузка аватара

### Учебная система
- Расписание уроков
- Оценки
- Посещаемость

### Финансы
- Просмотр платежей
- Статус оплаты



##  Backend (Django REST API)

### Технологии:
- Django
- Django REST Framework
- SimpleJWT
- Cloudinary
- SQLite / PostgreSQL

### Основные модели:
- Users (кастомная модель пользователя)
- Schedule
- Grades
- Attendance
- Payment
- Subject


##  API endpoints

### Auth
- POST `/api/register/`
- POST `/api/login/`
- POST `/api/token/refresh/`

### User
- GET `/api/user-info/`
- PATCH `/api/user-info/update/`

### Data
- GET `/api/schedule/`
- GET `/api/grades/`
- GET `/api/attendance/`
- GET `/api/payment/`


##  Frontend (React)

### Технологии:
- React
- Vite
- React Router
- Axios

### Функции:
- Авторизация (JWT)
- Protected routes
- Axios interceptors
- Dashboard
- Профиль пользователя
- Расписание
- Оценки
- Посещаемость
- Платежи


##  Архитектура

Frontend → API (Django) -> Database -- 
 ---> Cloudinary (аватарки)


##  Запуск проекта

### Backend
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
