from dataQuery.views import searchAll, searchCodeforce, searchLeetcode
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

def search(request):
    query = request.GET.get('q')
    if query is None:
        return HttpResponse("Search the Problems by given value")
   
    option = request.GET.get('opt')
    if option == '1':
        ans = searchCodeforce(query, 'problem_name')
    elif option == '2':
        ans = searchLeetcode(query, 'problem_code')
    else:
        ans = searchAll(query)

    page = request.GET.get('page', 1)
    per_page = 10
    paginator = Paginator(ans, per_page)
    paginated_data = paginator.get_page(page)

    return render(request, 'search.html', {'ans': paginated_data, 'search_query': query})


