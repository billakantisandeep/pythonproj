import re 

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ 
123456789

Ha HaHa

Metacharacters ( Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-544-4321
123.555.1234
143*345*5667

Mr. Schafer 
Mr Smith
Ms Davis
Mrs. Robinson 
Mr. T




'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')  #Dot represents to match anything 
#pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') #This matches only the particular character set described.   Matches only one character.
#pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d') #This matches no.s starting with 800 or 900 ex: 800.123.1234 etc..
#re.compile(r'[1-5]')     Matches for all the digits of 1 to 5 
#[a-z] Matches all the lower case a to z 
#(r'[^a-zA-Z]')   -- Negate the lower case and upper case letters. 



matches = pattern.finditer(text_to_search)


for match in matches: 
    print (match)
