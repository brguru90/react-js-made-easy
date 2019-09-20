import React from 'react';
import './App.css';
import page from './AppHtml'


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
