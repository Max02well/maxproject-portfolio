import React from 'react'

function Footer() {
  const currentYear = new Date().getFullYear();
  return (
    <div className='py-8'>
      <div className='bg-gray-700 h-[1px] w-full  flex items-center justify-center'>
        </div>
        <div className='flex items-center justify-center flex-col mt-7'>
            <h1 className='text-white'>
              &copy; {currentYear} 
            </h1>
            <h1 className='text-white'>
                <span className='text-white'>Developed by Maxwell Gogo</span>
            </h1>

        </div>
    </div>
  )
}

export default Footer
