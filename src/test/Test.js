import React from 'react';
import './Test.css';
import page from './TestHtml'

// function App() {
//   return (
//     <h1>Hi</h1>
//   );
// }

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { color: "red" };
  }
  componentDidMount() {

  }
  componentDidUpdate() {

  }
  render() {
    return (
      page
    )
  }
}

export default App;
