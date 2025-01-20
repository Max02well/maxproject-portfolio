import React from 'react';
import SectionTitle from '../../components/SectionTitle';

function Experience() {
  return (
    <div>
      <SectionTitle title={'Work Experience'} />
        <div className='flex py-10 gap-20 sm:flex-col'>
            <div className='sm:flex-row sm:overflow-scroll sm:w-full flex flex-col gap-7 w-1/3 border-l-2 border-teal-200'>
            <div className=''>
                <h1 className='text-xl px-5 text-white'>System Administrator Intern</h1>
            </div>
            </div>
            <div className='flex flex-col gap-5'>
            <h1 className='text-white text-2xl font-semibold'>Sept-Nov. 2024</h1>
            <h1 className='text-white text-xl'>I worked as a system administrator intern at Keystone DT Sacco Ltd where I was responsible for managing the company computer system, network infrastructure,system maintenance & update,executing cybersecurity policies,disaster management through data backup,security and alert strategies,providing technical support to the staff.</h1>
            <p className='text-white text-xl'>Technologies Used: Agile,DevOps Tools-Docker,Kubernetes,GitHub,Vanguard Financials Software</p>
            </div>
            </div>


    </div>
  );
}

export default Experience;