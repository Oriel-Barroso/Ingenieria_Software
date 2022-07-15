import React from 'react';
import '../styles/App.css';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Login from './Login';
import Nav from './Nav';
import Home from './Home'
import Register from './Register'


export default function App(){
  
  
    return (
      
      <div>
        
        <Nav/>
        <Router >
          <Routes>
            
            <Route path="/" exact element={<Login/>}/>
            <Route path="/home" exact element={<Home/>}/>
            <Route path="/register" exact element={<Register/>}/>
          
          </Routes> 
        </Router>
        </div>
        
    )
  
}