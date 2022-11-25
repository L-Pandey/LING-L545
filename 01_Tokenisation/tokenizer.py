########### Code without using replace() function. Using Dictionary instead, since lookup time in a dictionary is O(1).

# import libraries
import sys

# take input as a line from console
text = sys.stdin.readline()
# assign variable for couting lines
send_id = 1

# create a dict for replacing items
# key = original char, item = replacement char
dict_replacement = {
    '(': '( ',
    "'": "' ",
    '"': ' " ',
    ')': ' )',
    ',': ' ,',
    ', ': ' ,',
    ':': ': ',
}

# store ouput in pre-processed text
processed_text = ""

# while there exists a line in input
while text:
    # display the send Id and the original text
    print("# send_id = ", send_id)
    print('# ' + text)

    # iterate through the original text 
    for char in text:
        # if no match found from dictionary keys
        if char not in dict_replacement.keys():
            processed_text+=char
        # match found from dictionary keys
        elif char in dict_replacement.keys():
            # append the replacement character from dict to pre-processed text
            processed_text+=dict_replacement[char]
    
    # break into tokens by whitespace
    processed_text = processed_text.split(' ')
    # newline after each token
    processed_text = '\n'.join(processed_text)
    # display final tokenized words
    print(processed_text)

    # take the next line input from console
    text = sys.stdin.readline()
    # break if there is only whitespace and no characters in next line
    if len(text)<2:
        break
    # else increement the send_id
    send_id+=1
    # reset output
    processed_text = ""