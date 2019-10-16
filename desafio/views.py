from django.shortcuts import render, redirect, get_object_or_404
from .models import Zone
from .forms import ZoneForm
from .forms import ZoneForm_2


def zone_list(request):
    zones = Zone.objects.all()
    return render(request, 'zone.html', {'zones': zones})

def zone_new(request):
    form = ZoneForm(request.POST or None)

    if form.is_valid():

        d_name = form.cleaned_data['domain_name']

        s_zones = Zone.objects.all()
        """
        if form.is_valid():
            name = form.cleaned_data['name']
            number = form.cleaned_data['phone_number']
            p = Person(name=name, phone_number=number, date_subscribed=datetime.now(), messages_received=0)
            p.save()
         """

        if d_name in [zones.domain_name for zones in s_zones ]:
            print(d_name)
            print ([zones.domain_name for zones in s_zones ])



        form.save()
        return redirect('main')

    return render(request, 'zone_new.html', {'form': form})

def main(request):

    return render(request, 'index.html')

def zone_delete(request, id):

    zone =  get_object_or_404(Zone, pk=id)

    if request.method == 'POST':
        zone.delete()
        return redirect('zone_list')

    return render(request, 'zone_delete.html', {'zone': zone})


def create(request):

    form = ZoneForm_2(request.POST or None)

    if form.is_valid():
        #check if new domain is a subdomain

        d_new = form.cleaned_data['domain_name']
        d_list = Zone.objects.all()

        d_new_s = ".".join(d_new.split('.')[1:])
        print(d_new_s)

        if d_new_s in [zones.domain_name for zones in d_list ]:
            print(d_new)
            print ([zones.domain_name for zones in d_list ])


        form.save()
        return redirect('main')

        #return render_to_response('temp.html', message='Save complete');
        #return render_to_response('temp.html');
        #messages.info(request, 'Your password has been changed successfully!')
        #return render_to_response('temp.html')

    return render(request, 'new_domain.html', {'form': form})
