from django.contrib import admin
from django.urls import path
from main_app.views import EventListView, EventDetailView, EventCreateView, user_profile, EventModifyView, \
    EventDeleteView, ModifyProfileView, ChangePasswordView, DeleteProfileView, index, login_user, logout_user, user_registration

urlpatterns = [
    # Path for admin page
    path('admin/', admin.site.urls),

    # Paths for homepage and page with events
    path('', index, name='index'),
    path('homepage/', EventListView.as_view(), name='event-list'),

    # Paths for event
    path('event/new/', EventCreateView, name='event-create'),
    path('event/<int:event_id>/', EventDetailView.as_view(), name='event-detail'),
    path('event/<int:event_id>/modify/', EventModifyView, name='event-modify'),
    path('event/<int:event_id>/delete/', EventDeleteView, name='event-delete'),

    # Paths for profile
    path('profile/', user_profile, name='user-profile'),
    path('profile/modify/', ModifyProfileView, name='modify-profile'),
    path('profile/change-password/', ChangePasswordView, name='change-password'),
    path('profile/delete-profile/', DeleteProfileView, name='delete-profile'),

    # Paths for login and logout
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', user_registration, name='register')
]