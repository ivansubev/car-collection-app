from django import forms

from carCollectionApp.core.models import Profile, Car


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class EditProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class DeleteCarForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(attrs={'readonly': 'readonly'}),
            'model': forms.TextInput(attrs={'readonly': 'readonly'}),
            'year': forms.TextInput(attrs={'readonly': 'readonly'}),
            'image_url': forms.TextInput(attrs={'readonly': 'readonly'}),
            'price': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        cars = Car.objects.all()
        cars.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = []
