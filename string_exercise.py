#given a string, pring the string uppercased

my_name = 'oh happy day'
print(my_name.upper())

#given a string, print the string capitalized

name = 'aylin'
new_name = name[0].upper() + name[-4:]
print(new_name)


#reverse a string
forward = "Would you look at that!"
reverse_it = forward[-1::-1]
print(reverse_it)

#Leetspeak-Given a paragraph of text as a string, 
#print the paragraph in leetspeak. To translate a string to leetspeak, 
#you need to make the following character replacements 
#(treat all input characters as uppercase):

p = "This is a sentence. Now its in a leetspeak."
leet = ['a','e','g','i','o','s','t']
num = ['4','3','6','1','0','5','7']
for c in range(len(p)):
    for j in range(len(leet)):
        if leet[j] ==  p[c]:
            p = p.replace(p[c], num[j])
print(p)
   
      

#long-long vowels
#ask = input("Give me a word with a vowel in it:")
#vowels = ['a','e','i','o','u']

for c in input:
    for j in 









