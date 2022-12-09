import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

export default class Navbar extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return(
            <nav className="navbar navbar-expand-lg">
                <div className="navbar-nav">
                    <a class="navbar-brand">APT</a>
                    <a class="nav-item nav-link active " href="login">Home</a>
                    <a class="nav-item nav-link active" href="login">Login</a>
                    <a class="nav-item nav-link active" href="register">Register</a>
                </div>
            </nav> 
        )
    }
}