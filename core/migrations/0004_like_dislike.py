# Generated by Django 4.2.11 on 2024-05-24 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='core.article')),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='core.comment')),
                ('user', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DisLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='core.article')),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='core.comment')),
                ('user', models.ManyToManyField(related_name='dislikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
