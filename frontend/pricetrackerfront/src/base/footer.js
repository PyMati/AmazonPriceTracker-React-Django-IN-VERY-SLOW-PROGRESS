import React from "react";
import { renderMatches } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

export default class Footer extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            date: new Date()
        }
    }
    render(){
        return(
            <footer className="fixed-bottom bg-transparent text-center">
            <div className="row">
                <div className="col-4">
                    <p>{this.state.date.getDate()+"/"+this.state.date.getMonth()+"/"+this.state.date.getFullYear()}</p>
                </div>
                <div className="col-4">
                    <p>
                    <FontAwesomeIcon icon="fa-brands fa-github" />
                    </p>
                </div>
                <div className="col-4">
                    <p>Mateusz Cieśliński</p>
                </div>
            </div>
            </footer>
        )
    }
}