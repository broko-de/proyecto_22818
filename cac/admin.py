from django.contrib import admin
from cac.models import EstudianteM, Proyecto, CursoM, Categoria, Curso, Inscripcion

from django.contrib.auth.models import User,Group

class CacAdminSite(admin.AdminSite):
    site_header = 'Administracion Codo a Codo'
    site_title = 'Administracion superusuario'
    index_title = 'Inicio de administración'
    empty_value_display = 'No hay datos para visualizar'

# Register your models here.
#admin.site.register(Proyecto)

class EstudianteMAdmin(admin.ModelAdmin):
    list_display = ('dni_m','nombre_m', 'apellido_m')
    list_editable= ('nombre_m',)
    search_fields = ['apellido_m', 'nombre_m']
    list_filter = ('dni_m','apellido_m' )

#admin.site.register(EstudianteM,EstudianteMAdmin)

class CursoMAdmin(admin.ModelAdmin):
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'categoria':
            kwargs['queryset'] = Categoria.objects.filter(baja=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'estudiantes':
            kwargs['queryset'] = EstudianteM.objects.filter(matricula_m__startswith='LM')
        return super().formfield_for_manytomany(db_field, request, **kwargs)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','baja')
    list_filter = ('baja',)

    def get_queryset(self, request):
        query = super(CategoriaAdmin,self).get_queryset(request)
        filtered_query = query.filter(baja=False)
        return filtered_query

mi_admin = CacAdminSite(name='cacadmin')
mi_admin.register(Proyecto)
mi_admin.register(EstudianteM,EstudianteMAdmin)
mi_admin.register(CursoM,CursoMAdmin)
mi_admin.register(Curso)
mi_admin.register(Inscripcion)
mi_admin.register(Categoria,CategoriaAdmin)


# mi_admin.register(User)
# mi_admin.register(Group)

