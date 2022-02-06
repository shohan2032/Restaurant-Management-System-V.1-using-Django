from django.urls import path
from .import views

urlpatterns = [
    path('',views.ownerlogin,name="ownerlogin"),
    path('ownerlogin/',views.ownerlogin,name="ownerlogin"),
    path('ownerlogout/',views.owner_logout,name="owner_logout"),
    
    path('ownerlist/',views.Owner_list,name="Owner_list"),
    path('ownerdetails/<str:owner_id>/',views.Owner_details,name="Owner_details"),
    path('addowner',views.create_owner,name="create_owner"),
    path('editowner/<str:owner_id>/',views.edit_owner,name="edit_owner"),
    path('deleteowner/<str:owner_id>/',views.delete_owner,name="delete_owner"),
    
    path('foodlist/',views.food_list,name="food_list"),
    path('fooddetails/<str:food_id>/',views.food_details,name="food_details"),
    path('editfood/<str:food_id>/',views.edit_food,name="edit_food"),
    path('deletefood/<str:food_id>/',views.delete_food,name="delete_food"),
    path('addfood',views.add_food,name="add_food"),
]