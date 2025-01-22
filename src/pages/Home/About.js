import React from 'react'
import SectionTitle from '../../components/SectionTitle'
import logo from '../../assets/mygrad.JPG'



function About() {

    const skills = [
        'React Native',
        'React',
        'Node.js',
        'Docker',
        'Kubernetes',
        'Git',
        'Terraform',
        'Python',
        'Express.js',
        'MongoDB',
        'MySQL',
        'Tailwind CSS',
        'C#',
        'Figma',
        
    ]

    

    return (
        <div>
            <SectionTitle title={'About Me'} />
            <div className='flex w-full gap-10 items-center sm:flex-col'>
                <div className='w-1/2 h-[70vh] sm:w-full'>
                    <img src={logo} alt='about' className='w-[100vh] h-[70vh] object-contain rounded-3xl' loading="lazy" />
                </div>
                <div className='w-1/2 flex flex-col gap-5 sm:w-full'>
                    <h1 className='text-white text-4xl font-semibold'>Who am I?</h1>
                    <p className='text-white text-xl'>I am a software developer and an IT graduate of Dedan Kimathi University of Technology, Nyeri-Kenya.</p>
                    <p className='text-secondary-100 text-lg'>I am passionate about System support and monitoring, proficient in DevOps tools like Docker,Kubernetes and GitHub.I also have adequate knowledge in mobile app development with React Native,programming with Python and JavaScript and UI/UX Design which ensures users have a responsive and intuitive interfaces for their apps.</p>
                </div>
            </div>
            <div className='py-5 mt-5'>
                <h1 className='text-green-300 text-xl'>These are the technologies I've been working with recently:</h1>
                <div className='flex flex-wrap gap-10 mt-5'>
                    {skills.map((skill, index) => (
                         <div className="bg-gray-500 px-4 py-2 rounded-lg hover:bg-green-400 transition-colors duration-300 ease-in-out transform hover:scale-105 shadow-2xl">                       
                            <h1 className='text-slate-200 text-base hover:text-white font-medium'>{skill}</h1>
                        </div>
                    ))}
                </div>
              </div>
            </div>
    )
}

export default About