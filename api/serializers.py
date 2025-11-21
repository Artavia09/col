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
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
