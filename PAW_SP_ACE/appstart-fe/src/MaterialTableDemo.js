import React, {Component} from 'react';
import MaterialTable from 'material-table';
import MaterialTableDemo2 from './MaterialTableDemo2';
import axios from 'axios';
import { formatMs } from '@material-ui/core';

export default class MaterialTableDemo extends Component {
  constructor(props){
    super(props);

    this.state={
      columns: [
        //{ title: 'id', field: 'id', type: 'numeric' },
        { title: 'rol', field: 'rol' },
        { title: 'correo', field: 'correo' },
        { title: 'contrasena', field: 'contrasena'},  
        { title: 'paterno', field: 'paterno' },
        { title: 'paterno', field: 'materno' },
        { title: 'nombre', field: 'nombre' },
       // { title: 'nacimiento', field: 'nacimiento' , type: date formatMs(YYYY-MM-DD)},
       { title: 'nacimiento', field: 'nacimiento'},
        { title: 'telefono', field: 'telefono' },
        { title: 'domicilio', field: 'domicilio' },
        
      ],      
      data: [ 
        { rol: 'Alumno',correo :'a@a', contrasena: 'jeje', paterno: 'x', materno: 'Baran',nombre: 'Baran', nacimiento:'12/12/1992',telefono:'3322323',domicilio:'xyw' },
      ],
    }
  }

  componentDidMount(){
    const url = 'http://localhost:8000/api/appstart/v2/Usuario/';
    /*
    axios.get(url).then(response => response.data).then(data => {
      console.log("data",data)
    })*/
    
    axios.get(url).then(response => response.data).then(data => {
      this.setState({data:data})
    })

  }

  render(){
    return (
      <MaterialTable
        title="Editable Example"
        columns={this.state.columns}
        data={this.state.data}
        editable={{
          onRowAdd: (newData) =>
            new Promise((resolve) => {
              setTimeout(() => {
                resolve();
                this.setState((prevState) => {
                  const data = [...prevState.data];
                  data.push(newData);
                  //API CREAR                  
                  console.log("data",newData)
                  axios.post('http://localhost:8000/api/appstart/v2/Usuario/',newData)
                  return { ...prevState, data };
                });
              }, 600);
            }),
          onRowUpdate: (newData, oldData) =>
            new Promise((resolve) => {
              setTimeout(() => {
                resolve();
                if (oldData) {
                  this.setState((prevState) => {
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
                this.setState((prevState) => {
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

}
