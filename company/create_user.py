from django.contrib.auth.models import User
user = User.objects.create_user(username='admin',
                                 email='jobyalungal@gmail.com',
                                 password='admin')
