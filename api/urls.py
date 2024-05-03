
from django.urls import path, include
from rest_framework import routers
from .views import UserRegistration, UserLogin, UserProfile, ColumnListCreate, ColumnRetrieveUpdateDestroy, CardListCreate, CardRetrieveUpdateDestroy

router = routers.DefaultRouter()
router.register(r'Add User', UserRegistration, basename='user-registration')
router.register(r'Update Profile', UserProfile, basename='user-profile')
router.register(r'Create Column', ColumnListCreate, basename='column-list-create')
router.register(r'Update Column', ColumnRetrieveUpdateDestroy, basename='column-retrieve-update-destroy')
router.register(r'Add Card', CardListCreate, basename='card-list-create')
router.register(r'card-retrieve-update-destroy', CardRetrieveUpdateDestroy, basename='card-retrieve-update-destroy')

urlpatterns = [
    path('', include(router.urls)),
    path('Login/', UserLogin.as_view(), name='user-login'),
]
