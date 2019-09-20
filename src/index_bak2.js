import React from 'react';
import ReactDOM from 'react-dom';
import {  Router, Route,Switch,BrowserRouter} from 'react-router-dom';
import Guru2 from './Guru2/Guru2';
// import { Router, Route} from 'react-router'
import './index.css';
import * as serviceWorker from './serviceWorker';
import { createBrowserHistory } from 'history'
import App from './App/App';
import Test from './test/Test';

//  ReactDOM.render(<App />, document.getElementById('root'));

const history = createBrowserHistory()

ReactDOM.render((
    <BrowserRouter>
    <Router history={history}>
        <Switch>
            <Route exact path="/" component={App} />
            <Route path="/test" component={Test} />
			<Route path="/guru2" component={Guru2} />
        </Switch>
    </Router>
    </BrowserRouter>
), document.getElementById('root'))


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();