import React from 'react'

function Intro() {
  return (
    <div className='h-[100vh] bg-primary flex flex-col items-start justify-center gap-7 py-10 '>
        <h1 className='text-white text-2xl '>Hello,I am</h1>
        <h1 className='text-red-300 sm:text-3xl text-7xl font-semibold'>Maxwell Gogo</h1>
        <h1 className='text-white sm:text-3xl text-6xl font-semibold'>Software Developer</h1>
        <p className='text-white text-2xl w-2/3'>I am a software developer with a passion for building mobile applications with React Native.Also I am very interested in UI/UX Design which aims at building intuitive interfaces for app users.</p>
        <a href="#projects">
        <button className='border-2 border-blue-300 text-white px-10 py-3 rounded'>
          See Projects
        </button>
      </a>
      
    </div>
  )
}

export default Intro
