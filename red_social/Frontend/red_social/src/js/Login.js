import '../styles/Login.css';
import Axios  from "axios";
import React, {useState} from "react";
import { useNavigate} from "react-router-dom";
import swal from 'sweetalert';

function Login() {

    const empty =()=>{
        swal({
          title: 'Enter username and password',
          icon: 'warning',
          button: 'OK',
        })}
      
    
    const navigate = useNavigate();

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const login = async(e) => {

        e.preventDefault()

        if(!username || !password ){
            empty()
            return
        } 

        await Axios.post('http://127.0.0.1:8000/app1/get_user/',{
            
            username: username,
            password: password,
             
        }).then((response) => {
            
            console.log(response)
            navigate('/home')
            localStorage.setItem("user", JSON.stringify(response.data))
            
        });
           
    };
    const registerfunction = async(e) => {
        navigate('/register')
    }
    return (
    
        <div className="App">
            
            <label htmlFor="email">Username</label>
                <input type="text" className="log-input" placeholder="  Ej: Lucas23423"
                onChange={(e)=>{
                setUsername(e.target.value);
                }}
                />
            <label htmlFor="password">password</label>
                <input type="password" className="log-input" placeholder= "***********" 
                onChange={(e)=>{
                setPassword(e.target.value);
                }}
                />
            <button className="button-log"  onClick={login}>Login</button>
            
            <button className="button-register" onClick={registerfunction}>Register </button>
            
            

        </div>
        
    );
    }

export default Login;
