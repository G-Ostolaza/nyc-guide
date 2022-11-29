from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
    def get(self, request):
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})


class BoroughView(View):
    def get(self, request, borough):
        return render(
            request=request,
            template_name='borough.html',
            context={'borough': borough, 'activities': boroughs[borough].keys()},
        )


class ActivityView(View):
    def get(self, request, borough, activity):
        return render(
            request=request,
            template_name='activity.html', 
            context={ 'borough': borough,'activity': activity, 'activities': boroughs[borough][activity].keys()}
        )


class VenueView(View): 
    '''View is rendering for borough/activity in urls.py.
    The Borough and Activity arguments are strings taken in from the url.'''
    def get(self, request, borough, activity, venue): 
        venue_text = boroughs[borough][activity][venue].get('description')
        return render(
            request=request,
            template_name='venue.html',
            context={'borough' : borough, 'activity' : activity, 'venue' : venue, 'description': venue_text}
        )
