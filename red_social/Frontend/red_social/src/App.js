import './App.css';
import Axios  from "axios";
import React, {useState} from "react";



function App() {
  

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const login = async(e) => {
    e.preventDefault()
    
    await Axios.get('http://127.0.0.1:8000/app1/get_user/fsadsfaf',{

        
    }).then((response) => {
     
      
      console.log(response)
        
    });
};
  
return (
  <div className="App">
    
    <label htmlFor="email">Username</label>
        <input type="text" className="log-input" placeholder="  Ej: Lucas23423"
        onChange={(e)=>{
          setUsername(e.target.value);
          console.log(e.target.value)
          }}
        />
        <label htmlFor="password">password</label>
        <input type="password" className="log-input" placeholder= "***********" 
        onChange={(e)=>{
          setPassword(e.target.value);
          }}
        />
      <button className="button-log"  onClick={login}>Login</button>
      <h1>hola{username}</h1>

  </div>
);
}

export default App;
