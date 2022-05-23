from django.shortcuts import render, redirect

from music_app.web.forms import CreateProfileForm, AddAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from music_app.web.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('profile create')
    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums': albums,
    }
    return render(request, 'home-with-profile.html', context)


def album_add(request):
    profile = get_profile()
    if request.method == 'POST':
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = AddAlbumForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = EditAlbumForm(instance=album)
    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'edit-album.html', context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = DeleteAlbumForm(instance=album)
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'delete-album.html', context)


def profile_create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums': albums,
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        Album.objects.all().delete()
        return redirect('show home')
    else:
        form = DeleteProfileForm()
    context = {
        'form': form,
    }

    return render(request, 'profile-delete.html', context)


