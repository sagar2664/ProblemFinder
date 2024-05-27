from django.urls import path
from api.views import ProblemFind

urlpatterns = [
    path('', ProblemFind.as_view(), name='Finding Problem'),
]
