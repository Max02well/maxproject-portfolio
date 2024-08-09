import React from 'react'
import SectionTitle from '../../components/SectionTitle'
import logo from '../../assets/IMG_9313.jpg'


function About() {

    const skills = [
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
                <div className='w-1/2 h-[50vh] sm:w-full'>
                    <img src={logo} alt='about' className='w-full h-full object-contain rounded-3xl' loading="lazy" />
                </div>
                <div className='w-1/2 flex flex-col gap-5 sm:w-full'>
                    <h1 className='text-white text-4xl font-semibold'>Who am I?</h1>
                    <p className='text-white text-xl'>Hello, My name is Maxwell Gogo. I am a fourth year student at Dedan Kimathi University of Technology, Nyeri-Kenya. I am pursuing Bachelor of Science in Information Technology and currently am in my last semester.</p>
                    <p className='text-secondary-100 text-xl'>I am passionate about mobile development with React Native and as well UI/UX design which puts the user of an app as the center of every software development that ensures they have an interesting experience with the app.</p>
                </div>
            </div>
            <div className='py-5 mt-5'>
                <h1 className='text-green-300 text-xl'>These are the technologies I've been working with recently:</h1>
                <div className='flex flex-wrap gap-10 mt-5'>
                    {skills.map((skill, index) => (
                        <div key={index} className='flex items-center gap-5 border border-green-200 py-3 px-7 rounded'>
                            <h1 className='text-white text-lg'>{skill}</h1>
                        </div>
                    ))}
                </div>
              </div>
            </div>
    )
}

export default About