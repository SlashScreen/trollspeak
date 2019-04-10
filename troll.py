#troll .py. written on  2 am

#input for all
text = input("Enter text. ")
troll = input("Which troll? ").lower()
out = ""

#KARKAT
if "karkat" in troll:
    out = text.upper() #hahahahhahahahha
    #TEREZI
elif "terezi" in troll:
    text = text.replace ("a","4")
    text = text.replace ("i","1")
    text = text.replace ("e","3") #damn it be johns birthday. strande
    out = text.upper()
    #VRISKA
elif "vriska" in troll:
    #FIXME: Combo detect no work
    text = text.replace("b","8")
    text = text.replace("B","8")
    text = text.replace("ate","8")
    text = text.replace("eight","8")
    text = text.replace("Eight","8") #lazy work around for not lowering shit
    text = text.replace("ait","8")
    if input("Distressed? (y/n) ").lower() == "y": #if distressed
        s = list(text) #convert to list for char change
        print(s)
        for i, c in enumerate(text): #enumer8
            if c.lower() in ('a', 'e', 'i', 'o', 'u'): #if vowel
                s[i] = "8" #then 8
                print(s[i],"0")
                if s[i+1]: #if next character exists
                    print(s[i+1],"1")
                    if s[i+1].lower() in ('a', 'e', 'i', 'o', 'u'): #if vowel, for combos
                        s[i+1] = None #is nothing
                    print(s[i+1],"2")
        #find vowel combos
        out = ''.join(s)
        print(s)
    else:
        out = text #if not, everything was done before
        
    #oh god english
#FEFERI
elif "feferi" in troll:
    #verify loop for excite, then dashes
    verified = False
    excite = 0 #excitement levels
    while not verified:
        try:
            excite = int(input("Current Excitement Levels (CEL)? (0 -> 100) "))
            if excite <=100 and excite >= 0:
                verified = True #this satisfies both a number and between 0 and 100
            else:
                verified = False
                print("input a number between 1 and 100 please.")
        except:
            print("please input a number between 0 and 100.")

        text = text.lower().replace("h",") (") #do that ) ( ard to read thing
        le = text.rfind("e") #find last e
        if excite > 0: #if excite is 0 skip this shit
            text = text[:le] + "-"*(excite-1) + text[le:] #super long  thign. it's -1 because another 1 will be added later
            text = text.replace("e","-e") #replace others
        #detect last E in sequence, insert hyphen*exite. all others insert 1 beforehand.
        out = text.upper()
#NEPETA
elif "nepeta" in troll:
    text = text.replace ("e","33") #e
    out = ":33 < " + text #add bedinning
#EQUIUIUISUS
elif "equius" in troll:
    text = text.replace ("x","%") #x
    text = text.replace ("loo","100") #loo
    text = text.replace ("ool","001") #ool
    s = text.split(" ") #split into w ords
    for i,l in enumerate(s):
        if "strong" in l.lower(): #caps "strong" words
            s[i] = l.upper()+" " 
        else:
            s[i] = l+" " #ass space back in, like a bove, but no capitalize
    out = "D --> " + ''.join(s) #add shitty arrow
#ERIDIAN
elif "eridan" in troll:
    text = text.replace ("w","ww") #selfexplanatory
    out = text.replace ("v","vv")
#KANAYA
elif "kanaya" in troll:
   out = text.title() #capitalize every word Clearly And Carefully
#GAMZEE
elif "gamzee" in troll:
    alterniate = [] #haha get it??
    if input("Honk mode? ").lower() == "y":
        #split at .
        alterniate = text.split(".") #Split at sentences
        for i,l in enumerate(alterniate):
            alterniate[i] = l+"." #add period at sentences, removed in split
    else:
        alterniate = list(text.lower()) #list into chars, not sentences

    state = False #false for lower, true for upper
    for a in alterniate: #alternate
        o=''
        if state:
            o = a.lower() #lowervace
        else:
            o = a.upper() #uppercase
        state = not state #flip state
        out = out+o #add char
#TAVROS
elif "tavros" in troll:
    text = text.capitalize() #add capital at beginning of centence
    text = text.replace(".",",") #. -> ,
    out = ''.join(c.lower() if c.isupper() else c.upper() for c in text) # reverse capitalizeation
#ARABIA
elif "aradia" in troll:
    out = text.replace("o","0") #figgure it out jack asss
#SOLLUX CAPTOR
elif "sollux" in troll:
    text = text.replace ("i","ii") #two eyes. get it??
    text = text.replace ("to ","two ") #to with space for word
    text = text.replace ("too ","two ") #too with sapce for word
    text = text.replace ("to","two") #to without for parts of words like into and tomorrow
    out = text.replace ("s","2") #s -> 2
#LATER: Add more trolls and also cherubs maybe? dont forget Xefros
#INVALID TROLL >:[
else:
    out = "input a fucking troll you absolute doormat" #insult user

print(out) #print result

#i should be working on an essay
