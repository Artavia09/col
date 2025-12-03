from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login

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
from .serializers import (
    SchoolInfoSerializer,
    SedeSerializer,
    ProgramaSerializer,
    HorarioSerializer,
    DocumentoRequisitoSerializer,
    NoticiaSerializer,
    TeacherSerializer,
    EnrollmentRequestSerializer,
    ExamDateSerializer,
    DirectorSerializer,
    TestimonioEstudianteSerializer,
    UsuarioSerializer,
)


class SchoolInfoListCreateView(ListCreateAPIView):
    queryset = SchoolInfo.objects.all()
    serializer_class = SchoolInfoSerializer


class SchoolInfoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = SchoolInfo.objects.all()
    serializer_class = SchoolInfoSerializer


class SedeListCreateView(ListCreateAPIView):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer


class SedeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer


class ProgramaListCreateView(ListCreateAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer


class ProgramaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer


class HorarioListCreateView(ListCreateAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer


class HorarioDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer


class DocumentoRequisitoListCreateView(ListCreateAPIView):
    queryset = DocumentoRequisito.objects.all()
    serializer_class = DocumentoRequisitoSerializer


class DocumentoRequisitoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = DocumentoRequisito.objects.all()
    serializer_class = DocumentoRequisitoSerializer


class NoticiaListCreateView(ListCreateAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer


class NoticiaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer


class ExamDateListCreateView(ListCreateAPIView):
    queryset = ExamDate.objects.all()
    serializer_class = ExamDateSerializer


class ExamDateDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ExamDate.objects.all()
    serializer_class = ExamDateSerializer


class TeacherListCreateView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class EnrollmentRequestListCreateView(ListCreateAPIView):
    queryset = EnrollmentRequest.objects.all().order_by("-submitted_at")
    serializer_class = EnrollmentRequestSerializer

    def get_permissions(self):
        if self.request.method.lower() == "post":
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


class EnrollmentRequestDetailView(RetrieveUpdateDestroyAPIView):
    queryset = EnrollmentRequest.objects.all().order_by("-submitted_at")
    serializer_class = EnrollmentRequestSerializer
    permission_classes = [permissions.IsAdminUser]


class DirectorListCreateView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class TestimonioEstudianteListCreateView(ListCreateAPIView):
    queryset = TestimonioEstudiante.objects.all().order_by("-creado_en")
    serializer_class = TestimonioEstudianteSerializer


class TestimonioEstudianteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = TestimonioEstudiante.objects.all().order_by("-creado_en")
    serializer_class = TestimonioEstudianteSerializer


class UsuarioListCreateView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]


class UsuarioDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAdminUser]


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
            #sesiones de Django:
            return Response(
                {
                    "detail": "Inicio de sesión exitoso.",
                    "username": user.username,
                    "id": user.id,
                },
                status=status.HTTP_200_OK,
            )
        else:
            # Usuario no válido
            return Response(
                {"detail": "Nombre de usuario o contraseña incorrectos."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
