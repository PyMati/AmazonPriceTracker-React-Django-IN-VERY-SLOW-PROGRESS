import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./index.css"
import 'bootstrap/dist/css/bootstrap.min.css';
import LoginPage from "./login_page";

class App extends React.Component{
    render(){
        return(
        <BrowserRouter>
            <Routes>
              <Route path="/" element={<LoginPage />}></Route>
            </Routes>
        </BrowserRouter>
        )
    }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App/>);