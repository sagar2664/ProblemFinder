from dataQuery.codeforce import searchCodeforce
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

def search(request):
    search_query = request.GET.get('q')
    if search_query is None:
        return HttpResponse("Search the Problems by given value")
    
    ans = searchCodeforce(search_query)

    page = request.GET.get('page', 1)
    per_page = 10
    paginator = Paginator(ans, per_page)
    paginated_data = paginator.get_page(page)

    return render(request, 'search.html', {'ans': paginated_data, 'search_query': search_query})


