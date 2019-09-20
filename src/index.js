import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, Link, browserHistory } from 'react-router'
import './index.css';
import * as serviceWorker from './serviceWorker';
import { createBrowserHistory } from 'history'
import App from './App/App';
import Test from './test/Test';
import Guru from './Guru/Guru';

// ReactDOM.render(<App />, document.getElementById('root'));

const history = createBrowserHistory()

ReactDOM.render((
    <Router history={history}>
        <Route exact path="/" component={App} />
        <Route path="/test" component={Test} />
		<Route path="/guru" component={Guru} />
    </Router>
), document.getElementById('root'))


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();