import React, { useEffect, useState } from 'react';
import { auth } from './firebaseConfig';

const Notes = () => {
    const [userName, setUserName] = useState('');

    useEffect(() => {
        if (auth.currentUser) {
            setUserName(auth.currentUser.displayName);
        }
    }, []);

    return (
        <div className="Notes" style={{ textAlign: 'center', marginTop: '100px' }}>
            <h1>Here are your notes, {userName}</h1>
        </div>
    );
};

export default Notes;