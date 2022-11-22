# Generated by Django 3.2.14 on 2022-11-15 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cac', '0004_docentem_estudiantem_personam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('nombre_slug', models.SlugField(max_length=100, verbose_name='Nombre Slug')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
                ('url', models.URLField(max_length=100, verbose_name='Url')),
                ('portada', models.ImageField(null=True, upload_to='imagenes/proyecto/', verbose_name='Portada')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cac.estudiantem')),
            ],
        ),
        migrations.DeleteModel(
            name='DocenteABS',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='persona',
        ),
        migrations.DeleteModel(
            name='EstudianteABS',
        ),
        migrations.AddField(
            model_name='curso',
            name='fecha_inicio',
            field=models.DateField(default=None, null=True, verbose_name='Fecha de inicio'),
        ),
        migrations.AddField(
            model_name='curso',
            name='portada',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='Portada'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre Categoria'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descripcion',
            field=models.TextField(null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='estudiantes',
            field=models.ManyToManyField(through='cac.Inscripcion', to='cac.EstudianteM'),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cac.estudiantem'),
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]