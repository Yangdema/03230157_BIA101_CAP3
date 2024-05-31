
################################
# Github Repo link: https://github.com/Yangdema/03230157_BIA101_CAP3
# Your Name: Lhamyang Dema
# Your Section: BBI "B"
# Your Student ID Number: 03230157
################################
# REFERENCES
# https://ioflood.com/blog/python-sum-list-how-to-calculate-the-sum-of-the-elements-in-a-list/ 
# Used general Python documentation and knowledge.
################################
# SOLUTION
# Your Solution Score: The total sum of the given input file 157.txt is 493423.
################################

def read_input(file_path):
    #Initialize the sum variable
    total_sum = 0
    
    # Open the file and read it line by line
    with open(file_path, 'r') as file:
        line_number = 1
        for line in file:
            # Remove newline characters and strip whitespace
            cleaned_line = line.strip()
            
            # Initialize variables to hold the first and last digit
            first_digit = None
            last_digit = None
            
            # Loop through the characters to find the first digit
            for char in cleaned_line:
                if char.isdigit():
                    first_digit = char
                    break
            
            # Loop through the characters in reverse to find the last digit
            for char in reversed(cleaned_line):
                if char.isdigit():
                    last_digit = char
                    break
            
            # Check if both digits were found
            if first_digit is not None and last_digit is not None:
                # Combine them into a two-digit number
                two_digit_number = int(first_digit + last_digit)
                
                # Print the line number and the two-digit number
                print(f"Line {line_number}'s number is: {two_digit_number}")
                
                # Add the two-digit number to the sum
                total_sum += two_digit_number
            
            # Increment the line number
            line_number += 1
    
    # Print the total sum
    print(f'The total sum of the given input file {file_path} is {total_sum}.')

# Example usage
file_path = '157.txt'  # Replace 'your_file.txt' with the path to your text file
read_input(file_path)