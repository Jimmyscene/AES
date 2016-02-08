from PrintHexMatrix import PrintHexMatrix 
'''
Take a List of lists and returns a list of lists
Inner lists are of type String, In Hex format
'''
def MixCols(matrix):
    Rijndael=[[02,03,01,01],[01,02,03,01],[01,01,02,03],[03,01,01,02]]
    holder=[]
    d=[]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                holder.append((_Shift(matrix[k][j],Rijndael[i][k])))
            d.append(holder)
            holder=[]
    for row in d:
        temp=0 
        for x in range(4):
            temp=temp^row[x]
        holder.append(temp)
    retmatrix=[map(lambda a: format(holder[a],'02X'),range(b*4,b*4+4)) for b in range(4)] 
    return retmatrix


def _Shift(Element, Range):
    a=int(Element, 16)
    if(Range>1):
        a=a<<1
    
       # a=int(binformat(a),2)
        if(int(Element,16)>127):
            a=a^27
            a=a-256
        if(Range>2):
            a=a^int(Element,16)
    return a

if __name__=='__main__':

    
    b= [['7C','6B','01','D7'],['F2','30','FE','63'],['2B','76','7B','C5'],['AB','77','6F','67']]

    print MixCols(b)
    
















#print  binformat(Shift("87",2))
    #print  binformat(Shift("6E",3))
    #print  binformat(Shift("46",1))
    #print  binformat(Shift("A6",1))
    #
   # print hex(Shift("87",2)^Shift("6E",3)^Shift("46",1)^Shift("A6",1))
   #b=np.array([[int(raw_input(),16),int(raw_input(),16),int(raw_input(),16),int(raw_input(),16)],[int(raw_input(),16),int(raw_input(),16),int(raw_input(),16),int(raw_input(),16)],[int(raw_input(),16),int(raw_input(),16),int(raw_input(),16),int(raw_input(),16)],[int(raw_input(),16),int(raw_input(),16),int(raw_input(),16),int(raw_input(),16)]])
    #b=[[135, 242,  77, 151],[ 99,  76, 144, 236],[ 70,  55,  74, 195],[166, 140, 216, 149]]
    #   b= [['87','F2','4D','97'],['6E','4C','90','EC'],['46','E7','4A','C3'],['A6','8C','D8','95']]