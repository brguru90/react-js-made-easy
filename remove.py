import sys,os,re
import shutil

path="./src/"

def remove_route(name):
    f = open(path+"index.js", "r")
    content=f.read()
    if os.path.exists(path+'index_bak2.js'):
        os.remove(path+'index_bak2.js')
    f2 = open(path+"index_bak2.js", "w")
    f2.write(content)
    f2.close()

    line_arr=content.split("\n")
    line_count=0
    for line in line_arr:
        if re.search("import\s+"+name+"\s+from\s+'\./"+name+"/"+name+"'",line):
            line_arr.pop(line_count)
        line_count+=1
    line_count=0
    for line in line_arr:
        if re.search("\s*<Route\s+path=\"/"+name.lower()+"\"\s+component={"+name+"}\s*/>",line):
            line_arr.pop(line_count)
        line_count+=1
    f.close()
    f = open(path+"index.js", "w")
    f.write("\n".join(line_arr))
    f.close()

# -----------------------------------------MAIN--------------------------------------
for i in range(1,len(sys.argv)): 	
    component=sys.argv[i].capitalize()
    print("Removing "+component)
    try:
        if os.path.exists(path+component):
            shutil.rmtree(path+component)
            remove_route(component)
            print("Removed")
    except:
        print(component+" component already exists")