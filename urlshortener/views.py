from time import strftime
import random
import string
import json

from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Url
from .service import url_check, categorize_url


def index(request):
    return render(request, 'urlshortener/index.html')


def url(request):
    categories = ['IAB-699', 'IAB-Rm3SiT', 'IAB-avbNf2', 'IAB-XtODT3', 'IAB-I4GWl6', 'IAB-mm3UXx', 'IAB-HxqYV1', 'IAB-j9PaO9', 'IAB-pg0WhF', 'IAB-6i4dB6', 'IAB-8FD8nI', 'IAB-Z7rJBM', 'CUS-3', 'CUS-4', 'CUS-5']
    if request.method == 'POST':
        body = request.body.decode("utf-8")
        url = json.loads(body)
        url = url.get('url')

        category = categorize_url(url)
        #category = 'CUS-5'
        if category != None and category not in categories:

            url = url_check(url)
            random_hash = ''.join(random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
            urls = Url(original_url=url, shorten_url=random_hash,
                    creation_date=strftime("%d/%m/%y"))
            urls.save()
            # the full URL is built on a script in index.html
            response = [{'url': random_hash}]

            return JsonResponse(response, safe=False)
        else:
            response = [{'url': 'ERROR. The page may contain harmfull content'}]
            return JsonResponse(response, safe=False)

def redirect_to_original(request, url):
    try:
        url_return = Url.objects.get(shorten_url=url)
    except:
        return render(request, 'urlshortener/error.html')
    return redirect(url_return.original_url)
