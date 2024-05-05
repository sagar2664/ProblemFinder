from dataQuery.codeforce import searchCodeforce
from django.http import HttpResponse

def search(request):
    search = request.GET.get('q')
    if search is None:
        return HttpResponse("Search the Problems by given value")
    
    noOfProblems = request.GET.get('n')
    if noOfProblems is None or noOfProblems.isnumeric() is False:
        noOfProblems = 10

    noOfProblems = int(noOfProblems)
    ans = searchCodeforce(search, noOfProblems)

    return HttpResponse(ans)
