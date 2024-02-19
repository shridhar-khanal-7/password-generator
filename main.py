import random
import string

# Define character sets
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# Welcome message
print('Welcome to the Password Generator App')

# User input for password length
length_of_password = int(input('Please enter the desired length of password:'))

if __name__ == "__main__":

 while True:
    # Display complexity options to the user
    print('\nChoose Complexity level of your password')
    print('High   : Strong Password')
    print('Medium : Less Strong Password')
    print('Low    : Weak password')

    # Get user input for the desired complexity level and convert to lowercase
    complexity = input('Enter the complexity level of your password: ').lower()

    # Check the complexity level and set the character set accordingly
    if complexity == 'high':
        all_characters = list(letters + numbers + symbols)
        random.shuffle(all_characters)  # Shuffle for added randomness
    elif complexity == 'medium':
        all_characters = list(letters + numbers)
    elif complexity == 'low':
        all_characters = list(letters)
    else:
        print('Error: Invalid Complexity level please try again!')
        continue  # Restart the loop if the complexity level is invalid

    final_password_list = []  # Reset for each iteration

    # Generate password by choosing random characters from the character set
    for _ in range(length_of_password):
        random_password = random.choice(all_characters)#Selection of random characters from all_characters
        final_password_list.append(random_password)#Inserting the random password to the list

    # Converting the list into a string using join
    final_generated_password = ''.join(final_password_list)#Join -the string method concatenates all the characters of list to single string.
    print(final_generated_password)

    break  # Exits the loop after generating and printing the password
