import React, {Component} from 'react';
import gihub from "./images/GitHub.png";
import moneybag from "./images/MoneyBag.png";
import source_code from "./images/Source Code.png";



class Image extends Component{
  constructor(props){
    super(props);
    this.state = {
      image: [gihub, moneybag, source_code]
    }
  };
  render(){
    return(
      <img src={this.state.image[this.props.index]} alt="Image" />
    )
  }
}




export default Image;