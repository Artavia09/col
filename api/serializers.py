from rest_framework.serializers import ModelSerializer, ValidationError
from .models import (
    SchoolInfo,
    Sede,
    Programa,
    Horario,
    DocumentoRequisito,
    Noticia,
    Teacher,
    EnrollmentRequest,
    ExamDate,
    Director,
    TestimonioEstudiante,
    Usuario,
    PeriodoMatricula,
)


class SchoolInfoSerializer(ModelSerializer):
    class Meta:
        model = SchoolInfo
        fields = "__all__"


class SedeSerializer(ModelSerializer):
    class Meta:
        model = Sede
        fields = "__all__"


class ProgramaSerializer(ModelSerializer):
    class Meta:
        model = Programa
        fields = "__all__"


class HorarioSerializer(ModelSerializer):
    class Meta:
        model = Horario
        fields = "__all__"


class DocumentoRequisitoSerializer(ModelSerializer):
    class Meta:
        model = DocumentoRequisito
        fields = "__all__"


class NoticiaSerializer(ModelSerializer):
    class Meta:
        model = Noticia
        fields = "__all__"


class ExamDateSerializer(ModelSerializer):
    class Meta:
        model = ExamDate
        fields = "__all__"


class PeriodoMatriculaSerializer(ModelSerializer):
    class Meta:
        model = PeriodoMatricula
        fields = "__all__"


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class EnrollmentRequestSerializer(ModelSerializer):
    class Meta:
        model = EnrollmentRequest
        fields = "__all__"


class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"


class TestimonioEstudianteSerializer(ModelSerializer):
    class Meta:
        model = TestimonioEstudiante
        fields = "__all__"


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
            "num_telefono",
            "num_cedula",
            "fecha_nacimiento",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_email(self, value):
        if not value:
            return value
        qs = Usuario.objects.filter(email=value)
        instance = getattr(self, "instance", None)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise ValidationError("Ya existe un usuario con este correo electrónico.")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = Usuario(**validated_data)
        if password is not None:
            user.set_password(password)  # 🔐 contraseña cifrada
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)  # 🔐 al cambiar se vuelve a cifrar
        instance.save()
        return instance
class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
class EnrollmentRequestSerializer(ModelSerializer):
    class Meta:
        model = EnrollmentRequest
        fields = "__all__"
class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"
class TestimonioEstudianteSerializer(ModelSerializer):
    class Meta:
        model = TestimonioEstudiante
        fields = "__all__"
class UsuarioSerializer(ModelSerializer):   
    class Meta:
        model = Usuario
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
            "num_telefono",
            "num_cedula",
            "fecha_nacimiento",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }
    def validate_email(self, value):
        if not value:
            return value
        qs = Usuario.objects.filter(email=value)
        instance = getattr(self, "instance", None)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise ValidationError("Ya existe un usuario con este correo electrónico.")
        return value
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = Usuario(**validated_data)
        if password is not None:
            user.set_password(password)  # 🔐 contraseña cifrada
        user.save()
        return user
    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)  # 🔐 al cambiar se vuelve a cifrar
        instance.save()
        return instance
class LoginSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("username", "password")
    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        if username and password:
            try:
                user = Usuario.objects.get(username=username)
            except Usuario.DoesNotExist:
                raise ValidationError("Credenciales inválidas.")
            if not user.check_password(password):
                raise ValidationError("Credenciales inválidas.")
            data["user"] = user
            return data
        else:
            raise ValidationError("Se requieren ambos campos: username y password.") 
# 🔹 Vista de inicio de sesión (login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Usuario
from .serializers import UsuarioSerializer

class LoginView(APIView):
    """
    Vista de inicio de sesión.
    - Método: POST
    - Body JSON esperado: { "username": "...", "password": "..." }
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # Validar que vengan ambos campos
        if not username or not password:
            return Response(
                {"detail": "Debe enviar 'username' y 'password'."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Autenticar usando el sistema de auth de Django
        user = authenticate(request, username=username, password=password)

        if user is not None:
            token_acceso = RefreshToken.for_user(user).access_token
            #sesiones de Django:
            return Response(
                {
                    "detail": "Inicio de sesión exitoso.",
                    "username": user.username,
                    "id": user.id,
                    "access_token": str(token_acceso),
                },
                status=status.HTTP_200_OK,
            )
        else:
            # Usuario no válido
            return Response(
                {"detail": "Nombre de usuario o contraseña incorrectos."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


            