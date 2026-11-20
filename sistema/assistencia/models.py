from django.db import connection, models
 
CHAVE = "chave_assistencia"  # a mesma chave usada no script saep_db.sql
 
 
def criptografar(texto):
    # Pede ao PostgreSQL para criptografar, igual ao INSERT do script
    with connection.cursor() as cursor:
        cursor.execute("SELECT encode(pgp_sym_encrypt(%s, %s), 'hex')", [texto, CHAVE])
        return cursor.fetchone()[0]
 
 
def descriptografar(texto):
    # Pede ao PostgreSQL para abrir o cofre e devolver o CPF original
    with connection.cursor() as cursor:
        cursor.execute("SELECT pgp_sym_decrypt(decode(%s, 'hex'), %s)", [texto, CHAVE])
        return cursor.fetchone()[0]
 
 
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    senha = models.CharField(max_length=255)
 
    class Meta:
        managed = False
        db_table = "usuario"
 
 
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
 
    class Meta:
        managed = False
        db_table = "cliente"
 
    def cpf_aberto(self):
        return descriptografar(self.cpf)
 
    def __str__(self):
        return self.nome
 
 
class Aparelho(models.Model):
    id_aparelho = models.AutoField(primary_key=True)
    imei = models.CharField(max_length=15)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    cor = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, db_column="id_cliente")
 
    class Meta:
        managed = False
        db_table = "aparelho"
 
    def __str__(self):
        return self.imei + " - " + self.modelo
 
 
class Agendamento(models.Model):
    id_agendamento = models.AutoField(primary_key=True)
    data = models.DateField()
    horario = models.TimeField()
    servico = models.CharField(max_length=100)
    aparelho = models.ForeignKey(Aparelho, on_delete=models.PROTECT, db_column="id_aparelho")
 
    class Meta:
        managed = False
        db_table = "agendamento"

Ask AI
