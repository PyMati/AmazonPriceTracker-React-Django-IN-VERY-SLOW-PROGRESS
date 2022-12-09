import React from "react";
import Navbar from "../base/navbar";
import Footer from "../base/footer";

export default class HomePage extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return(
            <div>
                <Navbar />
                <Footer />
            </div>
        )
    }


}