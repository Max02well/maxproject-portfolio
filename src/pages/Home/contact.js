import React from 'react'
import SectionTitle from '../../components/SectionTitle'

function Contact() {
    const user = {
        Name: 'Maxwell Gogo',
        Email: 'maxarmstronggogo@gmail.com',
        Call:'0703603949'
      
    }
  return (
    <div>
      <SectionTitle title='Say Hello' />
      <div className='flex flex-col gap-3 items-center justify-between'>
        <h1 className='text-2xl text-secondary-200 text-semibold'>Contact Details</h1>
        {Object.keys(user).map((key,index)=>(
            <h1 key={index} className='text-white text-xl'><span>{key}: {user[key]}</span></h1>
        ))}
        
        </div>
    </div>
  )
}

export default Contact
