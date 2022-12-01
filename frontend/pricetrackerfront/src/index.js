import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./index.css"
import 'bootstrap/dist/css/bootstrap.min.css';
import LoginPage from "./react-pages/login_page.js";
import RegisterPage from './react-pages/register_page.js';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

class App extends React.Component{
    render(){
        return(
        <BrowserRouter>
            <Routes>
              <Route path="/login" element={<LoginPage />}></Route>
              <Route path='/register' element={<RegisterPage />}></Route>
            </Routes>
        </BrowserRouter>
        )
    }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App/>);