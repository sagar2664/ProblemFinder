from dataQuery.codeforce import searchCodeforce
from django.http import HttpResponse
from django.shortcuts import render

def search(request):
    search = request.GET.get('q')
    if search is None:
        return HttpResponse("Search the Problems by given value")

    noOfProblems = request.GET.get('n')
    if noOfProblems is None or not noOfProblems.isnumeric():
        noOfProblems = 10

    noOfProblems = int(noOfProblems)
    ans = searchCodeforce(search, noOfProblems)

    return render(request, 'search.html', {'ans': ans})

