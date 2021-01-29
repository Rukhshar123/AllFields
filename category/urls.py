
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loadCategory,name="loadCategory"),
    path('addCategory',views.addCategory,name="addCategory"),
    path('showCategory',views.showCategory,name="showCategory"),
    path('subcategory',views.subCategory,name="subcategory"),
    path('showsub',views.showSub,name="showsub"),
    path('editSubcategory/<int:id>',views.editSubcategory,name="subedit"),
    path('updateSubcategory/<int:id>',views.updateSubcategory,name="updateSubcategory"),
    path('deleteSubcategory/<int:id>',views.deleteSubcategory,name="deleteSubcategory"),
    path('product',views.product,name="product"),
    path('showProduct',views.showProduct,name="showProduct"),
    path('editProduct/<int:id>',views.editProduct,name="editProduct"),
    path('updateProduct/<int:id>',views.updateProduct,name="updateProduct"),

]
