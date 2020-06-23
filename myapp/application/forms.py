from django import forms
from application.models import config

"""
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['report_id_application','name_of_application', 'url_of_application', 'ip_of_application', 'description', 'type']

class ApplicationDiscoveryForm(forms.ModelForm):
    class Meta:
        model = ApplicationDiscovery
        fields = ['application_id','imgApplicationDiscovery','description']
    def __init__(self, *args, **kwargs):
        super(ApplicationDiscoveryForm, self).__init__(*args, **kwargs)
        self.fields['imgApplicationDiscovery'].required = False
"""
class ConfigForm(forms.ModelForm):
    class Meta:
        model = config
        fields = ['keywords','everyday', 'everyweek', 'everymonth']