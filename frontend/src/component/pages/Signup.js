import React, { useState } from 'react'
import axios from 'axios'
export const Signup = () => {
    const [username , setUsername] =useState('')
    const [password , setPassword] =useState('')
    const [confirm , setConfirm] =useState('')
    const [image , setImage] = useState(null)
    const sendHandler = async (e)=>{
        await e.preventDefault()
        const form = new FormData() 
        await form.append('username',username)
        await form.append('password',password)
        await form.append('profile_pic',image,`${username}-pic.${image.type.split('/')[1]}`)
        await console.log(form.get('profile_pic'))
        await axios({
            method:'POST',
            url:'http://127.0.0.1:8000/api/profiles/',
            data:form
        })
    }
    const imageHandler = (e)=>{
        setImage(e.target.files[0])
    }
  return (
    <div>
        <h1>sign up</h1>
        <form onSubmit={sendHandler}>
            <input type='file' onChange={imageHandler}/>
            <input type='text' placeholder='username' value={username} onChange={(e)=>{setUsername(e.target.value)}}/>
            <input type='password' placeholder='password' value={password} onChange={(e)=>{setPassword(e.target.value)}}/>
            <input type='password' placeholder='confirm' value={confirm} onChange={(e)=>{setConfirm(e.target.value)}}/>
            <button>sign up !</button>
        </form>
    </div>
  )
}