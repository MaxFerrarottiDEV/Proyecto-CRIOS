from django.core.management.base import BaseCommand
import firebase_admin
from firebase_admin import credentials, db
import mysql.connector
from mysql.connector import errorcode

class Command(BaseCommand):
    help = 'Sincroniza los datos de Firebase a MySQL'

    def handle(self, *args, **kwargs):
        # Inicializar Firebase
        cred = credentials.Certificate('./static/Firebase/credenciales.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://crios-db-proyecto-default-rtdb.firebaseio.com'
        })

        # Configurar conexión a MySQL
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='juan1234',
                database='criosdb'
            )
            cursor = connection.cursor()
            print('Conexión a MySQL exitosa')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de usuario o contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe")
            else:
                print(err)

        # Sincronizar Firebase con MySQL
        try:
            ref = db.reference('inscripcion')
            data = ref.get()

            if not data:
                print('No hay datos para sincronizar')
                return

            for key, inscripcion in data.items():
                # Validar datos
                if not all([inscripcion.get('nombre'), inscripcion.get('apellido'), inscripcion.get('dni')]):
                    print(f'Datos faltantes para inscripción: {key}')
                    continue

                # Transformar valores
                hijos = 1 if inscripcion.get('hijos') == 'Si' else (0 if inscripcion.get('hijos') == 'No' else None)
                ingreso = 1 if inscripcion.get('ingreso') == 'Si' else (0 if inscripcion.get('ingreso') == 'No' else None)
                beneficiario = 1 if inscripcion.get('beneficiario') == 'Si' else (0 if inscripcion.get('beneficiario') == 'No' else None)
                completo_estudios = 1 if inscripcion.get('completo_estudios') == 'Si' else (0 if inscripcion.get('completo_estudios') == 'No' else None)
                matricula = 1 if inscripcion.get('matricula') == 'Si' else (0 if inscripcion.get('matricula') == 'No' else None)
                legajo_fisico = 1 if inscripcion.get('legajo_fisico') == 'Si' else (0 if inscripcion.get('legajo_fisico') == 'No' else None)

                values = (
                    inscripcion.get('nombre'),
                    inscripcion.get('apellido'),
                    inscripcion.get('fecha_nac'),
                    inscripcion.get('provincia'),
                    inscripcion.get('dni'),
                    inscripcion.get('edad'),
                    inscripcion.get('domicilio'),
                    inscripcion.get('telefono_fijo'),
                    inscripcion.get('celular_nro'),
                    inscripcion.get('email'),
                    inscripcion.get('estado_civil'),
                    hijos,
                    inscripcion.get('lugar_trabajo'),
                    inscripcion.get('tel_emergencia'),
                    inscripcion.get('col_egreso'),
                    inscripcion.get('titulo'),
                    inscripcion.get('otro_titulo'),
                    inscripcion.get('anio_egreso'),
                    ingreso,
                    inscripcion.get('cual_otro_ingreso'),
                    completo_estudios,
                    beneficiario,
                    matricula,
                    legajo_fisico
                )

                # Verificar si el registro ya existe
                cursor.execute("SELECT COUNT(*) FROM dat_insc WHERE DNI = %s", (inscripcion.get('dni'),))
                record_exists = cursor.fetchone()[0]

                if not record_exists:
                    insert_query = """
                    INSERT INTO dat_insc (
                        Nombre, Apellido, Fecha_Nac, Provincia, DNI, Edad, Domicilio, Telefono_Fijo, Celular_Nro, 
                        Email, Estado_Civil, Hijos, Lugar_Trabajo, Tel_Emergencia, Col_Egreso, Titulo, Otro_Titulo, 
                        Anio_Egreso, Preg_1, Resp_1, Preg_2, Resp_2, Matricula, Legajo_Fisico
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(insert_query, values)
                    connection.commit()
                    print(f'Datos insertados para DNI: {inscripcion.get("dni")}')
                else:
                    print(f'Registro ya existente para DNI: {inscripcion.get("dni")}')

        except Exception as e:
            print(f'Error: {e}')
        finally:
            cursor.close()
            connection.close()
            print('Conexión a MySQL cerrada')

# Ejecutar sincronización

