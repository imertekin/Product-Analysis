import ProductList from "./components/ProductList";
import SearchBar from "./components/SearchBar";
import React, { useEffect,useState } from 'react'
import axios from "axios"
// import Pagination from "./components/Pagination";
import LandingPage from "./components/LandingPage";





import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import Nav from "./components/Nav";







export default function App()  {
 

  const [Products,setProducts]=useState([]);

  



  useEffect(() => {
    const getProduct = async()=>{
      let res =await axios.get("http://127.0.0.1:8000/api/product/?search= &order=")
      setProducts(res.data.results)
    }
    getProduct()
    
    
  }, [])

 
  const searchbar=async (e)=>{
    e.preventDefault()
    const ip=document.getElementById('test')
    const res = await axios.get("http://127.0.0.1:8000/api/product/?search="+ip.value)
    setProducts(res.data.results)
    ip.value=""
    
    
  }

  
 
    

  
    
    return (
      
      <Router>
      <Nav />
      
        <Switch>
        
        <Route exact path="/">
          
        <LandingPage />
        </Route>
        
        <Route path="/product">
        <SearchBar  search={searchbar} />
        <ProductList
         products={Products} />
          
        </Route>
       
        
      </Switch>
      
      </Router>
    )
  }


