def rootPath():
    name= __name__
    path=__file__
    return __file__.replace(name+".py","")