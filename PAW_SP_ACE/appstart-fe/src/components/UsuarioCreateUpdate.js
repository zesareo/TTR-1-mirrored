import  React, { Component } from  'react';
import  UsuariosService  from  '../services/UsuariosService';

const  usuariosService  =  new  UsuariosService();

class  UsuarioCreateUpdate  extends  Component {

    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    componentDidMount(){
        const { match: { params } } =  this.props;
        if(params  &&  params.pk)
        {
            usuariosService.getUsuario(params.pk).then((c)=>{
                this.refs.nombre.value  =  c.nombre;
                this.refs.paterno.value  =  c.paterno;
                this.refs.materno.value  =  c.materno;
                this.refs.correo.value  =  c.correo;
                this.refs.telefono.value  =  c.telefono;
                this.refs.direccion.value  =  c.direccion;
            })
        }
    }

    handleCreate(){
        usuariosService.createUsuario(
            {
            "nombre":  this.refs.firstName.value,
            "paterno":  this.refs.lastName.value,
            "materno":  this.refs.lastName.value,
            "correo":  this.refs.email.value,
            "telefono":  this.refs.phone.value,
            "domicilio":  this.refs.address.value,
            //"rol":  this.refs.description.value
            //"nacimiento":  this.refs.description.value
            }).then((result)=>{
                    alert("Usuario created!");
            }).catch(()=>{
                    alert('There was an error! Please re-check your form.');
            });
    }

    handleUpdate(pk){
        usuariosService.updateUsuario(
            {
            "pk":  pk,
            "nombre":  this.refs.nombre.value,
            "paterno":  this.refs.paterno.value,
            "materno":  this.refs.materno.value,
            "correo":  this.refs.correo.value,
            "telefono":  this.refs.telefono.value,
            "direccion":  this.refs.direccion.value
            }
            ).then((result)=>{

                alert("Usuario updated!");
            }).catch(()=>{
                alert('There was an error! Please re-check your form.');
            });
    }

    //Botton functionality
    handleSubmit(event) {
        const { match: { params } } =  this.props;
        if(params  &&  params.pk){
            this.handleUpdate(params.pk);
        }
        else
        {
            this.handleCreate();
        }
        event.preventDefault();
    }

    render() {
        return (
          <form onSubmit={this.handleSubmit}>
          <div className="form-group">
            <label>
              First Name:</label>
              <input className="form-control" type="text" ref='nombre' />

            <label>
              Last Name:</label>
              <input className="form-control" type="text" ref='paterno'/>

            <label>
              Last Name:</label>
              <input className="form-control" type="text" ref='materno'/>

            <label>
              Phone:</label>
              <input className="form-control" type="text" ref='telefono' />

            <label>
              Email:</label>
              <input className="form-control" type="text" ref='correo' />

            <label>
              Address:</label>
              <input className="form-control" type="text" ref='direccion' />


            <input className="btn btn-primary" type="submit" value="Submit" />
            </div>
          </form>
        );
    }

}
export default UsuarioCreateUpdate;