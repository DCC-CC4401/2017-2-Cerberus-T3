from django.contrib.auth.backends import ModelBackend
from .models import UsuarioAdministrador, UsuarioMunicipalidad, UsuarioNormal, UsuarioONG


class UsuariosBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        return self.downcast_user_type(super().authenticate(request, username, password, **kwargs))


    def get_user(self, user_id):
        return self.downcast_user_type(super().get_user(user_id))


    def downcast_user_type(self, user):
        try:
            admin = UsuarioAdministrador.objects.get(pk=user.pk)
            return admin
        except:
            pass

        try:
            muni = UsuarioMunicipalidad.objects.get(pk=user.pk)
            return muni
        except:
            pass

        try:
            normal = UsuarioNormal.objects.get(pk=user.pk)
            return normal
        except:
            pass

        try:
            ong = UsuarioONG.objects.get(pk=user.pk)
            return ong
        except:
            pass

        return user
