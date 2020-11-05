# Generated by Django 3.1.2 on 2020-11-04 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnboardApp', '0003_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('estrellas', models.IntegerField(choices=[[0, '1 estrellas'], [1, '2 estrellas'], [2, '3 estrellas'], [3, '4 estrellas'], [4, '5 estrellas']])),
            ],
        ),
        migrations.AlterField(
            model_name='contacto',
            name='avisos',
            field=models.BooleanField(verbose_name='¿Desea recibir promociones/avisos a su email?'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='tipo_consulta',
            field=models.IntegerField(choices=[[0, 'Consulta'], [1, 'Reclamo'], [2, 'Sugerencia'], [3, 'Felicitaciones']], verbose_name='Motivo contacto'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='imagen',
            field=models.ImageField(null=True, upload_to='lugares'),
        ),
    ]
