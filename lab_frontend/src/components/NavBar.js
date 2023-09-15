import React from 'react'
import { useState, useEffect } from "react";
import { CreateTitleButton } from './CreateTitleButton';


export const NavBar = () => {
    const [Titles, setTitles] = useState([]);
    const getTitles = async () => {
      const response = await fetch("http://127.0.0.1:8000/titles-list/");
      const data = await response.json();
      console.log(data);
      setTitles(data);
    };

    useEffect(() => {
      getTitles();
    }, []);

    const hello = () => {
        console.log(Titles)
    }
    return (
      <>
        <div className="navbar bg-red-300  rounded-lg mt-2 ">
          <div className="flex-1">
            <a className="btn bg-slate-400 normal-case text-xl text-gray-700">
              lab app
            </a>
          </div>
          <div className='mr-4'>
            <CreateTitleButton />
          </div>

          <div className="flex-none">
            <div className="dropdown dropdown-end">
              <label tabIndex={0} className="btn m-1 bg-black">
                titles
              </label>
              <ul
                tabIndex={0}
                className="dropdown-content z-[1] menu p-2 shadow rounded-box w-52 bg-black"
              >
                {Titles.map((title, index) => (
                  <li>
                    <a key={index}>{title.title}</a>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </>
    );
}
