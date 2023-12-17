from django.shortcuts import render, redirect
from . import forms
from . import models
from django.views.generic import DetailView
from django.contrib import messages


# Create your views here.




class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'carid'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()

        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
    




def buy_now(request, carid):
    car = models.Car.objects.get(pk = carid)
    
    if request.method == 'GET':
        if car.quantity != 0:
            profile_car = models.ProfileCar.objects.filter(carid = car.carid, name = car.name, author = request.user)
            if profile_car:
                # for i in profile_car:
                #     if i.carid == car.carid and i.author == request.user:
                s = models.ProfileCar.objects.get(carid = car.carid, name = car.name, author=request.user)
                car.quantity = car.quantity-1
                s.quantity = s.quantity + 1
                car.save()
                s.save()
                return redirect('car_details',carid=car.carid)
                    
            
            else:
                x = models.ProfileCar()
                x.carid = car.carid
                x.name = car.name
                x.price = car.price
                x.quantity = 1
                x.description = car.description
                x.brand = car.brand
                x.author = request.user
                x.image = car.image
                car.quantity = car.quantity - 1
                x.save()
                car.save()
                return redirect('car_details',carid=car.carid)
        else:
            messages.warning(request, 'Out of Stock!!')
            return redirect('car_details',carid=car.carid)


    return render(request, 'car_details.html', {'car' : car})
