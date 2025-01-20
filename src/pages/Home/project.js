import React from 'react'
import SectionTitle from '../../components/SectionTitle'
import { projects } from '../../resources/Projects'


function Projects() {
    const [selectionItemIndex, setSelectionItemIndex] = React.useState(0)
  return (
    <div id='projects'>
        <SectionTitle title={'Projects'} />
        <div className='flex py-10 gap-20 sm:flex-col'>
            <div className='sm:flex-row sm:overflow-scroll sm:w-full flex flex-col gap-7 w-1/3 border-l-2 border-teal-200'>
            {projects.map((project,index)=>(
                <div onClick={()=>{
                    setSelectionItemIndex(index)
                }} className='cursor-pointer'>
                    <h1 className={`text-xl px-5 ${selectionItemIndex === index ? `text-teal-200 border-teal-300 border-l-4 -ml-[3px] bg-[#4a5d87] py-3 sm:w-40` : `text-white`}`}>{project.title}</h1>
                </div>
            ))}
            </div>
           
        <div  className='flex flex-col gap-5'>
        <h1 className='text-secondary-200 text-2xl font-semibold'>{projects[selectionItemIndex].title}</h1>
        <h1 className='text-white text-xl'>{projects[selectionItemIndex].desc}</h1>
       <p className='text-white text-xl'>Technologies Used:{projects[selectionItemIndex].technologies}</p>
        </div>
        
        </div>
      
    </div>
  )
}

export default Projects
