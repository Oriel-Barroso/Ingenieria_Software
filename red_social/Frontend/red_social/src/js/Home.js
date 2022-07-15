import React from 'react';
import '../styles/Home.css';
import { useNavigate} from "react-router-dom";

export default function Home(){
    const navigate = useNavigate();
    const user = localStorage.getItem('user').replace(/['"]+/g, '')
    
    const logout= async(e) => {
        navigate('/')
        localStorage.removeItem('user') 
    }
    return(
        <div className='user'>
            <div className="profile">
                <img  src= '../img/user.jpg'/>
                <h1 className='username'>{user}</h1>
            </div>    
            <h1>Incio de sesión correcto</h1>
            <h1>HOLA {user}</h1>
            <div className='logout'>
                <button onClick={logout} className ="logout">Logout</button>
            </div>
        </div>
    );
}