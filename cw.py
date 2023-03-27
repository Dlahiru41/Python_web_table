#------necessary libraries for the program
from prettytable import PrettyTable
import random
import time
import sys
#------------------------------------------------

yesOrNo=[]#---------result array (STORE YES OR NO)-----
grid=[]#------------store random numbers
while True:#-------user input validation
    try:
        inputs= input('Enter space-separated integers: ').split()#-----take two inline inputs
        inputs = [int(item) for item in inputs]
        if inputs[0]<3 or inputs[0]>9:#--------check whether the inputs are in the correct range
            print('inputs shold be in the range 3-9')
            continue
        elif inputs[1]<3 or inputs[1]>9:
            print('inputs shold be in the range 3-9')
            continue
        else:
            break
    except ValueError:#------if user doen't input a integer error will be thrown
        print('inputs should be integers')
        continue
    except IndexError:#-----if user inputs more than two inputs
        break

    
lenoftheInputs=len(inputs)#--------if user give inputs 
#--------------------------------------------------
if lenoftheInputs==0 or lenoftheInputs==1 :
    for i in range(0,5):
        row=[]
        for i in range(0,5):
            n=random.randint(10,99)#-----create a random number in between range 0-99
            row.append(n)
        randomIndex=random.randint(0,len(row)-1)#-------randomly selects a index of row array
        row[randomIndex]=' '#------assign blank 
        grid.append(row)

    
    yesOrNo=[]
    for i in range(0,5):#-----------checks whether there is blank shells
        count=0
        for n in range(0,5):
            if grid[n][i]==' ':
                count=1
        if count==1:
            yesOrNo.append('NO')
        else:
            yesOrNo.append('OK')
    grid.append(yesOrNo)#-------append the resultarray to the main grid

    
#------------------------------------------------#------if user doesn't enter inputs 
else:
    for i in range(0,inputs[0]):
        row=[]
        for i in range(0,inputs[1]):
            n=random.randint(10,99)#-----create a random number in between range 0-99
            row.append(n)
        randomIndex=random.randint(0,len(row)-1)#-------randomly selects a index of row array
        row[randomIndex]=' '#------assign blank 
        grid.append(row)

        
    yesOrNo=[]
    for i in range(0,inputs[1]):#-----------checks whether there is blank shells
        count=0
        for n in range(0,inputs[0]):
            if grid[n][i]==' ':
                count=1
        if count==1:
            yesOrNo.append('NO')
        else:
            yesOrNo.append('OK')

    grid.append(yesOrNo)#-------append the resultarray to the main grid

for i in grid:#---------print the full grid
    for a in i:
        print(a, end='\t')
    print('\n')

x = PrettyTable()#------------print the same grid array in a pretty table
for i in grid:
    x.add_row(i)

print(x)
#--------------------create a html file and writes in it
result_string = """<HTML>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
<body>
    <table>\n"""
for i in grid:
    result_string += "        <tr>\n            "
    for j in i:
        result_string += "<td>%s</td>" %j
    result_string += "\n        </tr>\n"
result_string += """    </table>
</body>
</HTML>"""
display = open("table.html", 'w')
display.write(result_string)
display.close()

#----------------------------------------file handling
#randomData = ("Some Random stuff")
t,s = str(time.time()).split('.')
filename = t+".txt"#---------creates an unique name for a file everry time the program run
print ("writing to", filename)


#--------------writes the data in to the file
stdoutOrigin=sys.stdout
sys.stdout=open(filename,"a")
for i in grid:
    for a in i:
        print(a, end='\t')
    print('\n')
sys.stdout.close()#flush can close the IO object
sys.stdout=stdoutOrigin


