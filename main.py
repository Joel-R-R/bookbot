def main():
    with open("/home/joel/workspace/github.com/Joel-R-R/bookbot/books/frankenstein.txt", 'r') as f:  # Use your actual path
        file_contents = f.read()
    print(file_contents)

main()