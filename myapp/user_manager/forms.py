from django import forms
from django.contrib.auth.models import User
from user_manager.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields =('profile_pic',)

"""
def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('update_profile_success'))
    else:
        form = UpdateProfile()

    args['form'] = form
    return render(request, 'registration/update_profile.html', args)
"""

class UpdateProfile(forms.ModelForm):
	username = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)

	class Meta:
	    model = User
	    fields = ('username', 'email', 'first_name', 'last_name')

	def clean_email(self):
	    username = self.cleaned_data.get('username')
	    email = self.cleaned_data.get('email')

	    if email and User.objects.filter(email=email).exclude(username=username).count():
	        raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
	    return email

	def save(self, commit=True):
	    user = super(RegistrationForm, self).save(commit=False)
	    user.email = self.cleaned_data['email']

	    if commit:
	        user.save()

	    return user