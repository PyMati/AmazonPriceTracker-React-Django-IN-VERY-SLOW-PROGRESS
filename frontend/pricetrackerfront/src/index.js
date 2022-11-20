import React from 'react';
import ReactDOM from 'react-dom/client';
import "./index.css"
import Button from './buttons.js';
import Text from "./text.js"
import Image from './images.js';

class App extends React.Component{
    render(){
        return(
            <div>
                <Button index = {0}/>
                <Button index = {1}/>
                <Button index = {2}/>
                <Text index = {0}/>
                <Text index = {1}/>
                <Text index = {2}/>
                <Image index = {0}/>
                <Image index = {1}/>
                <Image index = {2}/>
            </div>
        )
    }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App/>);