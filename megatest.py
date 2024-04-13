gpsums = {

"F"   : 2,
"U"   : 3,
"V"   : 3,
"TH"  : 5,
"O"   : 7,
"R"   : 11,
"C"   : 13,
"K"   : 13,
"G"   : 17,
"W"   : 19,
"H"   : 23,
"N"   : 29,
"I"   : 31,
"J"   : 37,
"EO"  : 41,
"P"   : 43,
"X"   : 47,
"S"   : 53,
"Z"   : 53,
"T"   : 59,
"B"   : 61,
"E"   : 67,
"M"   : 71,
"L"   : 73,
"NG"  : 79,
"ING" : 79,
"OE"  : 83,
"D"   : 89,
"A"   : 97,
"AE"  : 101,
"Y"   : 103,
"IA"  : 107,
"IO"  : 107,
"EA"  : 109

}

runes = {

"ᚠ"   : 2,
"ᚢ"   : 3,
"ᚢ"   : 3,
"ᚦ"   : 5,
"ᚩ"   : 7,
"ᚱ"   : 11,
"ᚳ"   : 13,
"ᚳ"   : 13,
"ᚷ"   : 17,
"ᚹ"   : 19,
"ᚻ"   : 23,
"ᚾ"   : 29,
"ᛁ"   : 31,
"ᛄ"   : 37,
"ᛇ"   : 41,
"ᛈ"   : 43,
"ᛠ"   : 47,
"ᛋ"   : 53,
"ᛋ"   : 53,
"ᛏ"   : 59,
"ᛒ"   : 61,
"ᛖ"   : 67,
"ᛗ"   : 71,
"ᛚ"   : 73,
"ᛝ"   : 79,
"ᛝ"   : 79,
"ᛟ"   : 83,
"ᛞ"   : 89,
"ᚪ"   : 97,
"ᚫ"   : 101,
"ᚣ"   : 103,
"ᛡ"   : 107,
"ᛡ"   : 107,
"ᛉ"   : 109

}
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#<--------------------[!!! A WARNING !!!]--------------------->
#
#       THIS PROJECT IS WORK IN PROGRESS STILL! 
#   THE CODE IS MESSY, THIS IS A PERSONAL PROJECT 
#                  SO IT FITS MY NEEDS
#       MODIFY AT YOUR OWN RISK. THANK YOU!
#
#<--------------------[...GOOD LUCK...]--------------------->
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#The two squares from the solved pages
square1 = [272,138,341,131,151,366,199,130,320,18,226,245,91]
square2 = [434,1311,312,278,966,204,812,934,280,1071,626,620,809]


#<--------------------[start of additional functions]--------------------->
def menu():

    print()
    print()

    print("<============ [ GPSUM ] ============>")
    print("                                     ")
    print(" gematria primus sum in the terminal ")
    print("                                     ")
    print("<============= [ wip ] =============>")
    print("            # by SvEnY #")

    print()
    print()

def line():
    print("======================================")

def lineshort():
    print("--------------------------")
#!!!!!!!!!!!! VERY IMPORTANT METHOD I GOT FROM STACK OVERFLOW - IT MAKES GP SUM WORK !!!!!!!!!!!!!!!!!!!!!!!!
def func(word, n):
    return [''.join(item) for item in zip(*[word[n:] for n in range(n)])]

def factors(x):
    arr = []
    arrprimes = []

    for i in range (1, x + 1):
        if x % i == 0:
            arr.append(i)
            if isprime3(i):
                arrprimes.append(i)

    print(f"the factors of {x} are: {arr}")
    print(f"the PRIME FACTORS of {x} are : {arrprimes}")

def isprime(x):

    if x == 1 :
        print(f"{x} is not prime ")

    if x > 1:
        for i in range(2,x):
            if(x % i) == 0:
                print(f"{x} is not prime ")
                print(f"{i} times {x//i} is {x}")
                break
        else:
                print(f"{x} is PRIMEEEE!!!!")
    else:
        print(f"{x} is not prime ")


#def isprime2():
#            val = int(input(">value: "))
#            isprime(val)


def isprime3(x):

    if x <= 1 :
        return False

    if x > 1:
        for i in range(2,x):
            if(x % i) == 0:
                return False
            
        return True
    
def gcd(p,q):
    while q != 0:
        p,q = q, p%q
    return p 

def is_coprime(x,y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x, y)]
        return len(n)


def iteratelist(x):
    if x in square2 :
        print(f" Value {x} is FOUND in SQUARE 2")
    else :
        print(f"{x} NOT FOUND in square2")
    
    if x in square1 :
        print(f"{x} is FOUND in SQUARE 1")
    else :
        print(f"{x} NOT FOUND in square1")   


def isEmirp(num):
   num = int(num)
   if  isprime3(num) == False:
      return False

   reverse_num = 0
   while num != 0:
      d = num % 10
      reverse_num = reverse_num * 10 + d
      num = int(num / 10)
   return isprime3(reverse_num)
   

def nThPrime(n):
    i = 2
    while(n > 0):
 
       
        if(isprime3(i)):
            n -= 1
 
        i += 1  
 
    i -= 1 
   
    return i


######################################################################################################################################################################    
################################## [ START OF find_nth_non_symbol_character_and_remove_symbols  ] ####################################################################
######################################################################################################################################################################
def is_symbol(char):

    symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \n"
    return char in symbols

def nthchar(file_path, n):
    with open(file_path, 'r') as file:
        count = 0
        nth_character = None
        cleaned_text = ""
        
        while True:
            char = file.read(1)
            if not char:
                break  # End of file reached
            if not is_symbol(char):
                count += 1
                if count == n:
                    nth_character = char
            cleaned_text += char if not is_symbol(char) else ''  # Append the character if not a symbol
    print("------")
    print(f"{n}th character : {nth_character}") 
    print(f"characters : {count}")
    print("------") 

######################################################################################################################################################################    
################################## [ END OF find_nth_non_symbol_character_and_remove_symbols  ] ######################################################################
######################################################################################################################################################################

#<--------------------[end of additional functions]--------------------->
#                                   ***
#<-----------------------[ gematria sum function ]----------------------->

def gepsum():

  while True:

    print("Please input numeric value: ")
    print("[1] GP SUM ")
    print("[2] IS PRIME?")
    print("[0] Exit")
    try:
      option = int(input(">:"))
      if option == 0:
        break
      elif option == 1:
    

            sum=0
            word = input("Word: ").upper()
            wordcopy = word

# =============  searching for  ======================================================================= 
#                     ING

            for item in func(word, 3):
                for key,value in gpsums.items():
                    if key == item:
                        sum = sum + value
                        word = word.replace(item,'#')
                                  
# =============  searching for  ======================================================================= 
#           EA,IO,IA,AE,OE,NG,EO,TH

            sum2 = sum
            for item in func(word, 2):
                for key,value in gpsums.items():
                    if key == item:
                        sum2 = sum2 + value
                        word = word.replace(item,'#')
                                    
# =============  searching for  ======================================================================= 
#            REMAINING SINGLE LETTERS

            sum3 = sum2
            for item in func(word, 1):
                for key,value in gpsums.items():
                    if key == item:
                        sum3 = sum3 + value
                        word = word.replace(item,'#')
                                    




#<--------------------[ ***************************** ]--------------------->                                     
#    ===( MENU OPTIONS AND FUNCTIONS BASED ON INPUT [1][2][0] ETC )===    
#<--------------------[ ***************************** ]--------------------->                
 
            
#<--------------------[ [1] RESULT GPSUM + OTHER ]--------------------->        
#     
            print(f"\n     !!----> [{wordcopy}]  = {sum3} <----!! \n")
            
            line()
            lineshort()

            iteratelist(sum3)

            lineshort()

            isprime(sum3)

            if isEmirp(sum3):
                print("EMIRP")
            else :
                print("not emirp")

            lineshort()

            print(f"phi({sum3}) =               {phi_func(sum3)}")
            print(f"{sum3} % 29 =                {sum3 % 29}")
            letters_wo_space = len(wordcopy) - wordcopy.count(" ")
            print(f"char count w/o space =   {letters_wo_space}")
            print(f"char count w space =     {len(wordcopy)}")
            lineshort()
            factors(sum3)

            lineshort()

            # big values = computer boom
            maxv = 550
            if(sum3 > maxv):
                print(f"nth prime function disabled for values > {maxv}")

            else:
                 print(f"{sum3}th prime is {nThPrime(sum3)}")

            lineshort()


#<---[ nth character + total characters from text files ]---> 

            print("\n=-=-=- (w/o punc/symb/whsp) =-=-=- ")

            line()
            print("[ THE OLD RUNE POEM ]")           
            nthchar("runepoem.txt",sum3)

            print("[ THE MARRIAGE OF HEAVEN AND HELL ]")           
            nthchar("MOHAH.txt",sum3)
            line()
            

#<--------------------[ [2] CHECK PRIME NUMBER + OTHER ]--------------------->   

      elif (option == 2):
            val = int(input(">value: "))
            
            line()
            lineshort()
            
            isprime(val)
            
            lineshort()
            
            if isEmirp(val):
                print("EMIRP")
            else :
                print("not emirp")

            lineshort()
            line()

            print(f"phi({val}) =               {phi_func(val)}")
            print(f"{val} % 29 =                {val % 29}")
            factors(val)


#<---[ nth character + total characters from text files ]---> 
   
            print("\n=-=-=- (w/o punc/symb/whsp) =-=-=- ")

            line()
            print("[ THE OLD RUNE POEM ]")           
            nthchar("runepoem.txt",val)

            print("[ THE MARRIAGE OF HEAVEN AND HELL ]")           
            nthchar("MOHAH.txt",val)
            line() 
            
           # big value makes pc die 
            maxv = 550
            if(val > maxv):
                print(f"nth prime function disabled for values > {maxv}")

            else:
                 print(f"{val}th prime is {nThPrime(val)}")
            
            lineshort()
            
            iteratelist(val)
            
            line()

      else:           
        print("Invalid input!!!")
    except ValueError:
        print("Invalid input! Please use only 1/2/3")

menu()
gepsum()


