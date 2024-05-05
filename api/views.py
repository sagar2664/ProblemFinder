from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dataQuery.codeforce import searchCodeforce

class ProblemFind(APIView):
    def get(self, request):
        search = request.query_params.get('q')
        if search is None:
            return Response("Search the Problems by given value", status=status.HTTP_200_OK)

        noOfProblems = request.query_params.get('n')
        if noOfProblems is None or noOfProblems.isnumeric() is False:
            noOfProblems = 10

        noOfProblems = int(noOfProblems)
        ans = searchCodeforce(search, noOfProblems)
        return Response(ans, status=status.HTTP_200_OK)
