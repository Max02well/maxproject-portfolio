import React from 'react'

function SectionTitle({title}) {
  return (
    <div className='flex gap-10 items-center py-10'>
        <h1 className='text-white text-2xl'>
            {title}</h1>
            <div className='w-60 h-[1px] bg-green-200'></div>
    </div>
  )
}

export default SectionTitle
