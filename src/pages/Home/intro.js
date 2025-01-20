import React from 'react'

function Intro() {
  return (
    <div className='h-[100vh] bg-primary flex flex-col items-start justify-center gap-7 py-10 '>
        <h1 className='text-white text-2xl '>Hello,I am</h1>
        <h1 className='text-red-300 sm:text-2xl text-5xl font-semibold'>Maxwell Gogo</h1>
        <h1 className='text-white sm:text-2xl text-4xl font-semibold'>Software Developer</h1>
        <p className='text-white text-xl w-2/3'>I am a highly driven and detail-oriented Software developer with strong foundation in website and mobile programming,computer networks,system monitoring and database management with both NoSQL and SQL Databases. I am also proficient in containerization, orchestration and CI/CD pipelines using Docker and Kubernetes.</p>
        <a href="#projects">
        <button className='border-2 border-blue-300 text-white px-10 py-3 rounded'>
          See Projects
        </button>
      </a>
      
    </div>
  )
}

export default Intro
