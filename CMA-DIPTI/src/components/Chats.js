import React, { useRef, useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { ChatEngine} from 'react-chat-engine';
import { auth } from '../firebase';
import { useAuth } from '../context/AuthContext';
import axios from 'axios';


const Chats = () => {
    
    const didMountRef = useRef(false);
    const history = useHistory();
    const { user } = useAuth();
    const [loading, setLoading] = useState(true);
   
    console.log('fetched user',user);


    const handleLogout = async () => {
        await auth.signOut();
        history.push('/');
    }
    
    async function getFile(url) {
        let response = await fetch(url);
        let data = await response.blob();
        return new File([data], "userPhoto.jpg", { type: 'image/jpeg'});
    }

    useEffect(() => { 
        if (!didMountRef.current){
                didMountRef.current = true
            }

        if(!user || user===null) {
            history.push('/');
            return
        }

        axios.get('https://api.chatengine.io/users/me/', {
            headers: {
                "project-id": process.env.REACT_APP_CHAT_ENGINE_ID,
                "user-name": user.email,
                "user-secret": user.uid
                }
            })
        .then (() => {setLoading(false);})
        .catch(e => {
            let formdata = new FormData();
            formdata.append('email', user.email)
            formdata.append('username', user.email)
            formdata.append('secret', user.uid)

            getFile(user.photoURL)
                .then((avatar) => {
                    formdata.append('avatar', avatar, avatar.name)

                    axios.post('https://api.chatengine.io/users/',
                        formdata,
                        { headers: { "private-key": process.env.REACT_APP_CHAT_ENGINE_KEY}}
                    )
                    .then(() => {setLoading(false)})
                    .catch(e => console.log('e',e.response))
                })
             });
           
    }, [user, history]);

    
    if(!user || loading) return 'Loading...';

    return (
        <div className='chats-page'>
            <div className='nav-bar'>
                <div className='logo-tab'>
                    Unichat
                </div>
                <div onClick={handleLogout} className='logout-tab'>
                    logout
                </div>
            </div>
            
                    <ChatEngine    
                        //calc(height - header)
                        offset={6}
                        height="calc(100vh -66px)"
                        projectID = {process.env.REACT_APP_CHAT_ENGINE_ID}
                        userName= {user.email}
                        userSecret = {user.uid}
                        chatId = {user.uid}

                        onNewMessage={(chatId, message) => {   
                        console.log(chatId,message);
                       
                        let currentTime = new Date(message.created.toLocaleString('en-US', {
                            hour: 'numeric',
                            minute: 'numeric',
                            day: 'numeric',
                            month: 'short',
                            year: 'numeric',
                            localeMatcher: "best fit",
                             }
                        ))
                        message.text = message.text + "\n" + currentTime;
                        console.log(message.text)
                        }}
                        />
            
        </div>
    );
};

export default Chats;
