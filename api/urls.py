from django.urls import path
from .views import CategoryList,CreateCategory,CategoryUpdate,CategoryDelete,SignIn,SignUp

urlpatterns = [
    path('list/', CategoryList.as_view()),
    path('create/', CreateCategory.as_view()),
    path('update/<int:pk>', CategoryUpdate.as_view()),
    path('delete/<int:pk>', CategoryDelete.as_view()),
    path('login',SignIn.as_view()),
    path('signup',SignUp.as_view()),
]