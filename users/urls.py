from users.apps import UsersConfig
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDeleteAPIView

app_name = UsersConfig.name

urlpatterns = [
                  path('token/', TokenObtainPairView.as_view(),
                       name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(),
                       name='token_refresh'),

                  path('user/create/', UserCreateAPIView.as_view(),
                       name='creating user'),

                  path('user/list/', UserListAPIView.as_view(),
                       name='list of users'),

                  path('user/retrieve/<int:pk>/', UserRetrieveAPIView.as_view(),
                       name='list one user'),

                  path('user/update/<int:pk>/', UserUpdateAPIView.as_view(),
                       name='Updating of user'),

                  path('user/delete/<int:pk>/', UserDeleteAPIView.as_view(),
                       name='Deleting of user'),
              ]
