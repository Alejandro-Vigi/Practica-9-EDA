vg ="Global"

def f1():
    print(vg)

def f2():
    vg ="Local"
    print(vg)

def f3():
    global vg
    print(vg)
    vg = "Local"
    print(vg)

def f4():
    print(vg)
    vg ="Local"
    print(vg)
    
    

f1()
f2()
f4()
f3()
print(vg)