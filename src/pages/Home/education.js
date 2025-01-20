import React from 'react'
import SectionTitle from '../../components/SectionTitle'
import { schools } from '../../resources/School'

function Education() {
    const [selectionItemIndex, setSelectionItemIndex] = React.useState(0)
  return (
    <div>
        <SectionTitle title={'Education'} />
        <div className='flex py-10 gap-20 sm:flex-col'>
            <div className='sm:flex-row sm:overflow-scroll sm:w-full flex flex-col gap-7 w-1/3 border-l-2 border-teal-200'>
            {schools.map((school,index)=>(
                <div onClick={()=>{
                    setSelectionItemIndex(index)
                }} className='cursor-pointer'>
                    <h1 className={`text-xl px-7 ${selectionItemIndex === index ? `text-teal-200 border-teal-300 border-l-4 -ml-[3px] bg-[#4a5d87] py-3 sm:w-40` : `text-white`}`}>{school.date}</h1>
                </div>
            ))}
            </div>
        <div className='flex flex-col gap-5'>
        <h1 className='text-white text-2xl font-semibold'>{schools[selectionItemIndex].name}</h1>
        <h1 className='text-white text-xl'>{schools[selectionItemIndex].location}</h1>
        <p className='text-white text-xl'>{schools[selectionItemIndex].degree}</p>
        <p className='text-white text-xl'>{schools[selectionItemIndex].desc}</p>
        </div>
        
        </div>
      
    </div>
  )
}

export default Education
