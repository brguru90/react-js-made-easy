import sys,os,re
import shutil
from html import escape

path="./src/"

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
    f = open(path+component+"/"+component+".js", "w")
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
    f = open(path+component+"/"+component+"Html.js", "w")
    f.write(content)
    f.close()

def css(name):
    content='''
.'''+name+''' {
    text-align: center;
}
'''
    f = open(path+component+"/"+component+".css", "w")
    f.write(content)
    f.close()

def add_route(name):
    f = open(path+"index.js", "r")
    content=f.read()
    if os.path.exists(path+'index_bak.js'):
        os.remove(path+'index_bak.js')
    f2 = open(path+"index_bak.js", "w")
    f2.write(content)
    f2.close()

    line_arr=content.split("\n")
    line_count=0
    for line in line_arr:
        if not re.search("^import",line):
            line_arr.insert(line_count,"import "+name+" from './"+name+"/"+name+"';")
            break
        line_count+=1
    line_count=0;
    found=False
    for line in line_arr:
        if re.search(escape("<Route path="),escape(line)):
            found=True
        else:
            if found==True:
                line_arr.insert(line_count,"\t\t<Route path=\"/"+name.lower()+"\" component={"+name+"} />")
                break
        line_count+=1
    f.close()
    f = open(path+"index.js", "w")
    f.write("\n".join(line_arr))
    f.close()

for i in range(1,len(sys.argv)): 	
    component=sys.argv[i].capitalize()
    if os.path.exists(path+component):
        shutil.rmtree(path+component)
    os.mkdir(path+component)
    js(component)
    html(component)
    css(component)
    add_route(component)

   