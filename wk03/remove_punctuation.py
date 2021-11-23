import string

def main():
    with open("tolstoy.txt") as input_file:
        with open("no_punctuation.txt", "w+") as output_file:
            # Loop through each line in the read file
            for line in input_file:
                # Loop through word of the line 
                for word in line.split():
                    # Remove punctuation and then print out each word to 
                    # the output file, and append " " to the end of each word
                    print(word.strip(string.punctuation), end=" ", file=output_file)
                # By default print() adds a new line at the end of what it is
                # printing, so this prints out a "\n" to the output file
                print(file=output_file)


if __name__ == "__main__":
    main()
