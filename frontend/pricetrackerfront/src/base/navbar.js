import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import "../index.css"

export default class Navbar extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return(
            <nav className="navbar navbar-expand-lg">
                <div className="navbar-nav">
                    <a class="navbar-brand"><h1>APT</h1></a>
                </div>
                <div className="navbar-nav ms-auto">
                    <a class="nav-item nav-link active" href="/">Home</a>
                    <a class="nav-item nav-link active" href="login">Login</a>
                    <a class="nav-item nav-link active " href="register">Register</a>
                </div>
            </nav> 
        )
    }
}