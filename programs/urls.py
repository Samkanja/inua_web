from django.urls import path
from .views import ( HomePageView,AboutUsViewPage,ActivityDetailView, 
                    ProgramCreateView,Home,ActivityCreateView,
                    AboutUsCreateView,AddPhotoView,GalleryCreateView,GalleryViewPage,addPhoto)

app_name = 'inua'

urlpatterns = [
    path('',HomePageView.as_view(),name='homepage'),
    path('home',Home.as_view(),name='home'),
    path('aboutus/',AboutUsViewPage.as_view(),name='aboutus'),
    path('inua/aboutus/',AboutUsCreateView.as_view(),name='aboutus-create'),
    path('inua/programs/',ProgramCreateView.as_view(),name='programs'),
    path('inua/activity/',ActivityCreateView.as_view(),name='activity-create'),
    path('<uuid:public_id>/activities/',ActivityDetailView.as_view(),name='activity'),
    path('inua/photo/',GalleryCreateView.as_view(),name='create-gallery'),
    path('inua/gallery/',addPhoto, name='gallery-add'),
    path('gallery/',GalleryViewPage.as_view(),name='gallery'),   
]