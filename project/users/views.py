from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, ReviewForm, ProfileForm
from schools_site.models import Schools
from .models import Reviews, Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def add_review(request, url):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid() and request.user:
            review = form.save(commit=False)
            review.user = request.user
            review.school = get_object_or_404(Schools, web_site=f"{url}.mskobr.ru")
            review.save()
            return redirect(f'/{url}/')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})


def profile(request):
    if request.method == "POST":
        if "role" in request.POST and "school" in request.POST:
            form = ProfileForm()
            user_profile = Profile.objects.filter(user_id=request.user.id)
            if not user_profile:
                user_profile = form.save(commit=False)
                user_profile.user_id = request.user.id
            else:
                user_profile = user_profile[0]
            user_profile.role = request.POST.get("role")
            user_profile.school_id = request.POST.get("school")
            user_profile.save()
            return redirect("/")
        else:
            form = ProfileForm()
    else:
        user_profile = Profile.objects.filter(user_id=request.user.id)
        if user_profile:
            form = ProfileForm(initial={'role': user_profile[0].role, 'school_id': user_profile[0].school_id})
        else:
            form = ProfileForm(initial={'role': 'parent', 'school_id': 1})
    return render(request, 'profile.html', {"role": form["role"].value(), "school_id": int(form["school_id"].value()),
                                            "schools": Schools.schools_list.order_by("id")})