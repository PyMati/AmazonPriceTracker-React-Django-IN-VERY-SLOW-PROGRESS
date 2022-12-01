import React, { Suspense } from "react";
import "../index.css"
import 'bootstrap/dist/css/bootstrap.min.css';

export default class RegisterForm extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            fields: false
        }
    }
    render() {
        return(
        <div className="center col-12">
            <form>
                <div class="form-group pret">
                    <label>Username</label>
                    <br></br>
                    <input type = "email" className = "form-control-sm"></input>
                </div>
                <div class="form-group pret">
                    <label>Email</label>
                    <br></br>
                    <input type = "email" className = "form-control-sm"></input>
                </div>
                <div class="form-group pret">
                    <label>Password</label>
                    <br></br>
                    <input type = "password" className = "form-control-sm"></input>
                </div>
                <button className = "btn btn-dark pret">Register</button>
            </form>
        </div>
        )
    }
}
