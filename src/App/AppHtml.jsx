import React from 'react';
import { Link } from 'react-router-dom';

let Page = function (props) {
    let _this = props._this 
    let references = props.references
    return (
        <div className="App">
            <h1>Welcome</h1>
            <h2>App</h2>
            <Link to='/test'>Test</Link><br />
            <input type="text" placeholder="Type color name" onChange={_this.test1} ref={references.test1}/> <br />
            <input type="text" placeholder="Type color name" onChange={_this.test2} ref={references.test2}/> 
        </div>
    )
}





export default Page;