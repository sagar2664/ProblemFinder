from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dataQuery.views import searchCodeforce
from django.shortcuts import redirect, render

class ProblemFind(APIView):
    def get(self, request):
        search = request.query_params.get('q')
        if search is None:
            return redirect("/api/docs")

        ans = searchCodeforce(search)
        return Response(ans, status=status.HTTP_200_OK)

def documantation(request):
    return render(request, 'docs.html', {})
