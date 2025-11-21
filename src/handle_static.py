import os, shutil

def static_copy(origin, destination):
    shutil.rmtree(destination,False,onexc=None)

def recursive_copy(origin, destination, ):
    names = os.listdir(origin)
    
    for name in names:
        dire = os.path.join(origin,name)
        its_a_file = os.path.isfile(dire)
        if its_a_file:
            shutil.copy(dire, destination)
        else:
            dest = os.path.join(destination,name)
            os.mkdir(dest)
            recursive_copy(dire,dest)


    