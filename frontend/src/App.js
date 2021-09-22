import ProductList from "./components/ProductList";
import SearchBar from "./components/SearchBar";
import React, { Component } from 'react'
import axios from "axios"
import Pagination from "./components/Pagination";





export default class App extends Component {
  state={
    Products : [],
      searchQuery:"",
      offset:0,
      next:"",
      previous:"",
      
        

  }


  async componentDidMount(){

    const res = await axios.get("http://127.0.0.1:8000/api/product/")
    
    this.setState({Products:res.data.results})
    this.setState({next:res.data.next})
    this.setState({previous:res.data.previous})
    
   
 }
 
  next=async()=>{
    if(this.state.next!==null){
    const res = await axios.get(this.state.next)
    this.setState({next:res.data.next})
    this.setState({previous:res.data.previous})
    console.log(this.state.next)
    this.setState({Products:res.data.results})
    }
    
  
   else {console.log("null")
   
  
  
  } 
    
    }
  
    
    

  previous= async()=>{
    if(this.state.previous!==null){
      const res = await axios.get(this.state.previous)
      this.setState({next:res.data.next})
      this.setState({previous:res.data.previous})
      console.log(this.state.previous)
      this.setState({Products:res.data.results})
      }
      
    
     else {console.log("null")

  }
}



  searchbar=async (e)=>{
    e.preventDefault()
    const ip=document.getElementById('test')
    const res = await axios.get("http://127.0.0.1:8000/api/product/?search="+ip.value)
    this.setState({next:res.data.next})
    this.setState({previous:res.data.previous})
    this.setState({Products:res.data.results})
    ip.value=""
    console.log(this.state.next)
    
  }




 
    



  render() {
    
   
    return (
      
      <div>
        
        <SearchBar  search={this.searchbar}  />
        <ProductList
         products={this.state.Products} />
        <div className="flex justify-center py-4">
        <Pagination next={this.next} previous={this.previous} />
        </div>
        
        
      </div>
    )
  }
}

