import React from 'react'

function Loader() {
  return (
    <div className='h-screen flex items-center bg-primary justify-center fixed inset-0'>
        <div className='flex gap-5 text-6xl sm:text-3xl font-semibold'>
            <h1 className='text-red-300 m'>M</h1>
            <h1 className='text-white a'>A</h1>
            <h1 className='text-teal-200 g'>G</h1>

        </div>
      
    </div>
  )
}

export default Loader
