import React from 'react';
import '../styles/Nav.css';


export default function Menu(){
    
    return(
        <div className="container">
            <div className="subcontainer">
                <div className= "back-tittle">
                    <h1 className = "tittle">
                    RED SOCIAL
                    </h1>
                </div>
            </div>
                    
            <div className='Add'>
                <button className ="logout">Logout</button>
            </div>
        </div>
    );
}