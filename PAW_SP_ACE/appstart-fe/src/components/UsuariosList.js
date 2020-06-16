import  React, { Component } from  'react';
import  UsuariosService  from  '../services/UsuariosService';

const  usuariosService  =  new  UsuariosService(); 

class  UsuariosList  extends  Component {

    constructor(props) {
        super(props);
        this.state  = {
            usuarios: [],
            nextPageURL:  ''
        };
        this.nextPage  =  this.nextPage.bind(this);
        this.handleDelete  =  this.handleDelete.bind(this);

    }

    
    componentDidMount() {
        var self = this;
        usuariosService.getUsuarios().then(function (result) {
            self.setState({ usuarios:  result.data, nextPageURL:  result.nextlink})
        });
    }

    //Delet a user
    handleDelete(e,pk){
        var self = this;
        usuariosService.deleteUsuario({pk :  pk}).then(()=>{
            var  newArr  =  self.state.usuarios.filter(function(obj) {
                return  obj.pk  !==  pk;
            });
            self.setState({usuarios:  newArr})
        });
    }

    nextPage(){
        var self = this;
        usuariosService.getUsuariosByURL(this.state.nextPageURL).then((result) => {
            self.setState({ usuarios:  result.data, nextPageURL:  result.nextlink})
        });
    }

    render() {
        return (
            
        <div  className="usuarios--list">
            <table  className="table">
                <thead  key="thead">
                <tr>
                    <th>#</th>
                    <th>rol</th>
                    <th>Correo</th>                   
                    <th>Paterno</th>
                    <th>Materno</th>
                    <th>Nombre</th>
                    <th>Nacimiento</th>
                    <th>Telefono</th>
                    <th>Direccion</th>
                    <th>Actions</th>
                </tr>
                </thead>
                <tbody>
                    
                    {/*this.bind.state.usuario.map( c  =>
                    <tr  key={c.id}>
                        <td>{c.rol}  </td>
                        <td>{c.correo}</td>                    
                        <td>{c.paterno}</td>
                        <td>{c.materno}</td>
                        <td>{c.nombre}  </td>
                        <td>{c.nacimiento}</td>
                        <td>{c.telefono}  </td>
                        <td>{c.direccion}</td>
                        <td>
                        <button  onClick={(e)=>  this.handleDelete(e,c.id) }> Delete</button>
                        <a  href={"/Usuario/" + c.id}> Update</a>
                        </td>
                    </tr>)*/}
                </tbody>
            </table>
            <button  className="btn btn-primary"  onClick=  {  this.nextPage  }>Next</button>
        </div>
        );
    }
}
export  default  UsuariosList;