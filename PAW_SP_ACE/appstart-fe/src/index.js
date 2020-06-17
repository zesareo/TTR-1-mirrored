import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

import RegistroETS from './RegistroETS';
import Checkout from './Checkout';
import AppLogin from './components/AppLogin';
import SignInSide from './components/SignInSide';
import SignUp from './components/SignUp';

import MaterialTableDemo from './MaterialTableDemo';
import * as serviceWorker from './serviceWorker';

import { BrowserRouter } from  'react-router-dom'
import { Route, Link } from  'react-router-dom'
import  UsuariosList  from  './components/UsuariosList'
import  UsuarioCreateUpdate  from  './components/UsuarioCreateUpdate'
import Table_Alumnos_PAW from './components/Table_Alumnos_PAW'


const BaseLayout = () => (
  <div className="container-fluid">
<nav className="navbar navbar-expand-lg navbar-light bg-light">
  <a className="navbar-brand" href="#">Django React Demo</a>
  <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span className="navbar-toggler-icon"></span>
  </button>
  <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div className="navbar-nav">
      <a className="nav-item nav-link" href="/">USUARIOS</a>
      <a className="nav-item nav-link" href="/Usuario">CREATE USUARIO</a>

    </div>
  </div>
</nav>

    <div className="content">
      <Route path="/" exact component={UsuariosList} />
      <Route path="/Usuario/:pk"  component={UsuarioCreateUpdate} />
      <Route path="/Usuario/" exact component={UsuarioCreateUpdate} />

    </div>

  </div>
)


ReactDOM.render(
  
  <React.StrictMode>
     <AppLogin/>
     <Table_Alumnos_PAW/>
     <App />
       <BrowserRouter>
        <BaseLayout/>
      </BrowserRouter>
    {/*
   
    
    <SignUp/>
    <SignInSide/>
    <App />
    <RegistroETS/>
    <Checkout/>
    <MaterialTableDemo/>
    */}
    
  </React.StrictMode>,
  document.getElementById('root')  
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
