import React from 'react'

export const NavBar = () => {
  return (
    <>
      <div className="navbar bg-red-300  rounded-lg mt-2 ">
        <div className="flex-1">
          <a className="btn bg-slate-400 normal-case text-xl text-gray-700">daisyUI</a>
        </div>
        <div className="flex-none">
          <button className="btn btn-square btn-ghost bg-black hover:bg-slate-600 ">

            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              className="inline-block w-5 h-5 stroke-current"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"
              ></path>
            </svg>
          </button>
        </div>
      </div>
    </>
  );
}
