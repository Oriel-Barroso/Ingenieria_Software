import '../styles/Login.css';
import Axios  from "axios";
import React, {useState} from "react";
import { useNavigate} from "react-router-dom";

function Login() {
    
    const navigate = useNavigate();

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const login = async(e) => {
    e.preventDefault()

    await Axios.get('http://127.0.0.1:8000/app1/get_user/'+ username,{

        
    }).then((response) => {
        
        
        console.log(response)
        navigate('/home')
        localStorage.setItem("user", JSON.stringify(response.data))
        
    });
};
  
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
        

    </div>
      
);
}

export default Login;
