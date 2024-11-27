import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EventManagementSystem.settings')

application = get_asgi_application()

from django.contrib.auth import get_user_model

UserModel = get_user_model()

new_user = UserModel.objects