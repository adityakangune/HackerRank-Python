'''
You may be familiar with searching for text by pressing ctrl-F and typing
 in the words you’re looking for. Regular expressions go one step further:
They allow you to specify a pattern of text to search for.
Regular expressions, called regexes for short, are descriptions for a pattern
of text. For example, a \d in a regex stands for a digit character — that is, any single numeral 0 to 9.
'''
import re
for i in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except:
        print(False)