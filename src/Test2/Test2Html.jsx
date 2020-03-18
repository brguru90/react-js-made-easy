
import React from 'react';
import { Link } from 'react-router-dom';

let Page = function (props) {
    let _this = props._this 
    let references = props.references
    return (
        <div className="Test2">
            <h1>Welcome</h1>
            <h2>Test2</h2>
            <Link to='/'>App</Link><br />
            <input type="text" placeholder="Type color name" onChange={_this.test1} ref={references.test1}/>
        </div>
    )
}

export default Page;
    