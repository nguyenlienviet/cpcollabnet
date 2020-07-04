# Generated by Django 3.0.6 on 2020-07-04 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collaboration',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=400, null=True)),
                ('year', models.TextField(blank=True, null=True)),
                ('venue', models.CharField(blank=True, max_length=300, null=True)),
                ('type', models.CharField(blank=True, max_length=12, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('citations_count', models.PositiveIntegerField(blank=True, null=True)),
                ('citations_updated_at', models.DateTimeField(blank=True, null=True)),
                ('microsoft_id', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'Collaboration',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Collaborations2',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('year', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('data_source', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Collaborations2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('did', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=50)),
                ('college_name', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('edid', models.AutoField(primary_key=True, serialize=False)),
                ('field', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=10)),
                ('year', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Education',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Email',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('emid', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Employment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('iid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('domain', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('microsoft_id', models.CharField(blank=True, max_length=20, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
            ],
            options={
                'db_table': 'Institution',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('interest', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Interest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('name_alt', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('recent_salary', models.FloatField(blank=True, null=True)),
                ('citations_count', models.PositiveIntegerField(blank=True, null=True)),
                ('citations_updated_at', models.DateTimeField(blank=True, null=True)),
                ('scholar_id', models.CharField(blank=True, max_length=20, null=True)),
                ('microsoft_id', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('human_checked', models.DateTimeField(blank=True, null=True)),
                ('human_checked_by', models.CharField(blank=True, max_length=8, null=True)),
                ('note', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'Researcher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Researchers2',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('institution', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('ms_id', models.CharField(blank=True, max_length=20, null=True)),
                ('hired_year', models.TextField(blank=True, null=True)),
                ('cal_poly_position', models.CharField(blank=True, max_length=50, null=True)),
                ('education', models.CharField(blank=True, max_length=500, null=True)),
                ('gender', models.CharField(blank=True, max_length=15, null=True)),
                ('gender_accuracy', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Researchers2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PubSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=400)),
                ('authors', models.TextField()),
                ('year', models.CharField(max_length=4)),
                ('venue', models.CharField(blank=True, max_length=300, null=True)),
                ('type', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('cid', models.OneToOneField(db_column='cid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='collabs.Collaboration')),
                ('author_index', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Authors2',
            fields=[
                ('cid', models.OneToOneField(db_column='cid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='collabs.Collaborations2')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Authors2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('rid', models.OneToOneField(db_column='rid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='collabs.Researcher')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(max_length=7)),
                ('accuracy', models.PositiveIntegerField(blank=True, null=True)),
                ('samples', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Gender',
                'managed': False,
            },
        ),
    ]
