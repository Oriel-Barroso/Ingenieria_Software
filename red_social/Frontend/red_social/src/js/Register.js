import React from "react"
import { useState} from "react";
import Axios  from "axios";
import { useNavigate} from "react-router-dom";

import swal from 'sweetalert';
//Create new user
export default function Register() {
    const navigate = useNavigate();
    const alert=()=>{
        swal({
          title: 'Error faltan campos'
        })}
    const [first_name, setfirst_name] = useState("");
    const [last_name, setlast_name] = useState("");
    const [email, setemail] = useState("");
    const [passwordReg, setPasswordReg] = useState("");
    const [usernameReg, setUsernameReg] = useState("");
    

    const register = (e) => {
        e.preventDefault()
        if(!usernameReg || !passwordReg ){
          alert()
          
        }else{
        Axios.post('http://127.0.0.1:8000/app1/registro/',{
            first_name: first_name,
            last_name: last_name,
            email: email,
            username: usernameReg,
            password: passwordReg,

        }).then((response) => {
            
            console.log(response)
            navigate('/')
           
            
        });
    };
}
    
return (
    
    <div className="App">
        <label htmlFor="first_name">first_name</label>
            <input type="text" className="log-input" placeholder= "Juan" 
            onChange={(e)=>{
            setfirst_name(e.target.value);
            }}
            />
        <label htmlFor="last_name">last_name</label>
            <input type="text" className="log-input" placeholder= "Fernández" 
            onChange={(e)=>{
            setlast_name(e.target.value);
            }}
            />
        <label htmlFor="email">email</label>
            <input type="text" className="log-input" placeholder= "juanfernandez@gmail.com" 
            onChange={(e)=>{
            setemail(e.target.value);
            }}
            />         
        
        <label htmlFor="username">Username</label>
            <input type="text" className="log-input" placeholder="  Ej: Lucas23423"
            onChange={(e)=>{
            setUsernameReg(e.target.value);
            }}
            />
        <label htmlFor="password">password</label>
            <input type="password" className="log-input" placeholder= "***********" 
            onChange={(e)=>{
            setPasswordReg(e.target.value);
            }}
            />
           
        <button className="button-log"  onClick={register}>Register</button>
        


    </div>
    
);


}