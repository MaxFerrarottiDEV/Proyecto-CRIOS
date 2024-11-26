const admin = require('firebase-admin');
const mysql = require('mysql2');

// Inicializa Firebase
var serviceAccount = require("./credenciales.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://crios-db-proyecto-default-rtdb.firebaseio.com"
});

// Conexión a MySQL
const connection = mysql.createConnection({
  host: 'localhost', 
  user: 'root',      
  password: 'juan1234', 
  database: 'criosdb'
});

connection.connect(err => {
  if (err) {
    console.error('Error conectando a MySQL:', err);
    return;
  }
  console.log('Conexión a MySQL exitosa');
});

async function obtenerRegistrosDrive() {
  try {
    const db = admin.database();
    const ref = db.ref('inscripcion');
    const snapshot = await ref.once('value');
    const data = snapshot.val();

    if (!data) {
      console.log('No hay datos para sincronizar');
      return;
    }

    const promises = [];

    for (const key in data) {
      const inscripcion = data[key];

      // Validar datos
      if (!inscripcion.nombre || !inscripcion.apellido || !inscripcion.dni) {
        console.warn('Datos faltantes para inscripcion:', inscripcion);
        continue; // Salta al siguiente registro
      }
      const hijos = inscripcion.hijos === 'Si' ? 1 : (inscripcion.hijos === 'No' ? 0 : null);
      const ingreso= inscripcion.ingreso === 'Si' ? 1 : (inscripcion.ingreso === 'No' ? 0 : null);
      const beneficiario=inscripcion.beneficiario === 'Si' ? 1 : (inscripcion.beneficiario === 'No' ? 0 : null);
      const completo_estudios= inscripcion.completo_estudios === 'Si' ? 1 : (inscripcion.completo_estudios === 'No' ? 0 : null);
      const matricula=inscripcion.matricula === 'Si' ? 1 : (inscripcion.matricula === 'No' ? 0 : null);
      const legajo_fisico=inscripcion.legajo_fisico === 'Si' ? 1 : (inscripcion.legajo_fisico === 'No' ? 0 : null);
      
      const values = [
        inscripcion.nombre || null,
        inscripcion.apellido || null,
        inscripcion.fecha_nac || null,
        inscripcion.provincia || null,
        inscripcion.dni || null,
        inscripcion.edad || null,
        inscripcion.domicilio || null,
        inscripcion.telefono_fijo || null,
        inscripcion.celular_nro || null,
        inscripcion.email || null,
        inscripcion.estado_civil || null,
        hijos,
        inscripcion.lugar_trabajo || null,
        inscripcion.tel_emergencia || null,
        inscripcion.col_egreso || null,
        inscripcion.titulo || null,
        inscripcion.otro_titulo || null,
        inscripcion.anio_egreso || null,
        ingreso,
        inscripcion.cual_otro_ingreso || null,
        completo_estudios,
        beneficiario,
        matricula,
        legajo_fisico
      ];

      const checkQuery = 'SELECT COUNT(*) AS count FROM dat_insc WHERE DNI = ?';

      promises.push(
        new Promise((resolve,reject) => {
          connection.query(checkQuery, [inscripcion.dni], (err,results) =>{
            if(err) {
              console.error('Error al verificar existencia en MySQL', err);
              reject(err);
              return;
            }

            const recordExists= results[0].count > 0;

            if(!recordExists) {
              const insertQuery = `
              INSERT INTO dat_insc (
                Nombre, Apellido, Fecha_Nac, Provincia, DNI, Edad, Domicilio, Telefono_Fijo, Celular_Nro, 
                Email, Estado_Civil, Hijos, Lugar_Trabajo, Tel_Emergencia, Col_Egreso, Titulo, Otro_Titulo, 
                Anio_Egreso, Preg_1, Resp_1, Preg_2, Resp_2, Matricula, Legajo_Fisico
              ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
              `;

              connection.query(insertQuery, values, (err,results) => {
                if(err) {
                  console.error('Error al insertar en MySQL:', err);
                  reject(err);
                } else {
                  console.log('Datos insertaodos:', results);
                  return(results);
                }
              });
            } else {
              console.log('Registro ya existente:', inscripcion.dni);
              resolve();
            }
          });
        })
      );     
    } 

    await Promise.all(promises);

  } catch (error) {
    console.error('Error:', error);
  } finally {
    // Cerrar la conexión solo cuando todas las inserciones han terminado
    connection.end(err => {
      if (err) {
        console.error('Error al cerrar la conexión:', err);
      } else {
        console.log('Conexión a MySQL cerrada');
      }
    });
  }
}

obtenerRegistrosDrive();
 