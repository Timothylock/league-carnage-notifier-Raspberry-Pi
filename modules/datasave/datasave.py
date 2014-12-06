import json

def save(dic, filename):
    f = open(filename,'w')
    f.write(json.dumps(dic))
    f.close()

def read(filename):
    f = open(filename, 'r')
    dic = json.loads(f.readline())
    f.close()
    return dic
