from django.urls import path
from .views import (
    SchoolInfoListCreateView,
    SchoolInfoDetailView,
    SedeListCreateView,
    SedeDetailView,
    ProgramaListCreateView,
    ProgramaDetailView,
    HorarioListCreateView,
    HorarioDetailView,
    DocumentoRequisitoListCreateView,
    DocumentoRequisitoDetailView,
    NoticiaListCreateView,
    NoticiaDetailView,
    TeacherListCreateView,
    TeacherDetailView,
    ExamDateListCreateView,
    ExamDateDetailView,
    EnrollmentRequestListCreateView,
    EnrollmentRequestDetailView,
    DirectorListCreateView,
    DirectorDetailView,
    TestimonioEstudianteListCreateView,
    TestimonioEstudianteDetailView,
    UsuarioListCreateView,
    UsuarioDetailView,
    LoginView,  # 🔹 Import de la vista de login
)

urlpatterns = [
    path("schoolinfo/", SchoolInfoListCreateView.as_view()),
    path("schoolinfo/<int:pk>/", SchoolInfoDetailView.as_view()),

    path("sede/", SedeListCreateView.as_view()),
    path("sede/<int:pk>/", SedeDetailView.as_view()),

    path("programa/", ProgramaListCreateView.as_view()),
    path("programa/<int:pk>/", ProgramaDetailView.as_view()),

    path("horario/", HorarioListCreateView.as_view()),
    path("horario/<int:pk>/", HorarioDetailView.as_view()),

    path("documentorequisito/", DocumentoRequisitoListCreateView.as_view()),
    path("documentorequisito/<int:pk>/", DocumentoRequisitoDetailView.as_view()),

    path("noticia/", NoticiaListCreateView.as_view()),
    path("noticia/<int:pk>/", NoticiaDetailView.as_view()),

    path("teacher/", TeacherListCreateView.as_view()),
    path("teacher/<int:pk>/", TeacherDetailView.as_view()),

    path("examdate/", ExamDateListCreateView.as_view()),
    path("examdate/<int:pk>/", ExamDateDetailView.as_view()),

    path("enrollmentrequest/", EnrollmentRequestListCreateView.as_view()),
    path("enrollmentrequest/<int:pk>/", EnrollmentRequestDetailView.as_view()),

    path("director/", DirectorListCreateView.as_view()),
    path("director/<int:pk>/", DirectorDetailView.as_view()),

    path("testimonios/", TestimonioEstudianteListCreateView.as_view()),
    path("testimonios/<int:pk>/", TestimonioEstudianteDetailView.as_view()),

    path("usuario/", UsuarioListCreateView.as_view()),
    path("usuario/<int:pk>/", UsuarioDetailView.as_view()),

    # 🔹 Endpoint de inicio de sesión (POST con username y password)
    path("login/", LoginView.as_view()),
]
