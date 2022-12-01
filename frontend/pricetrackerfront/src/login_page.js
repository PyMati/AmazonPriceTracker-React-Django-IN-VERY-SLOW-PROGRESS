import React from "react";
import LoginForm from "./login_form";
import Footer from "./footer";
import 'bootstrap/dist/css/bootstrap.min.css';

export default class LoginPage extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return(
            <div>
                <LoginForm />
                <Footer />
            </div>
        )
    }
}