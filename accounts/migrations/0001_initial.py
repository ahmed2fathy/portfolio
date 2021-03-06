# Generated by Django 4.0.4 on 2022-06-01 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.EmailField(blank=True, default='User.email', max_length=254, null=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='About')),
                ('skills', models.CharField(blank=True, default='PHP, HTML, CSS, JavaScript, JQuery', max_length=300, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Fmale', 'Fmale')], max_length=40, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('fb_link', models.URLField(blank=True, max_length=400, null=True)),
                ('twitter_link', models.URLField(blank=True, max_length=400, null=True)),
                ('instagram_link', models.URLField(blank=True, max_length=400, null=True)),
                ('user', models.ForeignKey(default='User', on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
