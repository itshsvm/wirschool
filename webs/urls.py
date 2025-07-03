from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),

    # Basic
    path('tutorial/basic/1', views.BasicStepOneView.as_view(), name="basic-one"),
    path('tutorial/basic/2', views.BasicStepTwoView.as_view(), name="basic-two"),
    path('tutorial/basic/3', views.BasicStepThreeView.as_view(), name="basic-three"),


    # Advance
    path('tutorial/advance/1', views.advance_step_one, name="adv-one"),
    path('tutorial/advance/2',views.advance_step_two, name="adv-two"),
    path('tutorial/advance/3',views.advance_step_three, name="adv-three"),




] 