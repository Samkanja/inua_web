from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Program,AboutUs,Activity,BoardMember,Gallery,GalleryImage
from django.views.generic  import ListView, CreateView, TemplateView,View
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .forms import ProgramForm,GalleryForm
from django.contrib.auth.decorators import login_required


class Home(TemplateView):
    template_name = 'admin/home.html'

class HomePageView(ListView):
    model = Program
    template_name = 'home.html'
    context_object_name = 'programs'


class ProgramCreateView(CreateView):
    model = Program
    template_name = 'admin/program.html'
    form_class = ProgramForm
    success_url = reverse_lazy('inua:homepage')

    def form_valid(self,form):
        form.instance.admin = self.request.user
        return super().form_valid(form)



class AboutUsViewPage(ListView):
    model = AboutUs
    template_name = 'aboutus.html'
    context_object_name = 'aboutus'

class AboutUsCreateView(CreateView):
    model = AboutUs
    template_name = 'admin/about.html'
    fields  = ['description', 'mission', 'vision']
    success_url = reverse_lazy('inua:aboutus')

    def form_valid(self,form):
        form.instance.admin = self.request.user
        return super().form_valid(form)



class NavBarViewList(ListView):
    model = Program
    template_name = 'navbar.html'
    context_object_name = 'programs'

class BoardMemberView(ListView):
    model = BoardMember
    template_name = 'boardmembers.html'
    context_object_name = 'boardmembers'


class ActivityCreateView(CreateView):
    model =  Activity
    fields = ['title','description','image','program']
    template_name = 'admin/activity.html'
    success_url = reverse_lazy('inua:aboutus')

    def form_valid(self,form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class ActivityDetailView(DetailView):
    model = Program
    template_name = 'detail.html'
    context_object_name = 'program'

    def get_object(self,queryset=None):
        return Program.objects.get_object_by_public_id(public_id=self.kwargs['public_id'])

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        program = self.object
        context['activities'] = program.activity_set.all()
        return context 


class GalleryCreateView(CreateView):
    model = Gallery
    template_name = 'admin/photo.html'
    form_class = GalleryForm
    success_url = reverse_lazy('inua:homepage')

    def form_valid(self,form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
    

@login_required(login_url='login')
def addPhoto(request):
    user = request.user

    galleries = user.gallery_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        
        gallery =Gallery.objects.get(public_id=data['gallery'])
        
           

        for image in images:
            photo = GalleryImage.objects.create(
                gallery=gallery,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'galleries': galleries}
    return render(request, 'admin/add.html', context)



    

class AddPhotoView(LoginRequiredMixin, View):
    login_url = 'login'  # Replace with the URL for your login page
    redirect_field_name = 'next'
    template_name = 'admin/gallery.html'

    def post(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')
        for image in images:
            photo = Gallery.objects.create(image=image,admin=request.user)
        return redirect('inua:aboutus')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class GalleryViewPage(ListView):
    model = Gallery
    template_name = 'gallery.html'
    context_object_name = 'galleries'






