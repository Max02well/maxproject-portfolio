import React from 'react'

function SocialHandles() {
  return (
    <div className='fixed left-0 bottom-0 sm:static px-10'>
        <div className='flex flex-col items-center'>
      <div className='flex flex-col gap-3 sm:flex-row'>
        <a href='https://www.linkedin.com/in/maxwell-gogo-2015a0231/'>
      <i class="ri-linkedin-box-fill text-white text-xl">
      </i></a>
      <a href='https://mail.google.com/mail'>
      <i class="ri-mail-fill  text-white text-xl"></i>
      </a>
      <a href='https://github.com/Max02well'>
      <i class="ri-github-fill  text-white text-xl"></i>
      </a>
      <a href='https://x.com/gogo1_onyango'>
      <i class="ri-twitter-x-fill text-white text-xl"></i>
      </a>
      </div>
      <div className='w-[1px] h-52 bg-[#73caa9] sm:hidden'></div>
      </div>
    </div>
  )
}

export default SocialHandles
