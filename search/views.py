from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from search.search import searchProblems

class ProblemFind(APIView):
    def get(self, request):
        return Response("Working!", status=status.HTTP_200_OK)
    
    def post(self, request):
        search = request.data.get('search')
        if search is None:
            return Response("No search query", status=status.HTTP_400_BAD_REQUEST)
        
        noOfProblems = request.data.get('no')
        if noOfProblems is None:
            noOfProblems = 10
        
        ans = searchProblems(search, noOfProblems)

        return Response(ans, status=status.HTTP_200_OK)
