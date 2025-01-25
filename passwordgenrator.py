import random
import array

max_len=12

digit=['0','1','2','3','4','5','6','7','8','9']
locase=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
upcase=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
symbol=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

combined=digit+upcase+locase+symbol

#randomly choose one character from each above list, this step will meet minimum requirement of password that is atlest on character in caps, number, special character 
random.digit=random.choice(digit)
random.symbol=random.choice(symbol)
random.locase=random.choice(locase)
random.upcase=random.choice(upcase)

#create temp password by comining above four main selections, so current password is 4 length 
#still 
temp_pass=random.digit+random.upcase+random.locase+random.symbol
temp_pass

#loop to create remaining legth password randomly 
for x in range(max_len-4):
    temp_pass=temp_pass+random.choice(combined)
    temp_pass_list=array.array('u', temp_pass)            #not sure why 'u' is used  
    random.shuffle(temp_pass_list)                        #shuffle required so there will be no specific pattern

password=''
for x in temp_pass_list:
    password=password+x

password
