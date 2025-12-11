# Bristie Rahman
# Python implementation of stable matching problem
# Homework 1 Starter Code
# CYB 2013

def gs(men, women, pref):
    """
    Gale-shapley algorithm, modified to exclude unacceptable matches
    Inputs: men (list of men's names)
            women (list of women's names)
            pref (dictionary of preferences mapping names to list of preferred names in sorted order)
            blocked (list of (man,woman) tuples that are unacceptable matches)
    Output: dictionary of stable matches
    """
    # preprocessing
    ## build the rank dictionary
    rank={}
    for w in women:
        rank[w] = {}
        i = 1
        for m in pref[w]:
            rank[w][m]=i
            i+=1
    ## create a "pointer" to the next woman to propose
    prefptr = {}
    for m in men:
        prefptr[m] = 0

    freemen = set(men)    #initially all men and women are free
    numpartners = len(men) 
    S = {}           #build dictionary to store engagements 

    #run the algorithm
    while freemen:
        m = freemen.pop()
        #get the highest ranked woman that has not yet been proposed to
        w = pref[m][prefptr[m]]
        prefptr[m]+=1
        if w not in S: S[w] = m
        else:
            mprime = S[w]
            if rank[w][m] < rank[w][mprime]:
                S[w] = m
                freemen.add(mprime)
            else:
                freemen.add(m)
    return S

###Task A


def gs_block(men, women, pref, blocked):
  
    rank = {}
    for w in women:
       rank[w] = {}
       i = 1
       for m in pref[w]:
           rank[w][m] = i
           i += 1
#pointer
    prefptr = {}
    for m in men:
       prefptr[m] = 0

    #freemen = set(men)
    import copy
    freemen = copy.deepcopy(men) 
    numpartners = len(men)
    S = {}
#algortihm
    
    while freemen:
       m = freemen.pop(0)
       w = pref[m][prefptr[m]]
       prefptr[m] += 1

       if w not in S:
           # Check if this match is blocked
           
           if ((m,w) or (w,m)) and ((w, m) and (m, w)) not in blocked:
               
               S[w] = m
       else:
           mprime = S[w]
           if rank[w][m] < rank[w][mprime]:
               S[w] = m
               freemen.append(mprime)
           else:
               freemen.append(m)

    return S
                           
### Task B                              

def gs_tie(men, women, preftie):
    rank = {}

    for w in women:

       rank[w] = {}

       i = 1

       for m_set in preftie[w]:

           for m in m_set:

               rank[w][m] = i

           i += 1

#pointer
    prefptr = {}

    for m in men:

       prefptr[m] = 0




    freemen = set(men)

    numpartners = len(men)

    S = {}
    
##algortihm
    while freemen:

       m = freemen.pop()

       w_set = preftie[m][prefptr[m]]

       prefptr[m] += 1
       accepted = False
        
       for w in w_set:

           if w not in S:

               S[w] = m
               accepted = True
               break

           else:

               mprime = S[w]

               if rank[w][m] < rank[w][mprime]:
                   accepted = True 
                   S[w] = m

                   freemen.add(mprime)
                   break
                
       if accepted == False:
           freemen.add(m)  
                           
                   
                         
                   
#freemen.add(m)

 

    return S









if __name__=="__main__":
    #input data
    themen = ['xavier','yancey','zeus']
    thewomen = ['amy','bertha','clare']

    thepref = {'xavier': ['amy','bertha','clare'],
           'yancey': ['bertha','amy','clare'],
           'zeus': ['amy','bertha','clare'],
           'amy': ['yancey','xavier','zeus'],
           'bertha': ['xavier','yancey','zeus'],
           'clare': ['xavier','yancey','zeus']
           }
    thepreftie = {'xavier': [{'bertha'},{'amy'},{'clare'}],
           'yancey': [{'amy','bertha'},{'clare'}],
           'zeus': [{'amy'},{'bertha','clare'}],
           'amy': [{'zeus','xavier','yancey'}],
           'bertha': [{'zeus'},{'xavier'},{'yancey'},],
           'clare': [{'xavier','yancey'},{'zeus'}]
           }
    
    blocked = {('xavier','clare'),('zeus','clare'),('zeus','amy')}

    #eng
    match = gs(themen,thewomen,thepref)
    print(match)
    
    match_block = gs_block(themen,thewomen,thepref,blocked)
    print(match_block)

    match_tie = gs_tie(themen,thewomen,thepreftie)
    print(match_tie)
