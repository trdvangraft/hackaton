import React from 'react'

const TextBubble = ({ text, i, className }) => {
    return (
        <div key={`${className}-${i}`} className={`${className} chat-bubble`}>
            <span className="chat-content">{text}</span>
        </div>
    );
};

export default TextBubble