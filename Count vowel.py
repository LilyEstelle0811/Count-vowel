import os

def read_f(file):
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0
    story = open(file,'r')
    for i in story:
        new = i.lower()
        print(new,end='')
        for i in new:
            if i == 'a':
                count_a += 1
            elif i == 'e':
                count_e += 1
            elif i == 'i':
                count_i += 1
            elif i == 'o':
                count_o += 1
            elif i == 'u':
                count_u += 1
    print('A frequency:',count_a)
    print('E frequency:',count_e)
    print('I frequency:',count_i)
    print('O frequency:',count_o)
    print('U frequency:',count_u)
    story.close()
    with open ('paragraph_from_wikipedia.vowel_profile','w') as outstream:
        outstream.write('This is a Vowel Profile file')
        outstream.write('\n')
        outstream.write('A frequency:')
        outstream.write(str(count_a))
        outstream.write('\n')
        outstream.write('E frequency:')
        outstream.write(str(count_e))
        outstream.write('\n')
        outstream.write('I frequency:')
        outstream.write(str(count_i))
        outstream.write('\n')
        outstream.write('O frequency:')
        outstream.write(str(count_o))
        outstream.write('\n')
        outstream.write('U frequency:')
        outstream.write(str(count_u))
        outstream.close()
