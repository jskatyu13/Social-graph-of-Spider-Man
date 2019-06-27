#read the text file as the data for create the social network of spiderman
import numpy as np
f = open('porgat.txt', 'r')
x = f.readlines()

#create the hero/character list
hero_list={}
for index in range(6487):
    if index==0:
        continue
    else:
        hero=x[index].split(' ',1)
        hero_list[int(hero[0])]=hero[1][0:-1]

#check if the ID 5306 is spider-man
spidermanID=5306
print("The ID of %s is %d."% (hero_list[spidermanID],spidermanID))

#create the comic book list
comic_list={}
for index in range(6487,19429):
    comic=x[index].split(' ',1)
    comic_list[int(comic[0])]=comic[1]
#create the collaboration matrix, which includes the number of heros/characters as rows and the number of comic books as columns
edges_list=np.zeros((len(hero_list),len(comic_list)))
for index in range(19430,len(x)):
    edges=x[index].split(' ')
    for ix in range(1,len(edges)):
        edges_list[int(edges[0])-1][int(edges[ix])-6487]=1   

#using matrix multiplication to create the hero/character-hero/character matrix for the computation of spiderman number
hero_hero_list=np.zeros((len(hero_list),len(hero_list)))
edges_list_tp=np.transpose(edges_list)
hero_hero_list=np.matmul(edges_list,edges_list_tp)

# calculate the number of characters which have a spiderman number of 1

spiderman_number1=np.zeros(len(hero_list))
count_num0=0
count_num1=0
for ix in range(len(hero_list)):
    if ix==spidermanID-1:
        spiderman_number1[ix]=spidermanID
    elif hero_hero_list[spidermanID-1][ix]>0:
        spiderman_number1[ix]=1

for val in spiderman_number1:
    if val==1:
        count_num1+=1
    elif val==spidermanID:
        count_num0+=1
print("the number of characters which have a spider-man number of 0: %d" %count_num0)
print("the number of characters which have a spider-man number of 1: %d" %count_num1)

# calculate the number of characters which have a spiderman number of 2
spiderman_number2=np.zeros(len(hero_list))
count_num2=0
for ix in range(len(hero_list)):
    if spiderman_number1[ix]==0:
        for ix_in1 in range (len(spiderman_number1)):
            if (hero_hero_list[ix][ix_in1]>0 and spiderman_number1[ix_in1]>0):
                spiderman_number2[ix]=2
for val in spiderman_number2:
    if val==2:
        count_num2+=1

print("the number of characters which have a spider-man number of 2: %d" %count_num2)

# calculate the number of characters which have a spiderman number of 3
spiderman_number3=np.zeros(len(hero_list))
count_num3=0
for ix in range(len(hero_list)):
    if spiderman_number1[ix]==0 and spiderman_number2[ix]==0:
        for ix_in2 in range (len(spiderman_number2)):
            if (hero_hero_list[ix][ix_in2]>0 and spiderman_number2[ix_in2]>0):
                spiderman_number3[ix]=3
for val in spiderman_number3:
    if val==3:
        count_num3+=1
print("the number of characters which have a spider-man number of 3: %d" %count_num3)

# calculate the number of characters which have a spiderman number of 4
spiderman_number4=np.zeros(len(hero_list))
count_num4=0
for ix in range(len(hero_list)):
    if spiderman_number1[ix]==0 and spiderman_number2[ix]==0 and spiderman_number3[ix]==0:
        for ix_in3 in range (len(spiderman_number3)):
            if (hero_hero_list[ix][ix_in3]>0 and spiderman_number3[ix_in3]>0):
                spiderman_number4[ix]=4
for val in spiderman_number4:
    if val==4:
        count_num4+=1

print("the number of characters which have a spider-man number of 4: %d" %count_num4)

# calculate the number of characters which have a spiderman number from 0-3
spider_123=spiderman_number1+spiderman_number2+spiderman_number3
sum=count_num0+count_num1+count_num2+count_num3
print("the number of characters which have a spiderman number of 0-3: %d" %sum)

#create a hash table to store the spider number for each character
spiderman_num={}
for ix in range(len(spider_123)):
    if spider_123[ix]==spidermanID:
        spiderman_num[ix+1]=0
    elif spider_123[ix]==1:
        spiderman_num[ix+1]=1
    elif spider_123[ix]==2:
        spiderman_num[ix+1]=2
    elif spider_123[ix]==3:
        spiderman_num[ix+1]=3
    elif spider_123[ix]==0:
        spiderman_num[ix+1]=None

#function to print the character's appearance in comic books and spider-man number 
def print_hero_spiderman_num(heroID):
    print ("%s, appears in %d comic books and the spider-man number of this character is %s." %(hero_list[heroID], hero_hero_list[heroID-1][heroID-1], spiderman_num[heroID]))

# read the input of character ID to print the character name and this character's spider man number
while True:
    heroID =int(raw_input("What is the ID of the character that you are interested in? (1-6486) "))
    if heroID<=0 or heroID>6486:
        print("error in the character ID")
        break
    else:
        print_hero_spiderman_num(heroID)

