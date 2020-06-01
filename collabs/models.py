# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    cid = models.OneToOneField('Collaboration', models.DO_NOTHING, db_column='cid', primary_key=True)
    rid = models.ForeignKey('Researcher', models.DO_NOTHING, db_column='rid')
    iid_1 = models.ForeignKey('Institution', models.DO_NOTHING,
                              db_column='iid_1', blank=True, null=True,
                              related_name='iid_1s')
    iid_2 = models.ForeignKey('Institution', models.DO_NOTHING,
                              db_column='iid_2', blank=True, null=True,
                              related_name='iid_2s')
    author_index = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Author'
        unique_together = (('cid', 'rid'),)


class Authors2(models.Model):
    cid = models.OneToOneField('Collaborations2', models.DO_NOTHING, db_column='cid', primary_key=True)
    rid = models.ForeignKey('Researchers2', models.DO_NOTHING, db_column='rid')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Authors2'
        unique_together = (('cid', 'rid'),)


class Collaboration(models.Model):
    cid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=400, blank=True, null=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    venue = models.CharField(max_length=300, blank=True, null=True)
    type = models.CharField(max_length=12, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    citations_count = models.PositiveIntegerField(blank=True, null=True)
    citations_updated_at = models.DateTimeField(blank=True, null=True)
    microsoft_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Collaboration'


class Collaborations2(models.Model):
    cid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    data_source = models.CharField(max_length=100)
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Collaborations2'


class Department(models.Model):
    did = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=50)
    college_name = models.CharField(max_length=50, blank=True, null=True)
    iid = models.ForeignKey('Institution', models.DO_NOTHING, db_column='iid')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Department'


class Education(models.Model):
    edid = models.AutoField(primary_key=True)
    rid = models.ForeignKey('Researcher', models.DO_NOTHING, db_column='rid')
    iid = models.ForeignKey('Institution', models.DO_NOTHING, db_column='iid')
    field = models.CharField(max_length=50)
    level = models.CharField(max_length=10)
    year = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Education'


class Email(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    rid = models.ForeignKey('Researcher', models.DO_NOTHING, db_column='rid')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Email'


class Employment(models.Model):
    emid = models.AutoField(primary_key=True)
    rid = models.ForeignKey('Researcher', models.DO_NOTHING, db_column='rid')
    did = models.ForeignKey(Department, models.DO_NOTHING, db_column='did')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Employment'


class Gender(models.Model):
    rid = models.OneToOneField('Researcher', models.DO_NOTHING, db_column='rid', primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=7)
    accuracy = models.PositiveIntegerField(blank=True, null=True)
    samples = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Gender'


class Institution(models.Model):
    iid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    domain = models.CharField(unique=True, max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    microsoft_id = models.CharField(max_length=20, blank=True, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    lng = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Institution'


class Interest(models.Model):
    rid = models.ForeignKey('Researcher', models.DO_NOTHING, db_column='rid')
    interest = models.CharField(primary_key=True, max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Interest'
        unique_together = (('interest', 'rid'),)


class Researcher(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    name_alt = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    recent_salary = models.FloatField(blank=True, null=True)
    citations_count = models.PositiveIntegerField(blank=True, null=True)
    citations_updated_at = models.DateTimeField(blank=True, null=True)
    scholar_id = models.CharField(max_length=20, blank=True, null=True)
    microsoft_id = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    human_checked = models.DateTimeField(blank=True, null=True)
    human_checked_by = models.CharField(max_length=8, blank=True, null=True)
    note = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Researcher'


class Researchers2(models.Model):
    rid = models.AutoField(primary_key=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    institution = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    ms_id = models.CharField(max_length=20, blank=True, null=True)
    hired_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    cal_poly_position = models.CharField(max_length=50, blank=True, null=True)
    education = models.CharField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    gender_accuracy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Researchers2'
