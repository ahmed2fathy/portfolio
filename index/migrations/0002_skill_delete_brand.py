# Generated by Django 4.0.4 on 2022-05-21 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_title', models.CharField(max_length=60, verbose_name='skill')),
                ('skill_percentage', models.IntegerField(verbose_name='skill')),
                ('image', models.ImageField(upload_to='media/index/brands/', verbose_name='image')),
                ('color_bar', models.CharField(choices=[('Maroon', '#800000'), ('LightPurple', '#728FCE'), ('Purple', '#800080'), ('Azure', '#4863A0'), ('Marble', '#566D7E'), ('Lapis', '#15317E'), ('DeepSkyBlue', '#1E90FF'), ('Canary', '#0041C2'), ('BlueGreen', '#7BCCB5'), ('SlateBlue', '#6A5ACD'), ('BlueViolet', '#8A2BE2'), ('Zircon', '#57FEFF')], max_length=60, verbose_name='color')),
            ],
            options={
                'verbose_name_plural': 'Skill',
            },
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
