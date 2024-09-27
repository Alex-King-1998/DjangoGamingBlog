from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.utils import timezone
from .forms import ContactForm
from blog.models import Post, Comment, Game
from blog.forms import CommentForm
from .models import Game
from .forms import GameForm

def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)  # Handle file upload
        if form.is_valid():
            form.save()
            return redirect('games_list')  # Redirect to your games list view
    else:
        form = GameForm()
    return render(request, 'add_game.html', {'form': form})

def game_detail(request, game_name):
    game = get_object_or_404(Game, title=game_name)
    
    # Check if the release date is None or in the future
    if game.release_date is None:
        release_info = "Not Yet Released"
    elif game.release_date > timezone.now().date():
        release_info = "Not Yet Released"
    else:
        release_info = game.release_date.strftime("%B %d, %Y")  # Format the date
    
    context = {
        'game': game,
        'release_info': release_info,  # Make sure release_info is passed to the template
    }
    return render(request, 'game_detail.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email
            send_mail(
                f'Message from {name}',
                message,
                email,
                ['alexkingaus99@gmail.com'],  # The email you want the form data sent to
                fail_silently=False,
            )

            return render(request, 'blog/contact_success.html')  # Redirect or show success page
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }

    return render(request, "blog/detail.html", context)

def games_list(request):
    # Logic for retrieving games could go here
    return render(request, 'blog/games_list.html')