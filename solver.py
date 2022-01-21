import csv

with open('words.csv', newline='') as f:
    reader = csv.reader(f)
    words = list(reader)

list_5=[]
for word in words:
    if len(word[0]) == 5:
        list_5.append(word[0])
        
#step 1
word_1="power"
print("Enter the word 'POWER' oe some other word and let us know the result")

#stage 2
word_list=list_5.copy()
temp_word_list=[]
while True:
    word_1=input("Enter the last word you entered: ").lower()
    result=input("Enter the last result: ").lower()
    if result=="ggggg":
        print("Finished you won")
        break
    counter=0
    for i in result:
        if i=='g':
            for word in word_list:
                if word[counter]==word_1[counter]:
                    temp_word_list.append(word)
            del word_list
            word_list=temp_word_list.copy()
            del temp_word_list
            temp_word_list=[]
        counter=counter+1 
    counter=0
    for i in result:
        if i=='b':
            for word in word_list:
                if word_1[counter] in word:
                    pass
                else:
                    temp_word_list.append(word)
            del word_list
            word_list=temp_word_list.copy()
            del temp_word_list
            temp_word_list=[]
        counter=counter+1
    counter=0
    for i in result:
        if i=='y':
            for word in word_list:
                if word_1[counter] in word and word[counter]!=word_1[counter]:
                    temp_word_list.append(word)
            del word_list
            word_list=temp_word_list.copy()
            del temp_word_list
            temp_word_list=[]
        counter=counter+1
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    for word in word_list:
        print(word)
    print("Above are the possible words total: "+str(len(word_list))+" select a familiar word or a random word")
