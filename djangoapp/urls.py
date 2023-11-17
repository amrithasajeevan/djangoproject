
from django.urls import path
from .views import *
urlpatterns=[
    path('first/',first),
    path('second/',second),
    path('third/',third),
    path('fourth/',fourth),
    path('registration/',registration),
    path('login/',login),
    path('indexpg/',indexpg),
    path('imageup/',image_uploadd),
    path('employeereg/',emp_reg),
    path('empsearch/',emp_search),
    path('productdetail/',product_details),
    path('search/',product_check),
    path('filesupload/',fileup_load),
    path('checking/',select_check),
    path('displayy/',display_fun),
    path('regdetail/',display_reg),
    path('imagedisplay/',image_diaplay),
    path('filedisp/',display_files),
    path('update_pro/<int:id>',update_data),
    path('update_emp/<int:id>',update_emp),
    path('update_file/<int:id>',update_files),
    path('updateimg/<int:id>',image_edit),
    path('delete/<int:id>',delete_reg),
    path('delete_img/<int:id>',delete_img),
    path('delete_file/<int:id>',delete_file),
    path('authuserreg/',userregistration),
    path('authuser/',userresgis),
    path('userlogg/',userr_login),
    path('jsonview/',MyTodos.as_view(),name="jsonviews"),
    path('hotelview/',HotelViews.as_view(),name="hotel")

]