from django.contrib import admin
from django.urls import path,include
from Calculator.views import calculator_view

urlpatterns = [
    path("",calculator_view),
]

#class-based view

from Calculator.views_2 import (
    # Test purpose
    CalculatorView,

    # Exact CRUD views
    CalculatorCreateView,
    CalculatorReadView,
    CalculatorUpdateView,
    CalculatorDeleteView

    )

urlpatterns+=[
    path("",include(
        [
            path("test/",CalculatorView.as_view()),

            # 
            path("list/",CalculatorReadView.as_view(),name="calc_list"),
            path("create/",CalculatorCreateView.as_view(),name="calc_create"),
            path("update/<str:pk>",CalculatorUpdateView.as_view(),name="calc_update"),
            path("delete/<str:pk>",CalculatorDeleteView.as_view(),name="calc_delete"),
        ]
    )
    )
]