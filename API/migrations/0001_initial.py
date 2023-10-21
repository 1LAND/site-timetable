# Generated by Django 4.2.6 on 2023-10-20 14:52

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
            name='LearningPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Учебное заведение',
                'verbose_name_plural': 'Учебные заведения',
            },
        ),
        migrations.CreateModel(
            name='LearningPlaceClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('learning_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.learningplace')),
            ],
            options={
                'verbose_name': 'Учебное заведение',
                'verbose_name_plural': 'Учебные заведения',
            },
        ),
        migrations.CreateModel(
            name='LearningPlaceTimetableLesson',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('serial_number', models.SmallAutoField(primary_key=True, serialize=False)),
                ('start', models.TimeField(null=True)),
                ('end', models.TimeField(null=True)),
                ('learning_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.learningplace')),
                ('students_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.learningplaceclasses')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.CreateModel(
            name='User',
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
                ('type_user', models.CharField(choices=[('TEA', 'Учитель'), ('STU', 'Ученик'), ('ADM', 'Администратор')], default='STU', max_length=3)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('learning_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API.learningplace')),
                ('user_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API.learningplaceclasses')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='LearningPlacetTimetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('data', models.DateField(auto_now=True)),
                ('learning_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.learningplace')),
                ('lessons', models.ManyToManyField(blank=True, to='API.learningplacetimetablelesson')),
                ('students_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.learningplaceclasses')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписания',
            },
        ),
        migrations.AddField(
            model_name='learningplacetimetablelesson',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='LearningPlaceClassUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('learning_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.learningplace')),
                ('students_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.learningplaceclasses')),
            ],
            options={
                'verbose_name': 'Тип пользователя',
                'verbose_name_plural': 'Типы пользователей',
            },
        ),
        migrations.AddField(
            model_name='learningplaceclasses',
            name='timetable',
            field=models.ManyToManyField(blank=True, to='API.learningplacetimetablelesson'),
        ),
        migrations.AddField(
            model_name='learningplaceclasses',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='learningplace',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='learningplace',
            name='users_classes',
            field=models.ManyToManyField(blank=True, to='API.learningplaceclasses'),
        ),
    ]
