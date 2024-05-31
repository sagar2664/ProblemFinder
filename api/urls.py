from django.urls import path
from api.views import ProblemFind, documantation

urlpatterns = [
    path('', ProblemFind.as_view(), name='Finding Problem'),
    path('docs', documantation, name='Documentation of API'),
]
