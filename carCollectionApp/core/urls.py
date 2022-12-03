from django.urls import path

from carCollectionApp.core.views import ShowIndex, CreateProfile, \
    ShowCatalogue, \
    CreateCar, ShowCarDetail, EditCar, delete_car, ShowProfile, edit_profile, delete_profile

urlpatterns = [
    path('', ShowIndex.as_view(), name='show index'),
    path('profile/create', CreateProfile.as_view(), name='create profile'),
    path('catalogue/', ShowCatalogue.as_view(), name='show catalogue'),
    path('car/create/', CreateCar.as_view(), name='create car'),
    path('car/<int:pk>/details/', ShowCarDetail.as_view(), name='show car details'),
    path('car/<int:pk>/edit/', EditCar.as_view(), name='edit car'),
    path('car/<int:pk>/delete/', delete_car, name='delete car'),
    path('profile/details/', ShowProfile.as_view(), name='show profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile')

]
