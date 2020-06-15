import React from 'react';
import MaterialTable from 'material-table';

export default function MaterialTableDemo() {
  const [state, setState] = React.useState({
    columns: [
      { title: 'id', field: 'id', type: 'numeric' },
        { title: 'rol', field: 'rol' },
        { title: 'correo', field: 'correo' },
        { title: 'contrasena', field: 'contrasena'},  
        { title: 'paterno', field: 'materno' },
        { title: 'nombre', field: 'nombre' },
        { title: 'nacimiento', field: 'nacimiento', type: 'date' },
        { title: 'telefono', field: 'telefono' },
        { title: 'domicilio', field: 'domicilio' },
    ],

    
    data: [
     
      { id: 1, rol: 'Alumno',correo :'a@a', contrasena: 'jeje', paterno: 'x', materno: 'Baran',nombre: 'Baran', nacimiento:'12/12/1992',telefono:'3322323',domicilio:'xyw' },
    ],
    
  });

  return (
    <MaterialTable
      title="Editable Example"
      columns={state.columns}
      data={state.data}
      editable={{
        onRowAdd: (newData) =>
          new Promise((resolve) => {
            setTimeout(() => {
              resolve();
              setState((prevState) => {
                const data = [...prevState.data];
                data.push(newData);
                return { ...prevState, data };
              });
            }, 600);
          }),
        onRowUpdate: (newData, oldData) =>
          new Promise((resolve) => {
            setTimeout(() => {
              resolve();
              if (oldData) {
                setState((prevState) => {
                  const data = [...prevState.data];
                  data[data.indexOf(oldData)] = newData;
                  return { ...prevState, data };
                });
              }
            }, 600);
          }),
        onRowDelete: (oldData) =>
          new Promise((resolve) => {
            setTimeout(() => {
              resolve();
              setState((prevState) => {
                const data = [...prevState.data];
                data.splice(data.indexOf(oldData), 1);
                
                return { ...prevState, data };
              });
            }, 600);
          }),
      }}
    />
  );
}
