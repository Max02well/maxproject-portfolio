import React, { useState } from 'react';
import SectionTitle from '../../components/SectionTitle';
import { capstone } from '../../resources/capstone';
import luo from '../../assets/Maxwell_GogoCV-LUO.pdf';
import swahili from '../../assets/Maxwell_GogoCV-swahili.pdf';
import english from '../../assets/Maxwell_GogoCV-English.pdf';
import autoBio from '../../assets/AutoBio.pdf';

function Capstone() {
  const [selectionItemIndex, setSelectionItemIndex] = useState(0);
  const [showPdf, setShowPdf] = useState(null);

  const handleViewPdf = (pdfUrl) => {
    setShowPdf(pdfUrl);
  };

  return (
    <div>
      <SectionTitle title={'Capstone Project 4.2'} />
      <div className='flex py-10 gap-20 sm:flex-col'>
        <div className='sm:flex-row sm:overflow-scroll sm:w-full flex flex-col gap-7 w-1/3 border-l-2 border-teal-200'>
          {capstone.map((capstone, index) => (
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
                {capstone.title}
              </h1>
            </div>
          ))}
        </div>
        <div className='flex flex-col gap-5'>
          <h1 className='text-white text-2xl font-semibold'>
            {capstone[selectionItemIndex].title}
          </h1>
          <h1 className='text-white text-xl'>
            {capstone[selectionItemIndex].lang}
          </h1>
          <p className='text-white text-xl'>
            {capstone[selectionItemIndex].desc}
          </p>
        </div>
      </div>
      <div className='flex gap-7 flex-wrap mt-12 items-center justify-center'>
        <button
          onClick={() => handleViewPdf(autoBio)}
          className='text-white bg-blue-500 px-4 py-2 rounded'
        >
          View Autobiography (English)
        </button>
        <button
          onClick={() => handleViewPdf(english)}
          className='text-white bg-blue-500 px-4 py-2 rounded'
        >
          View CV (English)
        </button>
        <a
          href={english}
          download='Maxwell_GogoCV-English.pdf'
          className='text-white bg-blue-500 px-4 py-2 rounded'
        >
          Download CV (English)
        </a>
        <a
          href={swahili}
          download='Maxwell_GogoCV-swahili.pdf'
          className='text-white bg-blue-500 px-4 py-2 rounded'
        >
          Download CV (Kiswahili)
        </a>
        <a
          href={luo}
          download='Maxwell_GogoCV-LUO.pdf'
          className='text-white bg-blue-500 px-4 py-2 rounded'
        >
          Download CV (Luo)
        </a>
      </div>
      {showPdf && (
        <div className='fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex items-center justify-center z-50'>
          <div className='bg-white p-2 rounded-lg w-full h-full'>
            <button
              onClick={() => setShowPdf(null)}
              className='float-right text-black'
            >
              Close
            </button>
            <iframe src={showPdf} title='PDF Viewer' width='100%' height='100%' />
          </div>
        </div>
      )}
    </div>
  );
}

export default Capstone;
