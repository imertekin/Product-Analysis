import React, { Component } from 'react'



export default class SearchBar extends Component {


    
  


    render() {
        return (
            <div>
                <div className="bg-gray-800" >
                    <form  >
                    <div className="container flex items-center justify-center p-4 ">
                        <div className="relative">
                            <div className="absolute top-4 left-3"> <i className="z-20 text-gray-400 fa fa-search hover:text-gray-500"></i> </div>
                            <input  type="text" id="test" className="z-0 pl-8 pr-24 rounded-lg h-14 w-96 focus:shadow focus:outline-none" placeholder="Search anything..." />
                            <div className="absolute pl-6 top-2 right-2"> <button onClick={this.props.search} className="w-20 h-10 text-white bg-red-500 rounded-lg hover:bg-red-600">Search</button> </div>
                        </div>
                    </div>
                    </form>
                </div>

            </div>
        )
    }
}
