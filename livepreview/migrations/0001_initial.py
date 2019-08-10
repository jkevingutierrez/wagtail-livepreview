# Generated by Django 2.1.11 on 2019-08-10 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LivePreviewRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, verbose_name='created at')),
                ('content_json', models.TextField(verbose_name='content JSON')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='live_preview_updates', to='wagtailcore.Page', verbose_name='page')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'page live preview',
                'verbose_name_plural': 'page live previews',
            },
        ),
    ]