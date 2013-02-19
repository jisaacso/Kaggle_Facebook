from numpy import *
from scipy import sparse
import os
import csv
import pickle


def S(stri,strj):
    if stri==strj:
        return 1
    else:
        return -1

def alignScore(seq1, seq2):
#    print seq1
#    print seq2
    lena = len(seq1)
    lenb = len(seq2)

    lena_v = range(lena)
    lenb_v = range(lenb)

    d = 0

    F = array([[0]*lena]*lenb)
    F[0,:] = [d * x for x in lena_v]
    F[:,0] = [d * x for x in lenb_v]
    F[0,0] = S(seq1[0],seq2[0])

    for i in lenb_v[1:]:
        for j in lena_v[1:]:
            F[i][j]=max([F[i-1][j-1]+S(seq2[i],seq1[j]), F[i][j-1]+d, F[i-1][j]+d])


#    print float(F[-1][-1])/float(max([len(seq1),len(seq2)]))
            
    return float(F[-1][-1])/float(min([len(seq1),len(seq2)]))
#    return F[-1][-1]


def cleanstr(cstr):
#    str=str(str)
    return ''.join(sorted(cstr.lower())).lstrip()

#    return ''.join(cstr.split()).lower()
#    return ''.join(str(zz) for zz in sort([ord(chartohash) for chartohash in tmp]))

def hashstr_order_indep(arraytohash):
    arraytohash=''.join(arraytohash.split()).lower()
#    arraytohash = cleanstr(arraytohash)
    return str(hash(int(''.join(str(zz) for zz in sort([ord(chartohash) for chartohash in arraytohash])))))
#    return str(hash(int(cleanstr(arraytohash))))

def hash_AS_array(ASarray,trainset_node_h):

    for mystridx in range(len(ASarray)):
        mystr = ASarray[mystridx]
        if mystr.isdigit() and len(mystr)<19:
            mystrkey = mystr
        else:
            mystrkey = hashstr_order_indep(mystr)

        if trainset_node_h.has_key(mystrkey):
            ASarray[mystridx] = trainset_node_h[mystrkey] #rename
        else:
            trainset_node_h[mystrkey]=mystr

    return ASarray,trainset_node_h


def checkAS(str):
    global keycounter, trainset_hash

    akey = list()
    ISHASHED = False
    ISSMALLSTR = True
    MINMER = 5
    SIMILARITY_SCORE=.85
#    SIMILARITY_SCORE = 8
    hstr = hashstr_order_indep(str)

    for splitstr in str.split():
        ISNEWSTR = True
        if len(splitstr)>=MINNMER:
            ISSMALLSTR = False
        else:
            continue
        akey.append(hashstr_order_indep(splitstr))
        
        if trainset_hash.has_key(akey[-1]):
            idx = -1
            for b in trainset_hash[akey[-1]][1]:
                idx+=1
                d = alignScore(cleanstr(str),cleanstr(b))
                if d>SIMILARITY_SCORE:
                    albl = trainset_hash[akey[-1]][0][idx]
                    ISNEWSTR=False
                    ISHASHED=True
                    break
            if ISNEWSTR == True:
                trainset_hash[akey[-1]][1].append(str)
                trainset_hash[akey[-1]][0].append(keycounter)
#                albl = keycounter
#                keycounter+=1

#            ISHASHED = True
            break

    if ISSMALLSTR == True:
        albl = keycounter
        trainset_hash[hstr]=tuple([list(),list()])
        trainset_hash[hstr][0].append(albl)
        trainset_hash[hstr][1].append(str)
        keycounter+=1

    elif ISHASHED==False:
        albl = keycounter
        for key in akey:
            trainset_hash[key]=tuple([list(),list()])
            trainset_hash[key][0].append(albl)
            trainset_hash[key][1].append(str)
        keycounter+=1

    return albl

if __name__ == '__main__':
    
    print 'Hashing and writing paths.txt'

    f = open('train-all-clean-hashed.txt','wb')
    t = list()

    MINNMER = 5

    with open('train-all-clean.txt', 'rb') as csvfile:
        adjreader = csv.reader(csvfile, delimiter="|")
        global keycounter
        keycounter=0
        uniquecounter = 0
        global trainset_hash
        trainset_hash=dict()
        idx=-1

        for row in adjreader:
            idx+=1

            albl=checkAS(row[1])
            blbl=checkAS(row[2])

            t.append(row[0]+'|'+str(albl)+'|'+str(blbl)+'|'+row[3])
            if idx%100==0:
                print idx/float(722588)

    f.writelines('%s\n' % line for line in t)
    pickle.dump(trainset_hash,open('myhash.pkl','wb'))

    trainset_hash = pickle.load(open('myhash.pkl','rb'))

    print 'Number of unique keys is: ' + str(keycounter)
    t=list()
    f=open('paths-clean-hashed.txt','wb')
    print 'Done hashing\n'

    with open('paths-clean.txt', 'rb') as csvfile:
        adjreader = csv.reader(csvfile, delimiter="|")

        for row in adjreader:
            tsubstr = ''
            for col in row:
                blbl=checkAS(col)

                tsubstr = tsubstr+str(blbl)+'|'
                
            t.append(tsubstr)

        f.writelines('%s\n' % item for item in t)


