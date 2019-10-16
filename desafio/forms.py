from django.forms import ModelForm
from .models import Zone
from .models import Records


class ZoneForm_2(ModelForm):

    class Meta:
        model = Zone
        fields = ['domain_name']

class ZoneForm(ModelForm):
    class Meta:
        model = Zone
        #fields = ['domain_name', 'primary_name_server','child_domain','parent_domain']
        fields = ['domain_name', 'primary_name_server','parent_domain']

class Records(ModelForm):
    class Meta:
        model = Records
        fields = ['host_name', 'type', 'content','domain']