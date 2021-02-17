ab_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
   "m", "n", "o", "p", "q", "r", "s", "t", "v", "u", "w", "x", "y", "z"]

def encode_word(word, shift):
    new_word = ""

    for letter in word:
        if letter in ab_list:
            letter_index = ab_list.index(letter)
            new_word += ab_list[(letter_index + shift)%26] 
    return new_word

def decode_word(word, shift):
    
    new_word = ""

    for letter in word:

        if letter in ab_list:
            letter_index = ab_list.index(letter)
            new_word += ab_list[(letter_index - shift +26)%26] 
    return new_word



print("""Main Menu:

        1) Make a code 
        2) Decode a message
        3) Quit """)

user_input = int(input("Enter your selection: "))
    
if user_input == 1:
    word = input("Please enter a word to encode: ")
    word = word.lower()
    shift = int(input("Please enter a shift: "))
    print(encode_word(word, shift))

elif user_input == 2:
    word = input("Please enter a word to decode: ")
    word = word.lower()
    shift = int(input("Please enter a supposed shift: "))
    print(decode_word(word, shift))




# print(decode_word("nbnba", 1))
    
    
# def main():
#     again = "y"
#     while again == "y":
#         print("""Main Menu:

#         1) Make a code 
#         2) Decode a message
#         3) Quit """)

#         user_input = int(input("Enter your selection: "))
    
#     if user_input == 1:
#         word = input("Please enter a word to encode: ")
#         shift = int(input("Please enter a shift: "))
#         encode_word(word, shift)

    # elif user_input == 2:
    #     add_to_phb()

    # elif user_input == 3:
    #     show_surname()

    # elif user_input == 4:
    #     delete_byid()

    # elif user_input == 5:
    #     again = "n"

#     else:
#         print("Enter a number from the selection above")

# print(main())