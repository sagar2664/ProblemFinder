from django.urls import path
from search.views import ProblemFind

urlpatterns = [
    path('', ProblemFind.as_view(), name='Finding Problem'),
]
