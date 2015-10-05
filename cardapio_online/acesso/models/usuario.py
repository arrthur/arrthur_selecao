from django.contrib.auth.models import User

class Usuario(User):
    
    class Meta():
        app_label = 'acesso'