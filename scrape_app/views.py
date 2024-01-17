from django.shortcuts import render
from .forms import SearchForm
from .scrape import scrape_data
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import csv



def home(request):
    form = SearchForm(request.GET or None)
    if request.method == 'GET' and form.is_valid():
        search_for = form.cleaned_data['search']
        total = form.cleaned_data['total']
        results = scrape_data(search_for, total)
        request.session['results'] = results
        return render(request, 'results.html', {'results': results, 'form': form})
    return render(request, 'home.html', {'form': form})






from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import csv




@csrf_exempt
def download_csv(request):
    if request.method == 'POST':
        
        results = request.session.get('results', [])
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Details.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Address', 'Website', 'Phone Number', 'Reviews Count', 'Reviews Average', 'Latitude', 'Longitude'])

        for result in results:
            writer.writerow([
                result['name'],
                result['address'],
                result['website'],
                result['phone_number'],
                result['reviews_count'],
                result['reviews_average'],
                result['latitude'],
                result['longitude'],
            ])

        return response
    else:
        return HttpResponse("Method not allowed", status=405)



