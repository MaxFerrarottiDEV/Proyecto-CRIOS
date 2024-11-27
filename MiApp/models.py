# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models # type: ignore


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CamposEstudios(models.Model):
    id_campoestudio = models.AutoField(db_column='Id_CampoEstudio', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'campos_estudios'


class Carreras(models.Model):
    id_carrera = models.AutoField(db_column='Id_Carrera', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=200)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'carreras'


class CorrelativasCursar(models.Model):
    id_correlativacursar = models.AutoField(db_column='Id_CorrelativaCursar', primary_key=True)  # Field name made lowercase.
    id_materia_cc = models.ForeignKey('Materias', models.DO_NOTHING, db_column='Id_Materia_CC', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'correlativas_cursar'


class CorrelativasRendir(models.Model):
    id_correlativarendir = models.AutoField(db_column='Id_CorrelativaRendir', primary_key=True)  # Field name made lowercase.
    id_materia_cr = models.ForeignKey('Materias', models.DO_NOTHING, db_column='Id_Materia_CR', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'correlativas_rendir'


class Cuotas(models.Model):
    id_cuota = models.AutoField(db_column='Id_Cuota', primary_key=True)  # Field name made lowercase.
    mes_cuota = models.CharField(db_column='Mes_Cuota', max_length=45)  # Field name made lowercase.
    monto = models.FloatField(db_column='Monto')  # Field name made lowercase.
    fecha_vencimiento = models.DateField(db_column='Fecha_Vencimiento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuotas'


class DatInsc(models.Model):
    id_datinsc = models.AutoField(db_column='Id_DatInsc', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=200)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=200)  # Field name made lowercase.
    fecha_nac = models.DateField(db_column='Fecha_Nac')  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=45)  # Field name made lowercase.
    dni = models.CharField(db_column='DNI',max_length=10)  # Field name made lowercase.
    edad = models.CharField(db_column='Edad', max_length=2)  # Field name made lowercase.
    domicilio = models.CharField(db_column='Domicilio', max_length=200)  # Field name made lowercase.
    telefono_fijo = models.CharField(db_column='Telefono_Fijo', max_length=12, blank=True, null=True)  # Field name made lowercase.
    celular_nro = models.CharField(db_column='Celular_Nro', max_length=12)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=200, blank=True, null=True)  # Field name made lowercase.
    estado_civil = models.CharField(db_column='Estado_Civil', max_length=45)  # Field name made lowercase.
    hijos = models.IntegerField(db_column='Hijos', blank=True, null=True)  # Field name made lowercase.
    lugar_trabajo = models.CharField(db_column='Lugar_Trabajo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tel_emergencia = models.CharField(db_column='Tel_Emergencia', max_length=12)  # Field name made lowercase.
    col_egreso = models.CharField(db_column='Col_Egreso', max_length=200)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=200)  # Field name made lowercase.
    otro_titulo = models.CharField(db_column='Otro_Titulo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    anio_egreso = models.CharField(db_column='Anio_Egreso', max_length=4, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    preg_1 = models.IntegerField(db_column='Preg_1', blank=True, null=True)  # Field name made lowercase.
    resp_1 = models.CharField(db_column='Resp_1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    resp_2 = models.IntegerField(db_column='Resp_2', blank=True, null=True)  # Field name made lowercase.
    preg_2 = models.CharField(db_column='Preg_2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    matricula = models.BooleanField(db_column='Matricula', default=False)  # No permitimos NULL, default es False
    legajo_fisico = models.BooleanField(db_column='Legajo_Fisico', default=False)  # No permitimos NULL, default es False
    inscripto = models.BooleanField(db_column='Inscripto', default=False) # No permitimos NULL, default es False

    class Meta:
        managed = False
        db_table = 'dat_insc'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleados(models.Model):
    id_empleado = models.AutoField(db_column='Id_Empleado', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=200)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=200)  # Field name made lowercase.
    dni = models.BigIntegerField(db_column='DNI')  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=12)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleados'
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class EstadosCuotas(models.Model):
    id_estadocuota = models.AutoField(db_column='Id_EstadoCuota', primary_key=True)  # Field name made lowercase.
    id_pagcuot_ec = models.ForeignKey('PagosCuotas', models.DO_NOTHING, db_column='Id_PagCuot_EC', blank=True, null=True)  # Field name made lowercase.
    vigencia_cuota = models.IntegerField(db_column='Vigencia_Cuota')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estados_cuotas'


class EstadosCurriculares(models.Model):
    id_estadocurricular = models.AutoField(db_column='Id_EstadoCurricular', primary_key=True)  # Field name made lowercase.
    id_matxplan_estcur = models.ForeignKey('MateriasxplanesEstudios', models.DO_NOTHING, db_column='Id_MatXPlan_EstCur', blank=True, null=True)  # Field name made lowercase.
    id_estudiante_estcur = models.ForeignKey('Estudiantes', models.DO_NOTHING, db_column='Id_Estudiante_EstCur', blank=True, null=True)  # Field name made lowercase.
    condicion_nota = models.IntegerField(db_column='Condicion_Nota', blank=True, null=True)  # Field name made lowercase.
    nota = models.IntegerField(db_column='Nota', blank=True, null=True)  # Field name made lowercase.
    fecha_finalizacion = models.DateField(db_column='Fecha_Finalizacion')  # Field name made lowercase.
    folio = models.CharField(db_column='Folio', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estados_curriculares'


class Estudiantes(models.Model):
    id_estudiante = models.AutoField(db_column='Id_Estudiante', primary_key=True)  # Field name made lowercase.
    id_datinsc = models.ForeignKey(DatInsc, models.DO_NOTHING, db_column='Id_DatInsc', blank=True, null=True)  # Field name made lowercase.
    anio_insc = models.SmallIntegerField(db_column='Anio_Insc')  # Field name made lowercase.
    nro_legajo = models.CharField(db_column='Nro_Legajo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    legajo_digital = models.CharField(db_column='Legajo_Digital', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estudiantes'


class InscCarreras(models.Model):
    id_insccarrera = models.AutoField(db_column='Id_InscCarrera', primary_key=True)  # Field name made lowercase.
    id_estudiante_ic = models.ForeignKey(Estudiantes, models.DO_NOTHING, db_column='Id_Estudiante_IC', blank=True, null=True)  # Field name made lowercase.
    id_carrera_ic =  models.ForeignKey(Carreras, models.DO_NOTHING, db_column='Id_Carrera_IC', blank=True, null=True)  # Field name made lowercase.
    fecha_insc = models.DateField(db_column='Fecha_Insc')  # Field name made lowercase.
    id_empleado_ic = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='Id_Empleado_IC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'insc_carreras'


class InscExamenes(models.Model):
    id_inscexamen = models.AutoField(db_column='Id_InscExamen', primary_key=True)  # Field name made lowercase.
    id_estudiante_ie = models.ForeignKey(Estudiantes, models.DO_NOTHING, db_column='Id_Estudiante_IE', blank=True, null=True)  # Field name made lowercase.
    id_mesaexamen = models.ForeignKey('Mesas_Examenes', models.DO_NOTHING, db_column='Id_MatXPlan_IE', blank=True, null=True)  # Field name made lowercase.
    id_estadocuota_ie = models.ForeignKey(EstadosCuotas, models.DO_NOTHING, db_column='Id_EstadoCuota_IE', blank=True, null=True)  # Field name made lowercase.
    id_empleado_ie = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='Id_Empleado_IE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'insc_examenes'


class Materias(models.Model):
    id_materia = models.AutoField(db_column='Id_Materia', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=200)  # Field name made lowercase.
    id_unidad = models.ForeignKey('TiposUnidades', models.DO_NOTHING, db_column='Id_Unidad', blank=True, null=True)  # Field name made lowercase.
    cuatrimestral_anual = models.BooleanField(db_column='Cuatrimestral/Anual', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    correlatividad = models.BooleanField(db_column='Correlatividad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'materias'


class MateriasxplanesEstudios(models.Model):
    id_matxplan = models.AutoField(db_column='Id_MatXPlan', primary_key=True)  # Field name made lowercase.
    id_planestudio = models.ForeignKey('PlanesEstudios', models.DO_NOTHING, db_column='Id_PlanEstudio', blank=True, null=True)  # Field name made lowercase.
    id_materia = models.ForeignKey(Materias, models.DO_NOTHING, db_column='Id_Materia', blank=True, null=True)  # Field name made lowercase.
    id_campoestudio = models.ForeignKey(CamposEstudios, models.DO_NOTHING, db_column='Id_CampoEstudio', blank=True, null=True)  # Field name made lowercase.
    anio_materia = models.SmallIntegerField(db_column='Anio_Materia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'materiasxplanes_estudios'


class Mesas_Examenes(models.Model):
    id_mesaexamen = models.AutoField(db_column='Id_MesaExamen', primary_key=True)
    id_matxplan_me = models.ForeignKey('MateriasxplanesEstudios', models.DO_NOTHING, db_column='Id_MatXPlan_ME', blank=True, null=True)
    fecha_examen = models.DateField(db_column='Fecha_Examen')
    hora_examen = models.TimeField(db_column='Hora_Examen',blank=True, null=True)

class PagosCuotas(models.Model):
    id_pagcuot = models.AutoField(db_column='Id_PagCuot', primary_key=True)  # Field name made lowercase.
    id_cuota_pg = models.ForeignKey(Cuotas, models.DO_NOTHING, db_column='Id_Cuota_PG', blank=True, null=True)  # Field name made lowercase.
    id_estudiante_pg = models.ForeignKey(Estudiantes, models.DO_NOTHING, db_column='Id_Estudiante_PG', blank=True, null=True)  # Field name made lowercase.
    fecha_pago = models.DateField(db_column='Fecha_Pago')  # Field name made lowercase.
    monto = models.FloatField(db_column='Monto')  # Field name made lowercase.
    condicion_pago = models.IntegerField(db_column='Condicion_Pago')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pagos_cuotas'


class PlanesEstudios(models.Model):
    id_planestudio = models.AutoField(db_column='Id_PlanEstudio', primary_key=True)  # Field name made lowercase.
    id_carrera = models.ForeignKey(Carreras, models.DO_NOTHING, db_column='Id_Carrera', blank=True, null=True)  # Field name made lowercase.
    anio_plan = models.PositiveSmallIntegerField(db_column='Anio_Plan')
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planes_estudios'


class TiposUnidades(models.Model):
    id_unidad = models.AutoField(db_column='Id_Unidad', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipos_unidades'
