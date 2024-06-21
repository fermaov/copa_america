from django.db import models

class Fase(models.Model):
    cod_fase = models.CharField(primary_key=True, max_length=1)
    nom_fase = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_fase

    class Meta:
        managed = False
        db_table = 'fase'
        ordering = ['cod_fase']

class Equipo(models.Model):
    cod_equipo = models.CharField(primary_key=True, max_length=3)
    nom_equipo = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_equipo

    class Meta:
        managed = False
        db_table = 'equipo'
        ordering = ['nom_equipo']

class Partido(models.Model):
    nro_partido = models.IntegerField(primary_key=True)
    fase = models.ForeignKey('Fase', models.DO_NOTHING, db_column='fase')
    nro_fecha = models.IntegerField()
    fecha = models.DateTimeField()
    equipo1 = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='equipo1', related_name='equipo1',)
    equipo2 = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='equipo2', related_name='equipo2',)
    marcador1 = models.IntegerField(blank=True, null=True)
    marcador2 = models.IntegerField(blank=True, null=True)
    estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado', related_name='estado',)

    def __str__(self):
        return "%s VS %s" % (self.equipo1, self.equipo2)

    class Meta:
        managed = False
        db_table = 'partido'
        ordering = ['nro_partido']
        
class Estado(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    nom_estado = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_estado
    class Meta:
        managed = False
        db_table = 'estado'
        ordering = ['id_estado']
        
class ViewPosiciones(models.Model):
    num = models.BigIntegerField(primary_key=True)
    usuario = models.IntegerField(blank=True, null=True)
    nom_usuario = models.TextField(blank=True, null=True)  
    puntos = models.BigIntegerField(blank=True, null=True)
    puntos_5 = models.BigIntegerField(blank=True, null=True)
    puntos_3 = models.BigIntegerField(blank=True, null=True)
    puntos_0 = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return "%s  %s  %s  %s" % (self.num, self.nom_usuario, self.puntos, self.puntos_5)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_posiciones'

class ViewPartido(models.Model):
    nro_partido = models.IntegerField(primary_key=True)
    nom_fase = models.CharField(max_length=20, blank=True, null=True)
    nro_fecha = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    equipo1 = models.CharField(max_length=20, blank=True, null=True)
    equipo2 = models.CharField(max_length=20, blank=True, null=True)
    marcador1 = models.TextField(blank=True, null=True)
    marcador2 = models.TextField(blank=True, null=True)
    abierto = models.IntegerField(blank=True, null=True)
    nom_estado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_partido'

class ViewMarcador(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.IntegerField(blank=True, null=True)
    nom_usuario = models.TextField(blank=True, null=True)
    nro_partido = models.IntegerField(blank=True, null=True)
    nom_fase = models.CharField(max_length=20, blank=True, null=True)
    nro_fecha = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    equipo1 = models.CharField(max_length=20, blank=True, null=True)
    equipo2 = models.CharField(max_length=20, blank=True, null=True)
    marcador1 = models.TextField(blank=True, null=True)
    marcador2 = models.TextField(blank=True, null=True)
    resultado1 = models.IntegerField(blank=True, null=True)
    resultado2 = models.IntegerField(blank=True, null=True)
    abierto = models.IntegerField(blank=True, null=True)
    fecha_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_marcador'

class ViewCalculo(models.Model):
    usuario = models.IntegerField(blank=True, null=True)
    nom_usuario = models.TextField(blank=True, null=True)  
    nom_fase = models.TextField(blank=True, null=True) 
    nro_partido = models.IntegerField(primary_key=True)
    equipo1 = models.TextField(blank=True, null=True)  
    equipo2 = models.TextField(blank=True, null=True)  
    marcador1 = models.TextField(blank=True, null=True)  
    marcador2 = models.TextField(blank=True, null=True)  
    resultado1 = models.IntegerField(blank=True, null=True)
    resultado2 = models.IntegerField(blank=True, null=True)
    abierto = models.IntegerField(blank=True, null=True)
    dif1 = models.TextField(blank=True, null=True)  
    dif2 = models.TextField(blank=True, null=True)  
    difr = models.TextField(blank=True, null=True)  
    difm = models.TextField(blank=True, null=True)  
    tendencia = models.TextField(blank=True, null=True)  
    goles1 = models.TextField(blank=True, null=True)  
    goles2 = models.TextField(blank=True, null=True)  
    difgol = models.TextField(blank=True, null=True)  
    puntos = models.TextField(blank=True, null=True)  

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_calculo'

class ViewCuadroHonor(models.Model):
    usuario = models.IntegerField(primary_key=True)
    nom_usuario = models.TextField(blank=True, null=True)  
    campeon = models.TextField(blank=True, null=True)  
    nom_campeon = models.TextField(blank=True, null=True)  
    puntos_campeon = models.TextField(blank=True, null=True)  
    subcampeon = models.TextField(blank=True, null=True)  
    nom_subcampeon = models.TextField(blank=True, null=True)  
    puntos_subcampeon = models.TextField(blank=True, null=True)  
    tercero = models.TextField(blank=True, null=True)  
    nom_tercero = models.TextField(blank=True, null=True)  
    puntos_tercero = models.TextField(blank=True, null=True) 
    cuarto = models.TextField(blank=True, null=True)  
    nom_cuarto = models.TextField(blank=True, null=True)  
    puntos_cuarto = models.TextField(blank=True, null=True)  

    class Meta:
        managed = False  
        db_table = 'view_cuadro_honor'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        managed = False
        db_table = 'auth_user'

class Finalistas(models.Model):
    id = models.IntegerField(primary_key=True)
    campeon = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='campeon', related_name='campeon',)
    subcampeon = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='subcampeon', related_name='subcampeon',)
    tercero = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='tercero', related_name='tercero',)
    cuarto = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='cuarto', related_name='cuarto',)

    class Meta:
        managed = False
        db_table = 'finalistas'

class Marcador(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='usuario')
    nro_partido = models.ForeignKey('Partido', models.DO_NOTHING, db_column='nro_partido')
    marcador1 = models.IntegerField(blank=False, null=True)
    marcador2 = models.IntegerField(blank=False, null=True)
    fecha_mod = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s -->> %s" % (self.usuario, self.nro_partido)

    class Meta:
        managed = False
        db_table = 'marcador'
        

class ViewPosicionesPlayOff(models.Model):
    num = models.BigIntegerField(primary_key=True)
    usuario = models.IntegerField(blank=True, null=True)
    nom_usuario = models.TextField(blank=True, null=True)  
    puntos = models.BigIntegerField(blank=True, null=True)
    puntos_5 = models.BigIntegerField(blank=True, null=True)
    puntos_3 = models.BigIntegerField(blank=True, null=True)
    puntos_0 = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return "%s  %s  %s  %s" % (self.num, self.nom_usuario, self.puntos, self.puntos_5)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_posiciones_playoff'