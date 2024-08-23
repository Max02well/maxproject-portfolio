import React, { useState } from 'react';
import SectionTitle from '../../components/SectionTitle';
import { capstone } from '../../resources/capstone';
import luo from '../../assets/Maxwell_GogoCV-LUO.pdf';
import swahili from '../../assets/Maxwell_GogoCV-swahili.pdf';
import english from '../../assets/Maxwell_GogoCV-English.pdf';
import autoBio from '../../assets/AutoBio.pdf';
import essay from '../../assets/DEFORESTATION IN AFRICA.pdf';
import autoppt from '../../assets/AutoBio ppt.pptx'

function Capstone() {
  const [selectionItemIndex, setSelectionItemIndex] = useState(0);
  const [showFile, setShowFile] = useState(null);
  const [activeLanguage, setActiveLanguage] = useState(null);

  const handleViewFile = (fileUrl) => {
    setShowFile(fileUrl);
  };

  const handleLanguageClick = (language) => {
    setActiveLanguage(activeLanguage === language ? null : language);
  };

  return (
    <div>
      <SectionTitle title={'Capstone Project 4.2'} />
      <div className='flex py-10 gap-20 sm:flex-col'>
        <div className='sm:flex-row sm:overflow-scroll sm:w-full flex flex-col gap-7 w-1/3 border-l-2 border-teal-200'>
          {capstone.map((item, index) => (
            <div
              key={index}
              onClick={() => setSelectionItemIndex(index)}
              className='cursor-pointer'
            >
              <h1
                className={`text-xl px-7 ${
                  selectionItemIndex === index
                    ? `text-teal-200 border-teal-300 border-l-4 -ml-[3px] bg-[#4a5d87] py-3 sm:w-40`
                    : `text-white`
                }`}
              >
                {item.title}
              </h1>
            </div>
          ))}
        </div>

        <div className='flex flex-col gap-5 w-2/3'>
          {/* Video Player */}
          <iframe 
            width="100%" 
            height="315" 
            title="Abstract Videos"
            src={`https://www.youtube.com/embed/${capstone[selectionItemIndex].videoId}`} 
            allow="autoplay; encrypted-media" 
            allowFullScreen
            className='rounded-lg'
          ></iframe>

          <div className='text-center'>
            <h1 className='text-white text-2xl font-bold'>{capstone[selectionItemIndex].title}</h1>
            <h2 className='text-white text-xl'>{capstone[selectionItemIndex].lang}</h2>
          </div>

          {/* Clickable language sections */}
          <div className='flex flex-col gap-3'>
            <button 
              onClick={() => handleLanguageClick('english')}
              className='text-white text-2xl font-normal underline cursor-pointer'
            >
              English Abstract
            </button>
            {activeLanguage === 'english' && (
              <p className='text-white text-xl'>
                {capstone[selectionItemIndex].desc}
              </p>
            )}

            <button 
              onClick={() => handleLanguageClick('kiswahili')}
              className='text-white text-2xl font-normal underline cursor-pointer'
            >
              Kiswahili Abstract
            </button>
            {activeLanguage === 'kiswahili' && (
              <p className='text-white text-xl'>
                {capstone[selectionItemIndex].desc1}
              </p>
            )}

            <button 
              onClick={() => handleLanguageClick('luo')}
              className='text-white text-2xl font-normal underline cursor-pointer'
            >
              Luo Abstract
            </button>
            {activeLanguage === 'luo' && (
              <p className='text-white text-xl'>
                {capstone[selectionItemIndex].desc2}
              </p>
            )}
          </div>

          {/* PowerPoint Presentation Section */}
         
          
          
        </div>
        
      </div>
      <div className='items-center flex flex-col gap-3 mt-5'>
            <h2 className='text-white text-center text-xl font-bold'>PowerPoint Presentation:</h2>
            
            <a
              href={capstone[selectionItemIndex].ppt}
              download={`${capstone[selectionItemIndex].title}.pptx`}
              className='text-white bg-green-500 px-4 py-2 rounded text-center mt-2'
            >
              Download {capstone[selectionItemIndex].title} Powerpoint
            </a>
            <a
              href={capstone[selectionItemIndex].ppt}
              download={autoppt}
              className='text-white bg-green-500 px-4 py-2 rounded text-center mt-2'
            >
              Download Autobiography Powerpoint
            </a>
          </div>
      
 
      <div className='flex flex-col items-center gap-10 mt-12'>
        {/* Buttons for viewing PDF documents */}
        
        <h2 className='text-white text-center text-xl font-bold underline'>View Files:</h2>
        <div className='flex gap-7 flex-wrap justify-center'>
          <button
            onClick={() => handleViewFile(autoBio)}
            className='text-white bg-blue-500 px-4 py-2 rounded'
          >
            Autobiography (English)
          </button>
          <button
            onClick={() => handleViewFile(essay)}
            className='text-white bg-blue-500 px-4 py-2 rounded'
          >
            Photographic Essay
          </button>
        </div>
        
        {/* CV viewing buttons */}
        <div className='flex flex-col gap-2'>
          <div className='flex gap-2 justify-center'>
            <button
              onClick={() => handleViewFile(english)}
              className='text-white bg-blue-500 px-4 py-2 rounded'
            >
              English CV
            </button>
            <button
              onClick={() => handleViewFile(swahili)}
              className='text-white bg-blue-500 px-4 py-2 rounded'
            >
              Kiswahili CV
            </button>
            <button
              onClick={() => handleViewFile(luo)}
              className='text-white bg-blue-500 px-4 py-2 rounded'
            >
              Luo CV
            </button>
          </div>
        </div>

        {/* CV download links */}
        <div className='flex flex-col gap-2'>
          <h2 className='text-white text-xl font-semibold text-center'>Download CV:</h2>
          <div className='flex gap-2 justify-center'>
            <a
              href={english}
              download='Maxwell_GogoCV-English.pdf'
              className='text-white bg-green-500 px-4 py-2 rounded'
            >
              English
            </a>
            <a
              href={swahili}
              download='Maxwell_GogoCV-swahili.pdf'
              className='text-white bg-green-500 px-4 py-2 rounded'
            >
              Kiswahili
            </a>
            <a
              href={luo}
              download='Maxwell_GogoCV-LUO.pdf'
              className='text-white bg-green-500 px-4 py-2 rounded'
            >
              Luo
            </a>
          </div>
        </div>
      </div>

      {/* Modal for viewing files */}
      {showFile && (
        <div className='fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex items-center justify-center z-50'>
          <div className='bg-white p-4 rounded-lg w-full h-full'>
            <button
              onClick={() => setShowFile(null)}
              className='float-right text-black'
            >
              Close View
            </button>
            <iframe src={showFile} title='File Viewer' width='100%' height='100%' />
          </div>
        </div>
      )}
    </div>
  );
}

export default Capstone;
