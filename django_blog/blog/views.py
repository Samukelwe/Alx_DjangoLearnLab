from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Comment
from .forms import CommentForm


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


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_create.html'  # Create a template for comment creation
    success_url = '/'  # Redirect to the homepage after comment creation

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['post_id']  # Assuming you pass post_id through URL
        return super().form_valid(form)
    

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_update.html'  # Create a template for comment update
    success_url = '/'  # Redirect to the homepage after comment update

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
    

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'  # Create a template for comment deletion confirmation
    success_url = reverse_lazy('home')  # Redirect to a specific URL after comment deletion

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


def search_view(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)).distinct()
    else:
        posts = Post.objects.all()
    
    context = {
        'posts': posts,
        'query': query
    }
    return render(request, 'search_results.html', context)

def tag_filter_view(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    posts = Post.objects.filter(tags=tag)
    
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'tag_posts.html', context)


class PostByTagListView(ListView):
    model = Post
    template_name = 'posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        return Post.objects.filter(tags__slug=tag_slug)


