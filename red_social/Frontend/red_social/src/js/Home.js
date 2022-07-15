import React from 'react';
import '../styles/Home.css';
import { useNavigate} from "react-router-dom";

export default function Home(){
    const user = localStorage.getItem('user')
       
    const navigate = useNavigate();
    const logout= async(e) => {
        navigate('/')
    }
    return(
        <div className='user'>
            <h1>HOLA {user}</h1>
            <div className='Add'>
                <button onClick={logout} className ="logout">Logout</button>
            </div>
        </div>
    );
}