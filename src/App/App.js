import React from 'react';
import './App.scss';
import Page from './AppHtml.jsx'
var $ = require("jquery");


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { color: "red" };
  }

  references = {
    test1: React.createRef(),
    test2: React.createRef()
   }

 test1 = () => {
  //@ts-ignore
  console.log($(this.references.test1.current).css({ "color": this.references.test1.current.value }))
}
 test2 = () => {
   //@ts-ignore
   console.log($(this.references.test2.current).css({ "background-color": this.references.test2.current.value }))
   //@ts-ignore
   console.log(this.references.test2.current.value)
 }

  componentDidMount() {

  }
  componentDidUpdate() {

  }
  render() {
    return (
      <Page _this={this} references={this.references} /> 
    )
  }
}

export default App;
