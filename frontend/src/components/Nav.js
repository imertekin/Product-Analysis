import React from 'react'
import { BrowserRouter, Link } from 'react-router-dom'

export default function Nav() {
    return (
        <div>
             <nav className="w-full p-2 mt-0 bg-gray-800">
		<div className="container flex flex-wrap items-center mx-auto">
			<div className="flex justify-center w-full font-extrabold text-white md:w-1/2 md:justify-start">
                <Link className="text-white no-underline hover:text-white hover:no-underline" to="/" >
				
					<span className="pl-2 text-2xl"><i className="em em-grinning"></i> Product Analysis</span>
				</Link>
			</div>
            
			<div className="flex content-center justify-between w-full pt-2 md:w-1/2 md:justify-end">
				<ul className="flex items-center justify-between flex-1 list-reset md:flex-none">
					<li className="mr-3">
						<BrowserRouter forceRefresh>
						<Link  className="inline-block px-4 py-2 text-white no-underline" to="/product"> Products</Link>
						</BrowserRouter>
					</li>
					<li className="mr-3">
					<Link className="inline-block px-4 py-2 text-white no-underline" to="/">Link</Link>
					</li>
					<li className="mr-3">
					<Link className="inline-block px-4 py-2 text-white no-underline" to="/">Link</Link>
					</li>
					<li className="mr-3">
					<Link className="inline-block px-4 py-2 text-white no-underline" to="/">Link</Link>
					</li>
				</ul>
			</div>
		</div>
	</nav>
            
        </div>
    )
}
