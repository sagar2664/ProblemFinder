from dataQuery.views import searchAll, searchCodeforce, searchLeetcode
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

def search(request):
    query = request.GET.get('q')
    if not query:
        return render(request, 'search.html', {'error': "Please enter a search term."})

    option = request.GET.get('opt')
    if option == 'codeforce':
        ans = searchCodeforce(query)
    elif option == 'leetcode':
        ans = searchLeetcode(query)
    else:
        ans = searchAll(query)

    page = request.GET.get('page', 1)
    per_page = 10
    paginator = Paginator(ans, per_page)
    paginated_data = paginator.get_page(page)

    return render(request, 'search.html', {
        'ans': paginated_data,
        'search_query': query,
        'option': option
    })

