import React from "react";
import RegisterForm from "../forms/register_form.js";
import Footer from "../base/footer.js";
import Navbar from "../base/navbar.js";
import 'bootstrap/dist/css/bootstrap.min.css';

export default class RegisterPage extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return(
            <div>
                <Navbar />
                <RegisterForm />
                <Footer />
            </div>
        )
    }
}