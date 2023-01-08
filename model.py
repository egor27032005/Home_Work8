def init(stat, sern):
    global st
    global ser
    st=stat
    ser=sern

def teach_sear():
    lines = [] 
    with open ('teachers.txt', 'rt') as myfile:
        for myline in myfile: 
            lines.append(myline)
        for j in range(9):
            if ser in lines[j]:
                return(lines[j+1])
                    
def init2(subjet):
    global sub
    sub=subjet

def less_sear():
    lines = [] 
    with open ('lessons.txt', 'rt') as myfile:
        for myline in myfile: 
            lines.append(myline)
        for j in range(9):
            if sub in lines[j]:
                return (lines[j+1])
