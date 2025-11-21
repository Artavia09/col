from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    ROLES = (
        ("admin", "Administrador"),
        ("teacher", "Profesor"),
        ("student", "Estudiante"),
        ("principal", "Director"),
    )
    role = models.CharField(max_length=20, choices=ROLES, default="student")
    num_telefono = models.CharField(max_length=80, blank=True, null=True)
    num_cedula = models.CharField(max_length=80, blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.role == "admin":
            self.is_staff = True
            self.is_superuser = True
        elif self.role in ("teacher", "principal"):
            self.is_staff = True
            self.is_superuser = False
        else:
            self.is_staff = False
            self.is_superuser = False
        super().save(*args, **kwargs)


class SchoolInfo(models.Model):
    name = models.CharField(max_length=250, default="Escuela Joaquín García Monge")
    mission = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    about = models.TextField(blank=True)
    enrollment_schedule = models.TextField(blank=True)
    contact_phone = models.CharField(max_length=80, blank=True)
    contact_email = models.EmailField(blank=True)
    director_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Sede(models.Model):
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=255, blank=True)
    contacto = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.nombre


class Programa(models.Model):
    NIVEL_CHOICES = (
        ("EGBA", "EGBA"),
        ("EDAD", "EDAD"),
        ("BACH", "Bachillerato"),
        ("ALF", "Alfabetización"),
    )

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Horario(models.Model):
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name="horarios")
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, blank=True)
    dia_semana = models.CharField(max_length=50)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    periodo = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.programa.nombre} {self.dia_semana} {self.hora_inicio}-{self.hora_fin}"


class DocumentoRequisito(models.Model):
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name="requisitos")
    nombre_doc = models.CharField(max_length=160)
    url = models.CharField(max_length=255, blank=True)
    version = models.CharField(max_length=20, blank=True)
    vigente = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.programa.nombre} - {self.nombre_doc}"


class Noticia(models.Model):
    titulo = models.CharField(max_length=160)
    resumen = models.CharField(max_length=260, blank=True)
    contenido = models.TextField(blank=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class ExamDate(models.Model):
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name="exams")
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.date}"


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to="profesores/", blank=True, null=True)
    short_bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class EnrollmentRequest(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=80, blank=True)
    desired_program = models.ForeignKey(Programa, null=True, blank=True, on_delete=models.SET_NULL)
    comments = models.TextField(blank=True)
    pdf_file = models.FileField(
        upload_to="solicitudes/",
        blank=True,
        null=True,
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="pending")

    def __str__(self):
        return f"{self.full_name} ({self.email})"


class Director(models.Model):
    nombre_completo = models.CharField(max_length=200)
    mensaje = models.TextField(blank=True)
    correo = models.EmailField(blank=True)
    telefono = models.CharField(max_length=80, blank=True)
    foto = models.ImageField(upload_to="director/", blank=True, null=True)

    def __str__(self):
        return self.nombre_completo


class TestimonioEstudiante(models.Model):
    nombre_estudiante = models.CharField(max_length=200)
    testimonio = models.TextField()
    anio = models.CharField(max_length=10, blank=True)
    visible = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_estudiante} - {self.anio}"
