import React from "react";
import { renderMatches } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';

export default class Footer extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            date: Date.now()
        }
    }
    render(){
        return(
            <footer>
                <p>{this.state.date}</p>
            </footer>
        )
    }
}