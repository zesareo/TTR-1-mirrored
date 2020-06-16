import React, {Component} from 'react';
import MaterialTable from 'material-table';
import { formatMs } from '@material-ui/core';
import AlumnosService from '../services/AlumnosService';
import Paper from '@material-ui/core/Paper';
import TableContainer from '@material-ui/core/TableContainer';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';

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



const alumnosService = new AlumnosService();

export default class Table_Alumnos_PAW extends Component {
  constructor(props){
    super(props);

    this.state={
      columns: [
        //Datos Usuario
        { title: 'id', field: 'usuario.id' , hidden: false},
        //{ title: 'rol', field: 'usuario.rol', lookup: { 'Alumno': 'Alumno', 'Agente': 'Agente' },},
        { title: 'rol', field: 'usuario.rol', editable: 'onAdd'},
        { title: 'correo', field: 'usuario.correo' , editable: 'onAdd'},
        { title: 'contrasena', field: 'usuario.contrasena', editable: 'onAdd'},
        { title: 'paterno', field: 'usuario.paterno', editable: 'onAdd'},
        { title: 'paterno', field: 'usuario.materno', editable: 'onAdd' },
        { title: 'nombre', field: 'usuario.nombre', editable: 'onAdd' },
        
        //{ title: 'nacimiento', field: 'nacimiento' , type: date formatMs(YYYY-MM-DD)},
        { title: 'nacimiento', field: 'usuario.nacimiento', editable: 'onAdd'},
        { title: 'telefono', field: 'usuario.telefono', editable: 'onAdd'},
        { title: 'domicilio', field: 'usuario.domicilio', editable: 'onAdd'},
        //Datos alumno
        { title: 'boleta', field: 'boleta'},
        { title: 'curp', field: 'curp' },
        { title: 'fecha de ingreso', field: 'fecha_ingreso' },
        
      ],      
      data: [],
      loading:true,
    }
  }

  componentDidMount(){
    alumnosService.getAlumnos().then(data => {
      this.setState({data:data})
      this.setState({loading: false});
    })
  }

  render(){
    if(this.state.loading)
    {
      return (<p>Cargando...</p>);
    }
    return (
      <Grid container spacing={3}>
        <Grid item xs={12} md={1}>

        </Grid>
        <Grid item xs={12} md={10}>
        <MaterialTable 

          icons = {tableIcons}
          title="Alumnos"
          columns={this.state.columns}
          data={this.state.data}
          editable={{
            onRowAdd: (newData) =>
              new Promise((resolve) => {
                setTimeout(() => {
                  if (newData.boleta === '') {
                    return;
                }
                  resolve();
                  this.setState((prevState) => {
                    const data = [...prevState.data];                  
                    console.log("data",newData)
                    alumnosService.createAlumno(newData)
                    //FALTA VALIDAR SI SE CREO EL USUARIO PARA INSERTARLO EN LA TABLA
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
                    this.setState((prevState) => {
                      const data = [...prevState.data];                  
                      console.log("data",newData)
                      alumnosService.updateAlumno(newData)
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
                    alumnosService.deleteAlumno(oldData)
                    data.splice(data.indexOf(oldData), 1);
                    return { ...prevState, data };
                  });
                }, 600);
              }),
          }}
        />
        </Grid>
      </Grid>
    );
  }

}
