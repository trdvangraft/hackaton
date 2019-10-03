import React, { Component } from 'react';
import TextBubble from "./components/TextBubble";
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      userMessage: '',
      conversation: [
        {
          _id: 1,
          text: `Hi! I am Cortana from Aalto university.\n\nHow may I help you with today?`,
          user: 'ai',
          type: 'text',
        }
      ],
    };
  }

  componentDidMount() {

  }

  handleChange = event => this.setState({ userMessage: event.target.value });

  handleSubmit = event => {
    event.preventDefault();
    if (!this.state.userMessage.trim()) return;

    const msg = {
      text: this.state.userMessage,
      user: 'human',
      type: 'text',
    };

    this.setState({
      conversation: [...this.state.conversation, msg],
    });

    fetch('http://localhost:5000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: this.state.userMessage,
        metadata: []
      }),
    })
      .then(resp => resp.json())
      .then(result => {
        const msg = {
          user: 'ai',
          ...result
        }
        // handle the parsing here
        this.setState(prevState => {
          return {
            ...prevState,
            conversation: [...prevState.conversation, msg],
          }
        })
      });

    this.setState({ userMessage: '' });
  };

  render() {
    

    const chat = this.state.conversation.map(({ type, text, user }, index) => {
      switch (type) {
        case 'text':
          return <TextBubble text={text} className={user} i={index} />
        default:
          console.log(type)
      }
    });

    return (
      <div>
        <div className="chat-window">
          <div className="conversation-view">{chat}</div>
          <div className="message-box">
            <form onSubmit={this.handleSubmit}>
              <input
                value={this.state.userMessage}
                onChange={this.handleChange}
                className="text-input"
                type="text"
                autoFocus
                placeholder="Type your message and hit Enter to send"
              />
            </form>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
