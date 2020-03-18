import React from 'react';
import ReactDOM from 'react-dom';
import {  Router, Route,Switch,HashRouter} from 'react-router-dom';
import Not_found from './Not_found/Not_found';
import Test1 from './Test1/Test1';
// import { Router, Route} from 'react-router'
import './index.css';
import * as serviceWorker from './serviceWorker';
import { createBrowserHistory } from 'history'
import App from './App/App';
import Test from './test/Test';

//  ReactDOM.render(<App />, document.getElementById('root'));

const history = createBrowserHistory()

ReactDOM.render((
    <Router history={history}>
        <HashRouter>
            <Switch>
                <Route exact path="/" component={App} />
                <Route path="/test" component={Test} />
			<Route path="/test1" component={Test1} />
                <Route component={Not_found} />
            </Switch>
        </HashRouter>        
    </Router>
), document.getElementById('root'))


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();