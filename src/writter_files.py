'''
Save the input in to file
'''
def main():
    '''
    Main function
    '''
    # Get the input
    input_string = input()
    # Write to file
    with open('input.txt', 'w') as file:
        file.write(input_string)

'''
Execute the main function
'''
if __name__ == "__main__":
    main()