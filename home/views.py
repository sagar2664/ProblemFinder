from django.http import HttpResponse
from django.template import loader
from datetime import datetime

def home(request):
    template = loader.get_template('home.html')
    timestamp = datetime.now().timestamp()
    context = {'timestamp': timestamp}
    return HttpResponse(template.render(context, request))
