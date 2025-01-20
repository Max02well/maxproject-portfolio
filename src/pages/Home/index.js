import React from 'react'
import Header from '../../components/Header'
import Intro from './intro'
import About from './About'
import Education from './education'
import Projects from './project'
import Contact from './contact'
import Footer from './footer'
import SocialHandles from './social'
import Experience from './Experience'


export default function Home() {
  return (
    <div>
     <Header />
     <div className='bg-primary px-40 sm:px-5'>
     <Intro />
     <About />
     <Education />
     <Projects />
     <Experience />
     <Contact />
     <SocialHandles />
     <Footer />
     </div>
    </div>
  )
}
