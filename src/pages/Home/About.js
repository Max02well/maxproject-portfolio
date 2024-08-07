import React from 'react'
import SectionTitle from '../../components/SectionTitle'
import logo from '../../assets/IMG_9313.jpg'
import luo from '../../assets/Maxwell_GogoCV-LUO.pdf'
import swahili from '../../assets/Maxwell_GogoCV-swahili.pdf'
import english from '../../assets/Maxwell_GogoCV-English.pdf'

function About() {
    const skills =[
        'React Native',
        'React',
        'Node.js',
        'Express.js',
        'MongoDB',
        'C#',
        'Figma',
    ]
  return (
    <div>
        <SectionTitle title={'About Me'} />
        <div className='flex w-full gap-10 items-center sm:flex-col'>
            <div className='w-1/2 h-[50vh]'>
                <img src={logo} alt='about' className='w-full h-full object-contain sm:w-full rounded-3xl' />
            </div>
            <div className='w-1/2 flex flex-col gap-5 sm:w-full'>
                <h1 className='text-white text-4xl font-semibold'>Who am I?</h1>
                <p className='text-white text-xl'>Hello,My name is Maxwell Gogo.I am a fourth year student at Dedan Kimathi University of Technology,Nyeri-Kenya.I am pursuing Bachelor of Science in Information Technology and currently am in my last semester.</p>
                <p className='text-secondary-100 text-xl'>I am passionate about mobile development with React Native and as well UI/UX design which puts the user of an app as the center of every software development that ensures they have an interesting experience with the app.</p>
            </div>
        </div>
        <div className='py-5 mt-5' >
            <h1 className='text-green-300 text-xl'>These are the technologies I've been working with recently:</h1>
            <div className='flex flex-wrap gap-10 mt-5'>
            {skills.map((skill,index)=>(
                <div key={index} className='flex items-center gap-5 border border-green-200 py-3 px-7 rounded'>
                    <h1 className='text-white text-lg'>{skill}</h1>
                    
                </div>
            ))}  
            </div>
            <div className='flex gap-7 flex-row mt-12 items-center justify-center'>
                <a href={english} download="Resume">
                    <button className='text-white bg-blue-500 px-4 py-2 rounded'>Download CV(English)</button>
                </a>
                <a href={swahili} download="Resume">
                    <button className='text-white bg-blue-500 px-4 py-2 rounded'>Download CV(Kiswahili)</button>
                </a>
                <a href={luo} download="Resume">
                    <button className='text-white bg-blue-500 px-4 py-2 rounded'>Download CV(Luo)</button>
                </a>
            </div>
        </div>
      
    </div>
  )
}

export default About
