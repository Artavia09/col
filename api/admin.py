from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Usuario,
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
)


class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ("username", "first_name", "last_name", "email", "role", "is_active")
    list_filter = ("role", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Información personal", {"fields": ("first_name", "last_name", "email", "num_telefono", "num_cedula", "fecha_nacimiento")}),
        ("Rol y estado", {"fields": ("role", "is_active")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "first_name", "last_name", "email", "role", "num_telefono", "num_cedula", "fecha_nacimiento", "is_active"),
        }),
    )
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(SchoolInfo)
admin.site.register(Sede)
admin.site.register(Programa)
admin.site.register(Horario)
admin.site.register(DocumentoRequisito)
admin.site.register(Noticia)
admin.site.register(Teacher)
admin.site.register(EnrollmentRequest)
admin.site.register(ExamDate)
admin.site.register(Director)
admin.site.register(TestimonioEstudiante)
