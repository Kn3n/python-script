'''
Save the input in to file
'''
def main():
    '''
    Main function
    '''
    # Get the input
    input_string = input()
    print("Write the input to save in .txt archive.")
    # Write to file
    with open('input.txt', 'w') as file:
        file.write(input_string)
        print('You file has been created with the input')

'''
Execute the main function
'''
__name__ == '__main__' 
main()
