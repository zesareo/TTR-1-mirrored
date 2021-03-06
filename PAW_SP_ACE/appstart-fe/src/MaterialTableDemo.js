import React, {Component} from 'react';
import MaterialTable from 'material-table';
import { formatMs } from '@material-ui/core';
import UsuariosService from './services/UsuariosService';

import { forwardRef } from 'react';

import AddBox from '@material-ui/icons/AddBox';
import ArrowDownward from '@material-ui/icons/ArrowDownward';
import Check from '@material-ui/icons/Check';
import ChevronLeft from '@material-ui/icons/ChevronLeft';
import ChevronRight from '@material-ui/icons/ChevronRight';
import Clear from '@material-ui/icons/Clear';
import DeleteOutline from '@material-ui/icons/DeleteOutline';
import Edit from '@material-ui/icons/Edit';
import FilterList from '@material-ui/icons/FilterList';
import FirstPage from '@material-ui/icons/FirstPage';
import LastPage from '@material-ui/icons/LastPage';
import Remove from '@material-ui/icons/Remove';
import SaveAlt from '@material-ui/icons/SaveAlt';
import Search from '@material-ui/icons/Search';
import ViewColumn from '@material-ui/icons/ViewColumn';

const tableIcons = {
    Add: forwardRef((props, ref) => <AddBox {...props} ref={ref} />),
    Check: forwardRef((props, ref) => <Check {...props} ref={ref} />),
    Clear: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
    Delete: forwardRef((props, ref) => <DeleteOutline {...props} ref={ref} />),
    DetailPanel: forwardRef((props, ref) => <ChevronRight {...props} ref={ref} />),
    Edit: forwardRef((props, ref) => <Edit {...props} ref={ref} />),
    Export: forwardRef((props, ref) => <SaveAlt {...props} ref={ref} />),
    Filter: forwardRef((props, ref) => <FilterList {...props} ref={ref} />),
    FirstPage: forwardRef((props, ref) => <FirstPage {...props} ref={ref} />),
    LastPage: forwardRef((props, ref) => <LastPage {...props} ref={ref} />),
    NextPage: forwardRef((props, ref) => <ChevronRight {...props} ref={ref} />),
    PreviousPage: forwardRef((props, ref) => <ChevronLeft {...props} ref={ref} />),
    ResetSearch: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
    Search: forwardRef((props, ref) => <Search {...props} ref={ref} />),
    SortArrow: forwardRef((props, ref) => <ArrowDownward {...props} ref={ref} />),
    ThirdStateCheck: forwardRef((props, ref) => <Remove {...props} ref={ref} />),
    ViewColumn: forwardRef((props, ref) => <ViewColumn {...props} ref={ref} />)
  };


const usuariosService = new UsuariosService();

export default class MaterialTableDemo extends Component {
  constructor(props){
    super(props);

    this.state={
      columns: [
        //Datos Usuario
        { title: 'id', field: 'id',  hidden: true  },
        { title: 'rol', field: 'rol' },
        { title: 'correo', field: 'correo' },
        { title: 'contrasena', field: 'contrasena', editable: 'onAdd'},
        //editable: 'never,onAdd, onUpdate, always'  
        { title: 'paterno', field: 'paterno' },
        { title: 'paterno', field: 'materno' },
        { title: 'nombre', field: 'nombre' },
        //{ title: 'nacimiento', field: 'nacimiento' , type: date formatMs(YYYY-MM-DD)},
        { title: 'nacimiento', field: 'nacimiento'},
        { title: 'telefono', field: 'telefono' },
        { title: 'domicilio', field: 'domicilio' },
      
      ],      
      data: [],
    }
  }

  componentDidMount(){
    usuariosService.getUsuarios().then(data => {
      this.setState({data:data})
    })
  }

  render(){
    return (
      <MaterialTable
        icons = {tableIcons}
        title="Usuarios"
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
                  console.log("data",newData)
                  usuariosService.createUsuario(newData);
                  //FALTA VALIDAR SI SE CREO EL USUARIO PARA INSERTARLO EN LA TABLA                                
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
                    console.log("data",newData)
                    usuariosService.updateUsuario(newData)
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
                  console.log("data",oldData)
                  usuariosService.deleteUsuario(oldData)
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
