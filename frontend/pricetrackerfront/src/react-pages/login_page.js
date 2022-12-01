import React from "react";
import LoginForm from "../forms/login_form.js";
import Footer from "../base/footer.js";
import Navbar from "../base/navbar.js";
import 'bootstrap/dist/css/bootstrap.min.css';

export default class LoginPage extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return(
            <div>
                <Navbar />
                <LoginForm />
                <Footer />
            </div>
        )
    }
}