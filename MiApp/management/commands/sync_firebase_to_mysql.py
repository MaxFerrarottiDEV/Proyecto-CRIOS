from django.core.management.base import BaseCommand
import firebase_admin
from firebase_admin import credentials, db
import mysql.connector
from mysql.connector import errorcode


class Command(BaseCommand):
    help = 'Sincroniza los datos de Firebase a MySQL'

    def handle(self, *args, **kwargs):
        # Inicializar Firebase (verificar si ya está inicializado)
        try:
            firebase_admin.get_app()  # Verifica si ya existe una app Firebase inicializada
        except ValueError:  # Si no hay ninguna inicialización previa, inicializamos
            cred = credentials.Certificate('./static/Firebase/credenciales.json')
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://crios-db-proyecto-default-rtdb.firebaseio.com'
            })
            print("Firebase inicializado correctamente.")

        # Configurar conexión a MySQL
        cursor = None
        connection = None
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Samilove2016*',
                database='criosdb',
                auth_plugin='mysql_native_password'
            )
            cursor = connection.cursor()
            print('Conexión a MySQL exitosa')
        except mysql.connector.Error as err:
            print(f"Error de MySQL: {err}")
            return
        except Exception as e:
            print(f"Error general: {e}")
            return

        # Sincronizar Firebase con MySQL
        try:
            ref = db.reference('inscripcion')
            data = ref.get()

            if not data:
                print('No hay datos para sincronizar')
                return

            for key, inscripcion in data.items():
                # Validar datos necesarios
                if not all([inscripcion.get('nombre'), inscripcion.get('apellido'), inscripcion.get('dni')]):
                    print(f'Datos faltantes para inscripción: {key}')
                    continue

                # Transformar valores según el esquema
                hijos = 1 if inscripcion.get('hijos') == 'Si' else 0
                ingreso = 1 if inscripcion.get('ingreso') == 'Si' else 0
                beneficiario = 1 if inscripcion.get('beneficiario') == 'Si' else 0
                completo_estudios = 1 if inscripcion.get('completo_estudios') == 'Si' else 0
                matricula = 1 if inscripcion.get('matricula') == 'Si' else 0
                legajo_fisico = 1 if inscripcion.get('legajo_fisico') == 'Si' else 0

                # Preparar datos para inserción
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
            print(f'Error durante la sincronización: {e}')
        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
                print('Conexión a MySQL cerrada')
