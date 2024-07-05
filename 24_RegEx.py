# url = "https://dropbox.com/ramakant/img2.jpeg"
# lst = url.split('/')
# print(lst)
# print(lst[-1])

import re

'''
1. Methods
2. Meta characters
3. Special seqences
4. Extensions notations
    * comment
    * positive lookahead
    * negative lookahead
    * positive lookbehind
    * negative lookbehind
'''

string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
    including the FTSE, fell by 11.48% - the worst day since it launched in 1998. \
    The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
    of STOXX 600 shares since its all-time peak on 19 February."

string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% - the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

def UsingModules():
    path = r"c:\Users\temp\newfile.txt"     # raw string
    print(path)

    strPttrn = r"\d{2}"
    rePttrn = re.compile(strPttrn)

    print(strPttrn)
    print(type(rePttrn))

    # res = re.findall(rePttrn, string1)
    res = re.findall(strPttrn, string1)
    print(res)

    ## Search ######################################
    # Looks for the pattern through the entire string and stops after the first match
    res = re.search(strPttrn, string1)
    print(res)
    print(string1[res.span(0)[0]:res.span(0)[1]])

    # Match #####################################
    # Looks for the pattern from the starting of the string and stops after the patterne is found, and returns re.Match obj
    # If pattern is not found, it returns 'None'
    pt1 = r"\w{4}"
    res = re.match(pt1, string1)
    print(res)
    if res is not None:
        print(string1[res.span(0)[0]:res.span(0)[1]])
    else:
        print("No match found")

    ## FullMatch ###################################
    # Similar to match(), attempts to match from the beginning of the string, but it also has to match the entire string.
    print(len(string1))
    pt1 = r".{285}"         # '.' matches any character, apart from a newline
    res = re.fullmatch(pt1, string1)
    print(res)

    ## Split #######################################
    words = string1.split(' ')
    print(len(words), words)

    words = re.split(r"\s", string1)
    print(len(words), words)

    string2 = "The Euro STOXX 600 index, \nwhich tracks all stock markets across Europe including the FTSE, fell by 11.48% - the worst day since it launched in 1998. \nThe panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."
    words = string2.split(' ')
    print(len(words), words)

    words = re.split(r"\s", string2)
    print(len(words), words)

    words = re.split(r"\d{2}", string2)
    print(len(words), words)

    ## Sub - Substitute an occurance of a pattern with a given string
    res = re.sub(r'[A-Z]{2,}', "INDEX ", string1)
    print(type(res), res)

    ## SubN - Similar to sb, but returns a tuple - (<updatedString>, <replCount>)
    res = re.subn(r'[A-Z]{2,}', "INDEX ", string1)
    print(type(res), res)
    print(res[1], "-->", res[0])

def usingGroups():
    res = re.search(r".+\s(.+ex).+(\d\d\s.+).", string1)
    print(res.groups())     # Lists out all the matched groups

    # Individual group
    print(res.group(1))
    print(res.group(2))
    print(res.group(0))
    print(res.group())      # same as group(0)

    print(res.group(1, 2))
    
    print(res.span(1))
    print(res.span(2))

    print(res.start(1), res.end(1))
    print(res.start(2), res.end(2))

def usingFlags():
    res = re.findall(r'the', string1, re.I)     # Ignorecase
    print(len(res), "-->", res)

    string2 = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% - \nthe worst day since it launched in 1998. \nThe panic selling prompted by the coronavirus has wiped £2.7tn off \nthe value of STOXX 600 shares since its all-time peak on 19 February."
    res = re.findall(r'^the', string2, re.I|re.M)       # Multiline
    print(len(res), "-->", res)

    print(len(string2))
    pt1 = r".{288}"         # '.' matches any character, apart from a newline
    res = re.fullmatch(pt1, string2, re.S)      # DOTALL - enable the '.' to match newline chars as well.
    print(res)

    res = re.search(r'''.+\s        # Some chars of no interest in the beginning
                    (.+ex)          # word ending with the substring 'ex'
                    .+              # all chars in the middle
                    (\d\d\s.+)      # the date data we're looking for
                    .               # the last insignificant character
                    ''', string1, re.X)
    print(res.groups())


if __name__ == '__main__':
    # UsingModules()
    # usingGroups()
    usingFlags()