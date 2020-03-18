import sys,os,re
import shutil
from html import escape

path="./src/"

# -----------------------------------------JS--------------------------------------
def js(name):
    content='''
import React from 'react';
import './'''+name+'''.scss';
import Page from './'''+name+'''Html.jsx'
var $ = require("jquery");

class '''+name+''' extends React.Component {

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

export default '''+name+''';
    '''
    w_path=path+component+"/"+component+".js"
    print(w_path)
    f = open(w_path, "w")
    f.write(content)
    f.close()

# -----------------------------------------HTML--------------------------------------
def html(name):
    content='''
import React from 'react';
import { Link } from 'react-router-dom';

let Page = function (props) {
    let _this = props._this 
    let references = props.references
    return (
        <div className="'''+name+'''">
            <h1>Welcome</h1>
            <h2>'''+name+'''</h2>
            <Link to='/'>App</Link><br />
            <input type="text" placeholder="Type color name" onChange={_this.test1} ref={references.test1}/>
        </div>
    )
}

export default Page;
    '''
    w_path=path+component+"/"+component+"Html.jsx"
    print(w_path)
    f = open(w_path, "w")
    f.write(content)
    f.close()

# -----------------------------------------CSS--------------------------------------
def css(name):
    content='''
.'''+name+''' {
    text-align: center;
}
'''
    w_path=path+component+"/"+component+".scss"
    print(w_path)
    f = open(w_path, "w")
    f.write(content)
    f.close()

# -----------------------------------------ROUTE--------------------------------------
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
                line_arr.insert(line_count,"\t\t\t<Route path=\"/"+name.lower()+"\" component={"+name+"} />")
                break
        line_count+=1
    f.close()
    f = open(path+"index.js", "w")
    f.write("\n".join(line_arr))
    f.close()


# -----------------------------------------MAIN--------------------------------------
for i in range(1,len(sys.argv)): 	
    component=sys.argv[i].capitalize()
    # if os.path.exists(path+component):
    #     shutil.rmtree(path+component)
    print("Creating "+component)
    try:
        os.mkdir(path+component)
        js(component)
        html(component)
        css(component)
        add_route(component)
        print()
    except:
        print(component+" component already exists")

   