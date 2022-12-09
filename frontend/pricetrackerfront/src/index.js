// React imports
import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from "react-router-dom";

// Stylesheets
import "./index.css"
import 'bootstrap/dist/css/bootstrap.min.css';

//Pages
import LoginPage from "./react-pages/login_page.js";
import RegisterPage from './react-pages/register_page.js';
import HomePage from './react-pages/home_page';

class App extends React.Component{
    render(){
        return(
        <BrowserRouter>
            <Routes>
              <Route path='/' element={<HomePage />}></Route>
              <Route path="/login" element={<LoginPage />}></Route>
              <Route path='/register' element={<RegisterPage />}></Route>
            </Routes>
        </BrowserRouter>
        )
    }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App/>);