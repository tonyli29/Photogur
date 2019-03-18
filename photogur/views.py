from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import Picture, Comment
from photogur.forms import LoginForm, PictureForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404




import datetime

def pics(request):
    context = {
        'pictures': Picture.objects.all()
    }
    response = render(request, 'pictures.html', context)
    return HttpResponse(response)

def picture_show(request, id):
    picture = Picture.objects.get(pk=id)
    comments = picture.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save()
            return HttpResponseRedirect('/pictures/{}'.format(id))
        else:
            pass #some error
    else:
        comment_form = CommentForm(initial={'picture': id, 'user': request.user, 'name': 'placeholder'})
    context = {
        'picture': picture,
        'comments': comments,
        'comment_form': comment_form
    }
    response = render(request, 'picture.html', context)
    return HttpResponse(response)

# def project_show(request, id):
#     project = Project.objects.get(pk=id)
#     reward = project.rewards.all()
#     if request.method == 'POST':
#         rewards_form = RewardsForm(request.POST)
#         if rewards_form.is_valid():
#             new_reward = rewards_form.save()
#             return HttpResponseRedirect('/projects/{}'.format(id))
#         else:
#             # put some errors
#             pass
#     else:
#         rewards_form = RewardsForm(initial={'project': id})
#     context = {
#         'project': project,
#         'reward': reward,
#         'rewards_form': rewards_form
#     }
#     response = render(request, 'projectshow.html', context)
#     return HttpResponse(response)


def picture_search(request):
    query = request.GET['query']
    search_result = Picture.objects.filter(artist = query)
    context = {
        'pictures': search_result,
        'query': query
    }
    response = render(request, 'search.html', context)
    return HttpResponse(response)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/pictures/')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    response = render(request, 'login.html', context)
    return HttpResponse(response)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/pictures/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/pictures/')
    else:
        form = UserCreationForm()
    html_response =  render(request, 'signup.html', {'form': form})
    return HttpResponse(html_response) 

@login_required
def new_picture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            new_picture = form.instance
            new_picture.user = request.user
            new_picture.save()
            return HttpResponseRedirect('/pictures/')
    else:
        form = PictureForm()
    html_response =  render(request, 'new_picture.html', {'form': form})
    return HttpResponse(html_response)

def edit_picture(request, id):
    picture = get_object_or_404(Picture, pk=id, user=request.user.pk)
    form = PictureForm(request.POST or None, instance=picture)
    if form.is_valid():
        picture = form.save(commit=False)
        picture.save()
        return HttpResponseRedirect('/pictures/')
    context = {
        'form': form,
        'picture': picture
    }
    return render(request, 'edit.html', context)

def delete_picture(request, id):
    picture = get_object_or_404(Picture, pk=id, user=request.user.pk)
    picture.delete()
    return HttpResponseRedirect('/pictures/')
    
def delete_comment(request, id):
	comment = get_object_or_404(Comment, pk=id, user=request.user.pk)
	comment.delete()
	return HttpResponseRedirect('/pictures/')














#
