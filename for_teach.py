import model
def for_lesson(objekt):
    lines = [] 
    with open ('lessons.txt', 'rt') as myfile:
        for myline in myfile: 
            lines.append(myline)
        for j in range(9):
            if objekt in lines[j]:
                print (lines[j+1])