import React, {Component} from 'react';
import description_text from "./images/Descr.png";
import nevermiss_text from "./images/Nevermissthebestprices.png";
import nevermiss_text_sale from "./images/Nevermiss.png"

class Text extends Component{
    constructor(props){
      super(props);
      this.state = {
        image: [description_text, nevermiss_text, nevermiss_text_sale]
      }
    };
    render(){
      return(
        <img src={this.state.image[this.props.index]} alt="Text" />
      )
    }
  }

export default Text;