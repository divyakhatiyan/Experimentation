## Purpose of this Programme is to format the input List into required format
## Input: arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
## Output: 
###    32      3801      45      123
### + 698    -    2    + 43    +  49
### -----    ------    ----    -----

def arithmetic_arranger(problems, show_answers=False):
    formattedtoprow = ''
    formattedmiddlerow = ''
    formattedbottomrow = ''
    spacebtw = '    '
    hypentobeadded = '-'
    for row in problems:

        if row.find('+') > 0:
            Listarry = row.split('+')
            Listarry[0] = Listarry[0].strip()
            Listarry[1] = '+ ' + Listarry[1].strip()
            if len(Listarry[0]) < len(Listarry[1]):
               res = len(Listarry[1]) - len(Listarry[0])
               spacetobeadded = ' ' * res
               formattedtoprow = formattedtoprow + spacetobeadded + Listarry[0] + spacebtw
               formattedmiddlerow = formattedmiddlerow + Listarry[1] + spacebtw
               formattedbottomrow = formattedbottomrow + hypentobeadded * len(Listarry[1]) + spacebtw
            elif len(Listarry[0]) > len(Listarry[1]):
                res = len(Listarry[0]) - len(Listarry[0])
                spacetobeadded = ' ' * res
                formattedmiddlerow = formattedmiddlerow + spacetobeadded + Listarry[1] + spacebtw
                formattedtoprow = formattedtoprow + Listarry[0] + spacebtw
                formattedbottomrow = formattedbottomrow + hypentobeadded * len(Listarry[0]) + spacebtw
            else:
                formattedtoprow = formattedtoprow + Listarry[0] + spacebtw
                formattedmiddlerow = formattedmiddlerow + Listarry[1] + spacebtw
                formattedbottomrow = formattedbottomrow + hypentobeadded * len(Listarry[0]) + spacebtw
                print(f'Length Top Row + :{len(Listarry[0])}')
                print(f'Length middle Row + :{len(Listarry[1])}')
        elif row.find('-') > 0:
            Listarry = row.split('-')
            Listarry[0] = Listarry[0].strip()
            Listarry[1] = '- ' + Listarry[1].strip()
            if len(Listarry[0]) < len(Listarry[1]):
                res = len(Listarry[1]) - len(Listarry[0])
                spacetobeadded = ' ' * res
                formattedtoprow = formattedtoprow + spacetobeadded + Listarry[0] + spacebtw
                formattedmiddlerow = formattedmiddlerow + Listarry[1] + spacebtw
                formattedbottomrow = formattedbottomrow + hypentobeadded * len(Listarry[1]) + spacebtw
            elif len(Listarry[0]) > len(Listarry[1]):
                #print(f'First Negative index {Listarry[0]} and length {len(Listarry[0])}')
                #print(f'Second Negative index {Listarry[1]} and length {len(Listarry[1])}')
                res = len(Listarry[0]) - len(Listarry[1])
                #print(f'Length of space to be appended {res}')
                spacetobeadded = ' ' * res
                #print(f'Length of space to be appended {len(spacetobeadded)}')
                formattedmiddlerow = formattedmiddlerow + spacetobeadded + Listarry[1] + spacebtw
                formattedtoprow = formattedtoprow + Listarry[0] + spacebtw
                formattedbottomrow = formattedbottomrow + hypentobeadded * len(Listarry[0]) + spacebtw
                #print(formattedtoprow)
                #print(formattedmiddlerow)
            else:
                formattedtoprow = formattedtoprow + Listarry[0] + spacebtw
                formattedmiddlerow = formattedmiddlerow + Listarry[1] + spacebtw
                formattedbottomrow = formattedbottomrow + hypentobeadded * len(Listarry[0]) + spacebtw
            #print(f'Length Top Row - :{len(Listarry[0])}')
            #print(f'Length middle Row - :{len(Listarry[1])}')

    print(formattedtoprow)
    print(formattedmiddlerow)
    print(formattedbottomrow)
    return problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])}')
