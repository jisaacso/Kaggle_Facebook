from numpy import *

if __name__=='__main__':

    col=genfromtxt('train-all.txt', delimiter="|",usecols=(0,),dtype='string',comments="%",autostrip=True)
#    f=open("train-list.txt",'wb')   
#    f.writelines("%s\n" % item for item in col)
#    f.writelines("|\n")
    x=unique(col)
    print len(x)

    col=genfromtxt('train-all.txt', delimiter="|",usecols=(1,),dtype='string',comments="%",autostrip=True)
#    f.writelines("%s\n" % item for item in col)
#    f.writelines("|\n")
    x = unique(col)
    print len(x)

    col=genfromtxt('train-all.txt', delimiter="|",usecols=(2,),dtype='string',comments="%",autostrip=True)
#    f.writelines("%s\n" % item for item in col)
#    f.writelines("|\n")
    y=unique(col)
    print len(y)
    print len(unique(concatenate((x,y))))
#    col=genfromtxt('train-all.txt', delimiter="|",usecols=(3,),dtype='string',comments="%",autostrip=True)
#    f.writelines("%s\n" % item for item in col)
#    f.writelines("|\n")
