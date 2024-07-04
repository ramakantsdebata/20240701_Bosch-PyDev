import sys
import os

def demoSys():
    # lst = "This is a string to be broken up into tokens".split()
    # for index, word in enumerate(lst):
    #     print(index, "-->", word)

    ## sys.argv
    for index, arg in enumerate(sys.argv):
        print(index, "-->", arg)

    ## sys.path
    # sys.path.insert(0, "..\\..\\")
    for item in sys.path:
        print(item)

    ## sys.version
    print("Version ->", sys.version)

def osDemo():
    curr_dir = os.getcwd()
    print(curr_dir)

    newFldrName = "demo"

    # newfolder = curr_dir + os.sep() + newFldrName
    newfolder = os.path.join(curr_dir, newFldrName)

    if os.path.exists(newfolder) == False:
        os.mkdir(newfolder)
        print(f"Created the folder '{newfolder}'.")
    else:
        print(f"'{newfolder}' already exists.")

    print(os.listdir(curr_dir))

    newFile = os.path.join(newfolder, 'newfile.txt')
    fl = open(newFile, 'w')
    fl.write("This is some test data.")
    print(type(fl))
    fl.close()

    # with open(newFile, 'w') as fl:
    #     fl.write("This is some test data.")

        # write() - writes to the file
        # writeline() --> Doesn't exist in Python
        # writelines([]) -- Accepts a list of strings and writes each string as a line

    with open(newFile, 'r') as fl:
        print(fl.read())

    # read() - Reads till the end of file/stream
    # read(n) - Reads the next 'n' codepoints and returns
    # readline() - Reads till a newline char
    # readlines(hint) - return a list of lines; Reads till end of file and creates the list
    #                   Reads lines till the hint (no. of codepoints) is breached; then stops reading more lines
    #                   Will discuss in session tomorrow.



    
    os.remove(newFile)
    os.rmdir(newfolder)
    

if __name__ == '__main__':
    # demoSys()
    osDemo()