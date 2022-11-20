import React, {Component} from 'react';
import logbutt from "./images/loginbutt.png";
import regbutt from "./images/Register.png";
import howbutt from "./images/howitworks.png";
import gihub from "./images/GitHub.png";
import moneybag from "./images/MoneyBag.png";
import source_code from "./images/Source Code.png";



class Button extends Component{
  constructor(props){
    super(props);
    this.state = {
      image: [logbutt, regbutt, howbutt, gihub, moneybag, source_code]
    }
  };
  render(){
    return(
      <button ><img src={this.state.image[this.props.index]} alt="Button" /></button>
    )
  }
}




export default Button;
