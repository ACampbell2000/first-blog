from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, CV
from .forms import PostForm, CVForm
from django.contrib.auth.decorators import login_required

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request,pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_detail', pk=pk)

@login_required
def post_remove(request,pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	if post.published_date != None:
		return redirect('post_list')
	else:
		return redirect('post_draft_list')

def cv(request):
	cv = CV.objects.all().first()
	if cv is None:
		if request.user.is_authenticated:
			return redirect('create_cv')
		else:
			return redirect('post_list')
	else:
		return render(request, 'blog/cv.html', {'cv': cv})


@login_required
def create_cv(request):
	if request.method == "POST":
		form = CVForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('cv', pk=post.pk)
	else:
		form = CVForm()
	return render(request, 'blog/edit_cv.html', {'form': form})	

@login_required
def edit_cv(request, pk):
	cv = get_object_or_404(CV, pk=pk)
	if request.method == "POST":
		form = CVForm(request.POST, instance=cv)
		if form.is_valid():
			cv = form.save(commit=False)
			cv.author = request.user
			cv.save()
			return redirect('cv', pk=cv.pk)
	else:
		form = CVForm(instance=cv)
	return render(request, 'blog/edit_cv.html', {'form': form})