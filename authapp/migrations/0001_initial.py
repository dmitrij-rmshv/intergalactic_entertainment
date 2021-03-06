# Generated by Django 3.2.8 on 2021-11-17 13:51

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntergalacticUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(blank=True, upload_to='avatars', verbose_name='????????????????')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='??????????????')),
                ('sex', models.CharField(choices=[('male', '??????????????'), ('female', '??????????????'), ('not selected', '???? ????????????')], default='not selected', max_length=12, verbose_name='??????')),
                ('send_messages', models.BooleanField(default=True, verbose_name='?????????????????? ?? ?????????? ????????????????????????')),
                ('send_to_email', models.BooleanField(default=True, verbose_name='?????????????????????? ???? ??????????')),
                ('about_me', models.TextField(blank=True, null=True, verbose_name='?? ????????')),
                ('rating_author', models.FloatField(default=0, verbose_name='?????????????? ????????????')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(db_index=True, default=False, verbose_name='???????????? ??????????????????')),
                ('action', models.TextField(verbose_name='??????????')),
                ('text', models.TextField(blank=True, null=True, verbose_name='??????????')),
                ('target', models.TextField(blank=True, null=True, verbose_name='????????')),
                ('article_id', models.PositiveIntegerField(null=True, verbose_name='ID ????????????')),
                ('comment_id', models.PositiveIntegerField(null=True, verbose_name='ID ??????????????????????')),
                ('like_id', models.PositiveIntegerField(null=True, verbose_name='ID ??????????')),
                ('complaint_id', models.PositiveIntegerField(null=True, verbose_name='ID ????????????')),
                ('add_datetime', models.DateTimeField(auto_now_add=True, verbose_name='?????????? ??????????????????????')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='recipient', to=settings.AUTH_USER_MODEL, verbose_name='????????????????????')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sender', to=settings.AUTH_USER_MODEL, verbose_name='??????????????????????')),
            ],
            options={
                'verbose_name': '??????????????????????',
                'verbose_name_plural': '??????????????????????',
            },
        ),
    ]
