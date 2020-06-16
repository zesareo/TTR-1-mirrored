import React from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import PageNotFound from "./components/PageNotFound"
import  MaterialTableDemo  from  './MaterialTableDemo'
import  Table_Alumnos_PAW  from  './components/Table_Alumnos_PAW'
import UsuariosList from './components/UsuariosList'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <div className="app s-pxy-2">
          <h1 className="s-center">Bienvenidos a PAW</h1>
          <Router>
            <ul className="nav-container s-border s-main-center s-pl-0">
              
              <li className="nav-container--item s-mr-2">
              <Link to="/">UsuariosTable</Link></li>
              
              <li className="nav-container--item s-mr-2">
              <Link to="/info">AlumnoTable</Link></li>
              
              <li className="nav-container--item">
              <Link to="/contacto">Contactanos</Link></li>
            </ul>
            <Switch>
              <Route exact path="/" component={MaterialTableDemo}/>
              <Route exact path="/info" component={Table_Alumnos_PAW}/>
              <Route exact path="/contacto" component={MaterialTableDemo}/>
              <Route component={PageNotFound}/>
            </Switch>
          </Router>
          </div>
      </header>
    </div>
  );
}

export default App;
