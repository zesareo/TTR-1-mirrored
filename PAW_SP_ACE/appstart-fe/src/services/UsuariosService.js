import axios from 'axios';
const API_URL = `http://localhost:8000/api/appstart/v2/`;

export default class UsuariosService{

    constructor(){}


    getUsuarios() {
        const url = `${API_URL}Usuario/`;
        //const url = 'http://localhost:8000/api/appstart/v2/Usuario/';
        console.log("URL ACCEDIDA"+ url);
        return axios.get(url).then(response => response.data);
    }
    getUsuariosByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getUsuario(pk) {        
        const url = `${API_URL}Usuario/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteUsuario(usuario){
        const url = `${API_URL}Usuario/${usuario.pk}`;
        return axios.delete(url);
    }
    createUsuario(usuario){
        const url = `${API_URL}Usuario/`;
        return axios.post(url,usuario);
    }
    updateUsuario(usuario){
        const url = `${API_URL}Usuario/${usuario.pk}`;
        return axios.put(url,usuario);
    }
}

