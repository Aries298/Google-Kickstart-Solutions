#For some reason it doesn't work on the Google site but works fine elsewhere
def Solution(s):
    T,N,K,S = [],[],[],[]
    def parseinput(text):
        text = text.split()
        T.append(int(text[0]))
        for i in range(1,len(text),3):
            N.append(int(text[i]))
            K.append(int(text[i+1]))
            S.append(str(text[i+2]))
        for i in range(len(N)):
            if(N[i]<1 or N[i]>2*pow(10,5)):
                raise ValueError("ValueError exception thrown")
            if(K[i]<0 or K[i]>(N[i]/2)):
                raise ValueError("ValueError exception thrown")
    
    def testgoodness(S):
        S = list(S)
        score = 0
        for i in range(int(len(S)/2)):
            if(S[i]!=S[len(S)-i-1]):
                score += 1
        return score
    
    parseinput(s)
    for i in range(T[0]):
        print(f"Case #{i+1}: {abs(testgoodness(S[i])-K[i])}")
