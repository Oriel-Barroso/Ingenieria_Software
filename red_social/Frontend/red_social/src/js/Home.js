import React from 'react';
import '../styles/Home.css';
import { useHistory } from "react-router-dom";

export default function Home(){
    const user = localStorage.getItem('user')
    
    return(
        <div className='user'>
            <h1>HOLA {user}</h1>
        </div>
    );
}