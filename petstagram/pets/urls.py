from django.urls import path

from petstagram.pets.views import PetsListView, CreatePetView, UpdatePetView, DeletePetView, PetDetailsView, \
    LikePetView, CommentPetView  # like_pet, details_or_comment_pet, list_pets, create_pet, edit_pet, delete_pet

urlpatterns = [
    # path('', list_pets, name='list pets'),
    path('', PetsListView.as_view(), name='list pets'),
    # path('detail/<int:pk>/', details_or_comment_pet, name='pet details or comment'),
    path('detail/<int:pk>/', PetDetailsView.as_view(), name='pet details'),
    # path('like/<int:pk>/', like_pet, name='like pet'),
    path('like/<int:pk>/', LikePetView.as_view(), name='like pet'),
    # path('edit/<int:pk>/', edit_pet, name='edit pet'),
    path('edit/<int:pk>/', UpdatePetView.as_view(), name='edit pet'),
    # path('delete/<int:pk>/', delete_pet, name='delete pet'),
    path('delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),
    # path('create/', create_pet, name='create pet'),
    path('create/', CreatePetView.as_view(), name='create pet'),
    path('comment/<int:pk>/', CommentPetView.as_view(), name='comment pet'),
]
