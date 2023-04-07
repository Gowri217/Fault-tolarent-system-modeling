import random

def dataSource():
    v=random.randint(4,5)
    i=random.random()
    p=v*i
    t=random.randint(80,120)
    s=random.randint(40,100)
    payload='{"Voltage" : ' + str(v) + ', "Current" : '+ str(i) +', "Power" : ' + str(p) + ', "Temperature" : ' + str(t) + ', "Sound" : '+str(s)+' }'
    print(payload)
    return payload
