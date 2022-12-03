from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin

from carCollectionApp.core.forms import ProfileForm, CarForm, DeleteCarForm, EditProfileForm, DeleteProfileForm
from carCollectionApp.core.models import Profile, Car
from django.views import generic


# Create your views here.

def get_profile():
    profile = Profile.objects.all()
    return profile


class ShowIndex(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


class CreateProfile(generic.CreateView):
    template_name = 'profile-create.html'
    form_class = ProfileForm
    success_url = reverse_lazy('show index')


class ShowCatalogue(generic.TemplateView):
    @staticmethod
    def get_cars():
        cars = Car.objects.all()
        return cars

    template_name = 'catalogue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = self.get_cars()
        context['total_cars'] = len(self.get_cars())
        return context


class CreateCar(generic.CreateView):
    template_name = 'car-create.html'
    form_class = CarForm
    success_url = reverse_lazy('show catalogue')


class ShowCarDetail(generic.DetailView):
    template_name = 'car-details.html'
    context_object_name = 'car_detail'
    model = Car


class EditCar(generic.UpdateView):
    fields = '__all__'
    model = Car
    template_name = 'car-edit.html'
    success_url = reverse_lazy('show catalogue')


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == "POST":
        car_form = DeleteCarForm(request.POST, request.FILES, instance=car)
        if car_form.is_valid():
            car_form.save()
            return redirect('show catalogue')
    else:
        car_form = DeleteCarForm(instance=car)

    context = {
        'car_form': car_form,
        'car_id': pk
    }
    return render(request, 'car-delete.html', context)


class ShowProfile(generic.TemplateView):
    @staticmethod
    def get_profile():
        profile = Profile.objects.all()[0]
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_profile()
        car_sum = f'{sum([obj.price for obj in Car.objects.all()]):.3f}'
        context['car_sum'] = car_sum
        return context

    template_name = 'profile-details.html'


def edit_profile(request):
    profile = Profile.objects.all()[0]
    if request.method == "POST":
        profile_form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('show profile')
    else:
        profile_form = EditProfileForm(instance=profile)
    context = {
        "profile_form": profile_form
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.all()[0]

    if request.method == "POST":
        profile_form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('show index')
    else:
        profile_form = DeleteProfileForm(instance=profile)
    context = {
        'profile_form': profile_form
    }
    return render(request, 'profile-delete.html', context)
