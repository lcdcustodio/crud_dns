from django.shortcuts import render, redirect, get_object_or_404
from .models import Zone
from .forms import ZoneForm
from .forms import ZoneForm_2
from .support import read_domain

def zone_list(request):
    zones = Zone.objects.all()
    #-----------------
    d_names = [temp.domain_name for temp in zones]
    p_zones = [temp.parent_domain for temp in zones ]
    map_res = read_domain(d_names,p_zones)

    return render(request, 'zone.html', {'zones': zones, 'maps':map_res })


def main(request):

    zones = Zone.objects.all()
    #-----------------
    d_names = [temp.domain_name for temp in zones]
    p_zones = [temp.parent_domain for temp in zones ]

    map_res = read_domain(d_names,p_zones)

    return render(request, 'index.html', {'zones': zones, 'maps':map_res })



def zone_delete(request, id):

    zone =  get_object_or_404(Zone, pk=id)

    if request.method == 'POST':
        zone.delete()
        return redirect('main')

    return render(request, 'zone_delete.html', {'zone': zone})


def create(request):

    form = ZoneForm_2(request.POST or None)

    if form.is_valid():
        #check if new domain is a subdomain
        d_new = form.cleaned_data['domain_name']
        d_list = Zone.objects.all()

        d_new_s = ".".join(d_new.split('.')[1:])
        p_domain = (d_new_s if d_new_s in [zones.domain_name for zones in d_list ] else 'NA')
        p_name_s = 'ns1.' + d_new
        #--------------
        print(d_new)
        print(p_domain)
        print(p_name_s)
        #--------------

        insert_db = Zone.objects.create(domain_name=d_new, primary_name_server=p_name_s,parent_domain=p_domain)
        insert_db.save()

        return redirect('main')

    return render(request, 'new_domain.html', {'form': form})
