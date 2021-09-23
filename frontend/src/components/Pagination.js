import React from 'react'



export default function Pagination(props) {
    
    
    const numbers = [1, 2, 3, 4, 5,6];
    const listItems = numbers.map((number) =>
        <li key={number} ><button className="h-10 px-5 text-indigo-600 transition-colors duration-150 bg-white border border-r-0 border-indigo-600 focus:shadow-outline ">{number}</button></li>
    );
    return (



        
        <div>
            
            <nav aria-label="Page navigation">
                <ul  className="inline-flex">

                    <li><button onClick={props.previous} className="h-10 px-5 text-indigo-600 transition-colors duration-150 bg-white border border-r-0 border-indigo-600 rounded-l-lg focus:shadow-outline hover:bg-indigo-100 ">Prev</button></li>
                    {listItems}
                    <li><button onClick={props.next} className="h-10 px-5 text-indigo-600 transition-colors duration-150 bg-white border border-indigo-600 rounded-r-lg focus:shadow-outline hover:bg-indigo-100">Next</button></li>
                </ul>
            </nav>

        </div>
    )
}
