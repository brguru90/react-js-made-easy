import sys,os,re

def js(name):
    content='''
import React from 'react';
import './'''+name+'''.css';
import page from './'''+name+'''Html'

class '''+name+''' extends React.Component {

    constructor(props) {
        super(props);
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

export default '''+name+''';
    '''
    f = open(component+"/"+component+".js", "w")
    f.write(content)
    f.close()

def html(name):
    content='''
import React from 'react';
let page=

<div className="'''+name+'''">
    <h1>Welcome</h1>
    <h2>'''+name+'''</h2>
</div>

export default page;
    '''
    f = open(component+"/"+component+".Html.js", "w")
    f.write(content)
    f.close()

def css(name):
    content='''
.'''+name+''' {
    text-align: center;
}
'''
    f = open(component+"/"+component+".css", "w")
    f.write(content)
    f.close()

def add_route(name):
    f = open("index.js", "r+")
    content=f.read()
    if os.path.exists('index_bak.js'):
        os.remove('index_bak.js')
    f2 = open("index_bak.js", "w")
    f2.write(content)
    f2.close()

for i in range(1,len(sys.argv)): 	
    component=sys.argv[i]
    os.mkdir(component)
    js(component)
    html(component)
    css(component)

   