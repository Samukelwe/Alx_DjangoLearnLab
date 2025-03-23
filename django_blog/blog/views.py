from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

def register(request):
    form= UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/') 
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    
    return render(request, 'profile.html', {'user': user})




def login_view(request):
    return HttpResponse("Login Page")

def logout_view(request):
    return HttpResponse("Logout Page")


def profile_view(request):
    return HttpResponse("User Profile Page")

def index(request):
    return HttpResponse("Welcome to the homepage")




def profile_management_view(request):
    if request.method == 'POST':
        # Handle form submission to update user information
        # Logic to update user details
        return HttpResponse("Profile updated successfully!")
    else:
        # Retrieve and display user profile information
        # Logic to fetch and display user details
        return HttpResponse("User Profile Page")

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # Create this template
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # Create this template
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_form.html'  # Create this template
    fields = ['title', 'content']  # Include fields for title and content

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_form.html'  # Reuse the post_form template
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'  # Create this template
    success_url = reverse_lazy('post-list')


def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Process the form data
            new_post = form.save(commit=False, author=request.user)
            new_post.save()
            # Redirect or render a success page
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
