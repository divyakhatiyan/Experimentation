## Purpose of this Programme is to format the input List into required format
## Input: arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
## Output: 
###    32      3801      45      123
### + 698    -    2    + 43    +  49
### -----    ------    ----    -----

def validations(problems):
    records = []

    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        for record in problems:
            if record.find('+') > 0:
                records = record.split('+')
                #print(f'Length of record: {len(records[0].strip())}')
                #print(f'Length of record: {len(records[1].strip())}')
                print(f'record is {records[0]}')
                print(f'record is {records[1]}')
                if len(records[0].strip()) > 4 or len(records[1].strip()) > 4:
                    return "Error: Numbers cannot be more than four digits."
                elif records[0].strip().isnumeric() == False or records[1].strip().isnumeric() == False:
                    print(f'Number is: {records[0]}')
                    print(f'Number is: {records[1]}')
                    return "Error: Numbers must only contain digits."
                elif len(records) > 2:
                    return "Error: More than two operands are not allowed."
            elif record.find('-') > 0:
                records = record.split('-')
                print(f'Length of record: {len(records[0].strip())}')
                print(f'Length of record: {len(records[1].strip())}')
                if len(records[0].strip()) > 4 or len(records[1].strip()) > 4:
                    return "Error: Numbers cannot be more than four digits."
                elif records[0].strip().isnumeric() == False or records[1].strip().isnumeric() == False:
                    print(f'Number is: {records[0]}')
                    print(f'Number is: {records[1]}')
                    return "Error: Numbers must only contain digits."
                    #print(f'record is {records[0]}')
                    #print(f'record is {records[1]}')
                elif len(records) > 2:
                    return "Error: More than two operands are not allowed."

                #print(f'record is {records[0]}')
                #print(f'record is {records[1]}')
            elif record.find('+') == -1 or record.find('-') == -1:
                #print("Error: Operator must be '+' or '-'.")
                return "Error: Operator must be '+' or '-'."
    return "NONE"

def arithmetic_arranger(problems, show_answers=False):
    formattedtoprow = ''
    formattedmiddlerow = ''
    formattedbottomrow = ''
    formattedsumrow = ''
    spacebtw = '    '
    hypentobeadded = '-'

    if validations(problems) == "NONE":

        for row in problems:

            if row.find('+') > 0:
                Listarry = row.split('+')
                Listarry[0] = Listarry[0].strip()
                sum = int(Listarry[0]) + int(Listarry[1])
                #print(f'Sum is: {sum}')
                Listarry[1] = '+ ' + Listarry[1].strip()

                if len(Listarry[0]) < len(Listarry[1]):
                   res = len(Listarry[1]) - len(Listarry[0])
                   spacetobeadded = ' ' * res
                   formattedtoprow = formattedtoprow + spacetobeadded + Listarry[0] + spacebtw
                   formattedmiddlerow = formattedmiddlerow + Listarry[1] + spacebtw
                   formattedbottomrow = formattedbottomrow + hypentobeadded * len(Listarry[1]) + spacebtw
                   space_append_last_row = len(hypentobeadded * len(Listarry[1])) - len(str(sum))
                   #print(f'Length of formatted bottom row {len(Listarry[1])}')
                   #print(f'Length of formatted bottom row {len(str(sum))}')
                   #print(f'space_append_last_row {space_append_last_row}')
                   formattedsumrow = formattedsumrow + (space_append_last_row * ' ') + str(sum) + spacebtw
                   #print(f'formatted sum row {formattedsumrow}')
                elif len(Listarry[0]) > len(Listarry[1]):
                    res = len(Listarry[0]) - len(Listarry[0])
                    spacetobeadded = ' ' * res
                    formattedmiddlerow = formattedmiddlerow + spacetobeadded + Listarry[1] + spacebtw
                    formattedtoprow = formattedtoprow + Listarry[0] + spacebtw
                    formattedbottomrow = formattedbottomrow + hypentobeadded * len(Listarry[0]) + spacebtw
                    space_append_last_row = len(hypentobeadded * len(Listarry[0])) - len(str(sum))
                    formattedsumrow = formattedsumrow + (space_append_last_row * ' ') + str(sum) + spacebtw
                    #print(f'formatted sum row {formattedsumrow}')
                else:
                    formattedtoprow = formattedtoprow + Listarry[0] + spacebtw
                    formattedmiddlerow = formattedmiddlerow + Listarry[1] + spacebtw
                    formattedbottomrow = formattedbottomrow + hypentobeadded * len(Listarry[0]) + spacebtw
                    space_append_last_row = len(hypentobeadded * len(Listarry[0])) - len(str(sum))
                    formattedsumrow = formattedsumrow + (space_append_last_row * ' ') + str(sum) + spacebtw
                    #print(f'formatted sum row {formattedsumrow}')
                    #print(f'Length Top Row + :{len(Listarry[0])}')
                    #print(f'Length middle Row + :{len(Listarry[1])}')
            elif row.find('-') > 0:
                Listarry = row.split('-')
                Listarry[0] = Listarry[0].strip()
                sub = int(Listarry[0]) - int(Listarry[1])
                #print(f'Subtraction is: {sub}')
                Listarry[1] = '- ' + Listarry[1].strip()
                #formattedsumrow = formattedsumrow + str(sub) + spacebtw
                if len(Listarry[0]) < len(Listarry[1]):
                    res = len(Listarry[1]) - len(Listarry[0])
                    spacetobeadded = ' ' * res
                    formattedtoprow = formattedtoprow + spacetobeadded + Listarry[0] + spacebtw
                    formattedmiddlerow = formattedmiddlerow + Listarry[1] + spacebtw
                    formattedbottomrow = formattedbottomrow + hypentobeadded * len(Listarry[1]) + spacebtw
                    space_append_last_row = len(hypentobeadded * len(Listarry[1])) - len(str(sub))
                    formattedsumrow = formattedsumrow + (space_append_last_row * ' ') + str(sub) + spacebtw
                    #print(f'formatted sum row {formattedsumrow}')
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
                    space_append_last_row = (len(hypentobeadded * len(Listarry[0]))) - len(str(sub))
                    formattedsumrow = formattedsumrow + (space_append_last_row * ' ') + str(sub) + spacebtw
                    #print(f'formatted sum row {formattedsumrow}')
                    #print(formattedtoprow)
                    #print(formattedmiddlerow)
                else:
                    formattedtoprow = formattedtoprow + Listarry[0] + spacebtw
                    formattedmiddlerow = formattedmiddlerow + Listarry[1] + spacebtw
                    formattedbottomrow = formattedbottomrow + hypentobeadded * len(Listarry[0]) + spacebtw
                    space_append_last_row = len(hypentobeadded * len(Listarry[0])) - len(str(sub))
                    formattedsumrow = formattedsumrow + (space_append_last_row * ' ') + str(sub) + spacebtw
                    #print(f'formatted sum row {formattedsumrow}')
                #print(f'Length Top Row - :{len(Listarry[0])}')
                #print(f'Length middle Row - :{len(Listarry[1])}')

    else:
        return validations(problems)
    #print(formattedtoprow)
    #print(formattedmiddlerow)
    #print(formattedbottomrow)
    #print(formattedsumrow)
    if show_answers == True:
        output = (formattedtoprow + '\n' + formattedmiddlerow + '\n' + formattedbottomrow + '\n' + formattedsumrow)
    else:
        output = (formattedtoprow + '\n' + formattedmiddlerow + '\n' + formattedbottomrow)
    return output


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])}')
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["1 + 2", "1 - 98015"],True)}')
print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49","126 + 79","126 - 79"], True)}')
print(f'\n{arithmetic_arranger(["11 * 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], True)}')
