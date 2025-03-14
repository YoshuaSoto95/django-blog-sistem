from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Tag, Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# Posts ========== #
# =================================================================================================== #
@login_required
def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts.html', context)

@login_required
def create_post(request):
    tags_show = Tag.objects.all()
    categories_show = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('description')
        imagen_main = request.FILES.get('imagen_main')
        content = request.POST.get('content')
        category_id = request.POST.get('category_id')
        tags_id = request.POST.get('tags_id')

        if title and subtitle and description and imagen_main and content and category_id and tags_id:
            categories = Category.objects.get(id=category_id)
            tags = Tag.objects.get(id=tags_id)
            post = Post(
                title=title,
                subtitle=subtitle,
                description=description,
                image_main=imagen_main,
                content=content,
                categories=categories,
                tags=tags,
            )
            post.save()
            messages.success(request, "Post created successfully")
            return redirect('dashboard:posts')
        else:
            messages.error(request, "Invalid request")
            return redirect('dashboard:create_post')
    return render(request, 'create_post.html', {'tags': tags_show, 'categories': categories_show})

@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    category_show = Category.objects.all()
    tags_show = Tag.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        subtitle =  request.POST.get('subtitle')
        description = request.POST.get('description')
        imagen_main = request.FILES.get('imagen_main', None)
        content = request.POST.get('content')
        category_id = request.POST.get('category_id', None)
        tags_id = request.POST.get('tags_id', None)
        
        if title and subtitle and description and content:
            
            post.title = title
            post.subtitle = subtitle
            post.description = description

            if imagen_main:
                post.image_main = imagen_main

            post.content = content

            if category_id:
                categories = Category.objects.get(id=category_id)
                post.categories = categories

            if tags_id:
                tags = Tag.objects.get(id=tags_id)
                post.tags = tags

            post.save()
            messages.success(request, "Post updated successfully")
            return redirect('dashboard:posts')
        else:
            messages.error(request, "Invalid request")
            return redirect('dashboard:posts')
    context = { 'categories': category_show, 'tags': tags_show, 'post': post }
    return render(request, 'update_post.html', context)

@login_required
def delete_post(request, id):
    posts = get_object_or_404(Post, id=id)
    posts.delete()
    messages.success(request, "Post deleted successfully!!!")
    return redirect('dashboard:posts')
    return render(request, 'posts.html')

# =================================================================================================== #
# End Posts ========== #

# Categories ========== #
# =================================================================================================== #
@login_required
def categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'categories.html', context)

@login_required
def create_category(request):
    if request.method == "POST":
        name = request.POST['name']
        if name:
            Category.objects.create(name=name)
            messages.success(request, "Category created successfully")
            return redirect('dashboard:categories')
        else:
            messages.error(request, "Invalid request")
            return redirect('dashboard:categories')
    else:
        messages.error(request, "Invalid request")
        return redirect('dashboard:categories')

@login_required
def update_category(request, id):
    if request.method == "POST":
        name = request.POST['name']

        if name:
            category = Category.objects.get(id=id)
            category.name = name
            category.save()
            messages.success(request, "Category updated successfully")
            return redirect('dashboard:categories')
        else:
            messages.error(request, "Invalid request")
            return redirect('dashboard:categories')
    else:
        messages.error(request, "Invalid request")
        return redirect('dashboard:categories')

@login_required
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, "Category deleted successfully")
    return redirect('dashboard:categories')

# =================================================================================================== #
# End Categories ========== #


# Tags ========== #
# =================================================================================================== #
@login_required
def tags(request):
    tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'tags.html', context)

@login_required
def create_tag(request):
    if request.method == "POST":
        name = request.POST['name']
        if name:
            Tag.objects.create(name=name)
            messages.success(request, "Tag created successfully")
            return redirect('dashboard:tags')
        else:
            messages.error(request, "Invalid request")
            return redirect('dashboard:tags')
    else:
        messages.error(request, "Invalid request")
        return redirect('dashboard:tags')

@login_required
def update_tag(request, id):
    if request.method == "POST":
        name = request.POST['name']
        if name:
            tag = Tag.objects.get(id=id)
            tag.name = name
            tag.save()
            messages.success(request, "Tag updated successfully")
            return redirect('dashboard:tags')
        else:
            messages.error(request, "Invalid request")
            return redirect('dashboard:tags')
    else: 
        messages.error(request, "Invalid request")
        return redirect('dashboard:tags')

@login_required
def delete_tag(request, id):
    tag = get_object_or_404(Tag, id=id)
    tag.delete()
    messages.success(request, "Tag deleted successfully")
    return redirect('dashboard:tags')

# =================================================================================================== #
# End Tags ========== #

# Users ========== #
# =================================================================================================== #
@login_required
def users(request):
    users = User.objects.all()
    context = { 'users': users }
    return render(request, 'users.html', context)

@login_required
def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        is_superuser = request.POST['is_superuser']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            try:
                user = User.objects.create_user(
                    username=username, 
                    is_superuser=is_superuser, 
                    first_name=first_name, 
                    last_name=last_name, 
                    email=email, 
                    password=password1)
                user.save()
                messages.success(request, 'User created successfully')
                return redirect('dashboard:users')
            except:
                messages.error(request, 'User Allready Exists')
                return redirect('dashboard:users')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('dashboard:users')
    return render(request, 'users.html')

@login_required
def update_password(request, id):
    if request.method == "POST":
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.get(id=id)
            user.set_password(password1)
            user.save()
            messages.success(request, "Password updated successfully")
            return redirect('dashboard:users')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('dashboard:users')
    else:
        messages.error(request, "Invalid request")
        return redirect('dashboard:users')
    return render(request, 'users.html')

@login_required
def update_user(request, id):
    users = get_object_or_404(User, id=id)
    if request.method == "POST":
        username = request.POST['username']
        is_superuser = request.POST['is_superuser']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if username and is_superuser and first_name and last_name and email:
            users.username = username
            users.is_superuser = is_superuser
            users.first_name = first_name
            users.last_name = last_name
            users.email = email
            users.save()
            messages.success(request, "User updated successfully")
            return redirect('dashboard:users')
        else:
            messages.error(request, "All fields are required")
            return redirect('dashboard:users')
    else:
        messages.error(request, "Invalid request")
        return redirect('dashboard:users')

@login_required
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success(request, "User deleted successfully")
    return redirect('dashboard:users')

# =================================================================================================== #
# End Users
