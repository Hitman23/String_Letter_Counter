
class StringCount:

    def count_Words(self,x):
        
        #define a dictionary to which we shall add the words and there values
        dictionary = {}
        
        #get the length of the list provided
        num = len(x)
        
        #iterating through the list provided as input
        iterator = 0

        while iterator<num:
            #seperate each word with in the current string. By default it is spaces
            words = x[iterator].split()
            
            #loop through each of the separated words
            for k in words:
                #convert each word to lower case
                word = k.lower()
                
                if word in dictionary:
                    #if word already exists in the dictionary increments its value
                    dictionary[word]+=1
                else:
                    #if word doesn't exist then give it a value of 1
                    dictionary[word] = 1
            #increment the iteration factor(acting as our index) so as to access the next element in the sequence     
            iterator+=1

        return dictionary


#a list of strings/messages that are provided as actual parameters for the countWords function
words_to_count = ["hi there, how are you","are you coming for lunch tonight", "when are we going to the movies"]
#a prompt for the user to enter his or her message
new_word = raw_input("Type your message here:")

#add the user's message into our list
words_to_count.append(newword)

#creating object of the stringcount class
returned_Data = StringCount()

#printing our output
print returned_Data.count_Words(words_to_count)


    
