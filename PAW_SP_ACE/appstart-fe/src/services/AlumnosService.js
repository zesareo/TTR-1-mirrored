import axios from 'axios';
const API_URL = `http://localhost:8000/api/appstart/v2/Alumno/`;

export default class AlumnosService{

    constructor(){}


    getAlumnos() {
        const url = `${API_URL}`;
        return axios.get(url).then(response => response.data);
        /*
                axios.get(url).then(response => response.data).then(data => {
        console.log("data",data)
        })  
        })*/
    }
    getAlumnosByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getAlumno(pk) {        
        const url = `${API_URL}${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteAlumno(alumno){
       /* alumno.usuario.id
        alumno.usuario.rol
        ...
        alumno.boleta*/
        const url = `${API_URL}${alumno.usuario.id}`;
        return axios.delete(url);
    }
    createAlumno(alumno){
        const url = `${API_URL}`;
        return axios.post(url,alumno);
    }
    updateAlumno(alumno){
        const url = `${API_URL}${alumno.usuario.id}`;
        return axios.put(url,alumno);
    }
}

