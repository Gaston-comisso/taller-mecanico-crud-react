import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'; // Asegúrate de importar el archivo CSS

function App() {
  const [clients, setClients] = useState([]);
  const [vehiculos, setVehiculos] = useState([]);
  const [reparaciones, setReparaciones] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch de Clientes
    axios.get('http://localhost:5000/api/clients')
      .then(response => {
        const data = response.data;
        if (Array.isArray(data)) {
          setClients(data);
        } else {
          setError('Datos de clientes no válidos');
        }
      })
      .catch(error => {
        setError(`Error al cargar clientes: ${error.message}`);
      });

    // Fetch de Vehiculos
    axios.get('http://localhost:5000/api/vehiculo')
      .then(response => {
        const data = response.data;
        if (Array.isArray(data)) {
          setVehiculos(data);
        } else {
          setError('Datos de vehículos no válidos');
        }
      })
      .catch(error => {
        setError(`Error al cargar vehículos: ${error.message}`);
      });

    // Fetch de Reparaciones
    axios.get('http://localhost:5000/api/reparaciones')
      .then(response => {
        const data = response.data;
        if (Array.isArray(data)) {
          setReparaciones(data);
        } else {
          setError('Datos de reparaciones no válidos');
        }
      })
      .catch(error => {
        setError(`Error al cargar reparaciones: ${error.message}`);
      });

    setLoading(false);
  }, []);

  if (loading) return <div>Cargando...</div>;
  if (error) return <div>{error}</div>;

  const handleEdit = (id) => {
    console.log('Editar ID:', id);
    // Aquí iría la lógica para editar
  };

  const handleDelete = (id) => {
    console.log('Borrar ID:', id);
    // Aquí iría la lógica para borrar
  };

  return (
    <div className="container">
      <h1 className="title">Clientes, Vehículos y Reparaciones</h1>

      <section className="table-section">
        <h2>Clientes</h2>
        <table className="data-table">
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Email</th>
              <th>Teléfono</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {clients.map((client, index) => (
              <tr key={index}>
                <td>{client.name ?? 'Sin nombre'}</td>
                <td>{client.email ?? 'No disponible'}</td>
                <td>{client.phone ?? 'No disponible'}</td>
                <td>
                  <button className="btn-edit" onClick={() => handleEdit(client.id)}>Editar</button>
                  <button className="btn-delete" onClick={() => handleDelete(client.id)}>Borrar</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>

      <section className="table-section">
        <h2>Vehículos</h2>
        <table className="data-table">
          <thead>
            <tr>
              <th>Marca</th>
              <th>Modelo</th>
              <th>Patente</th>
              <th>Año</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {vehiculos.map((vehiculo, index) => (
              <tr key={index}>
                <td>{vehiculo.marca ?? 'Sin marca'}</td>
                <td>{vehiculo.modelo ?? 'No disponible'}</td>
                <td>{vehiculo.patente ?? 'No disponible'}</td>
                <td>{vehiculo.año ?? 'No disponible'}</td>
                <td>
                  <button className="btn-edit" onClick={() => handleEdit(vehiculo.id)}>Editar</button>
                  <button className="btn-delete" onClick={() => handleDelete(vehiculo.id)}>Borrar</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>

      <section className="table-section">
        <h2>Reparaciones</h2>
        <table className="data-table">
          <thead>
            <tr>
              <th>Descripción</th>
              <th>Fecha Ingreso</th>
              <th>Fecha Entrega</th>
              <th>Estado</th>
              <th>Vehículo ID</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {reparaciones.map((reparacion, index) => (
              <tr key={index}>
                <td>{reparacion.descripcion ?? 'Sin descripción'}</td>
                <td>{reparacion.fecha_ingreso ?? 'No disponible'}</td>
                <td>{reparacion.fecha_entrega ?? 'No disponible'}</td>
                <td>{reparacion.estado ?? 'No disponible'}</td>
                <td>{reparacion.vehiculo_id ?? 'No disponible'}</td>
                <td>
                  <button className="btn-edit" onClick={() => handleEdit(reparacion.id)}>Editar</button>
                  <button className="btn-delete" onClick={() => handleDelete(reparacion.id)}>Borrar</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </div>
  );
}

export default App;
