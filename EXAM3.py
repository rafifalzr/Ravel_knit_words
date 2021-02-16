# kata = input("masukkan kata: ") 
# list_kata = list(kata) 
# # jumlah = len(list_kata)
# print(list_kata[0])
def ravel(y) :
    listy = list(y) 
    jum = len(listy) 
    list_ravel = [] 
    for i in range(jum) : 
        x = listy[0:i+1]  
        list_ravel.append(x) 
    # new = "".join(list_ravel) ## join error
    # return new
    return list_ravel

        

print(ravel("Purwadhika"))
print(ravel("Digital"))
print(ravel("Coding"))
print(ravel("School"))


def knit(z) :
    listz = list(z)
    jum = len(listz)
    list_knit = []
    for i in range(jum):
        x = listz[0:i]
        list_knit.pop(x)
    return list_knit
    
print(knit("PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika"))
print(knit('DDiDigDigiDigitDigitaDigital'))
print(knit('CCoCodCodiCodinCoding'))
print(knit('SScSchSchoSchooSchool'))