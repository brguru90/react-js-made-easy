
import React from 'react';
import './Test2.css';
import Page from './Test2Html.jsx'
var $ = require("jquery");

class Test2 extends React.Component {

    references = {
        test1: React.createRef()
    }
    test1 = () => {
        //@ts-ignore
        console.log($(this.references.test1.current).css({ "color": this.references.test1.current.value }))
    }

    constructor(props) {
        super(props);
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

export default Test2;
    