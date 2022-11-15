#randomizes JWE dinosaur selection, skins and genes.

#add toggle for canon skins?

import random
import pygame

pygame.init()

''' DISPLAY SECTION '''
display_width = 300
display_height = 500
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_orange = (255,128,0)
orange = (200,100,0)
yellow = (200,200,0)
bright_yellow = (255,255,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('JWE2 Randomizer Tool')
clock = pygame.time.Clock()
bg=pygame.image.load('jwe2bg.png')

#List that decides dinosaur tiers in park by number of total species desired.
tls=[0,1,2,3,4,5,3,4,2,5,1,3,4,5,2,3,4,3,2,1,2,4,3,5,1,3,2,4,5,0,3,1,2,4,5,3,3,1,4,4,5,4,3,2,1,0,1,2,3,4,5,4,3,2,1,0,1,2,3,4,5,4,3,2,1,0,1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2,3,4,5,4,3,5,3,5,3,5,3,5,3,5,3]
#traditional type distro based on JP novel/film and a bit of JWorld
#tradition=['LC','ceratopsian','sauropod','Orn','SH','SC','SC','pterosaur','stegosaurid','Orn','small','small','MC','ankylosaurid','SC','small','MC','Aq','SH','SH','medium','large','ceratopsian','pterosaur','LC','sauropod','ceratopsian','SC','SC','ceratopsian','LC','ceratopsian','sauropod','Orn','SH','SC','SC','SC','pterosaur','stegosaurid','Orn','small','small','MC','small','ankylosaurid','MC','Aq','SH','SH','medium','large','ceratopsian','pterosaur','LC','sauropod','ceratopsian','SC','SC','ceratopsian']
tradition=['LC','ceratopsian','sauropod','Orn','SC','SH','SC','pterosaur','stegosaurid','MC','small','medium','small','Orn','SM','ankylosaurid','SC','ceratopsian','Aq','SH','pterosaur','LC','MC','sauropod','medium','small','large','SH','SC','Orn','LC','ceratopsian','sauropod','Orn','SC','SH','SC','pterosaur','stegosaurid','MC','small','medium','small','Orn','SM','ankylosaurid','SC','ceratopsian','Aq','SH','pterosaur','LC','MC','sauropod','medium','small','large','SH','SC','Orn']
#roster by dino types in game
balance=['pterosaur','sauropod','ceratopsian','carnosaur','ankylosaurid','coelurosaur','hadrosaur','stegosaurid','plesiosaurid','primitive','ornithomimid','pachy','ornithopod','raptor','spinosaurid','mosasaurid','ceratosaurid','hybrid','ichthyosaurid','pterosaur','sauropod','ceratopsian','carnosaur','ankylosaurid','coelurosaur','hadrosaur','stegosaurid','pterosaur','sauropod','ceratopsian','pterosaur','sauropod','ceratopsian','carnosaur','ankylosaurid','coelurosaur','hadrosaur','stegosaurid','plesiosaurid','primitive','ornithomimid','pachy','pterosaur','sauropod','ceratopsian','carnosaur','ankylosaurid','coelurosaur','hadrosaur','stegosaurid','plesiosaurid','primitive','ornithomimid','pachy','ornithopod','raptor','spinosaurid','mosasaurid','ceratosaurid','hybrid']

skins=['SD','DV','GSD','CV','SH','LR','QM','YR','Sv','AR','MF','GRB']
patterns=['Ra','Ch','Li','Pu','Pa','Pe']

#check tls numbers
#n0=0
#n1=0
#n2=0
#n3=0
#n4=0
#n5=0
#for i in tls:
#    if i == 0:
#        n0+=1
#    elif i == 1:
#        n1+=1
#    elif i == 2:
#        n2+=1
#    elif i == 3:
#        n3+=1
#    elif i == 4:
#        n4+=1
#    elif i == 5:
#        n5+=1
#print(n0,n1,n2,n3,n4,n5)

#alphabet mode base
alphabet={}

#store dino data here
dinodict={}

#open csv file with raw data, add to list for now
templist=[]
f=open('JWEstats.csv')
for line in f.readlines():
    #print(line)
    templist.append(line.split('\n')[0].split(','))
f.close()

#open config
global ban,cap,mode
ban=[]
force=[]
cap=15
mode='True Random' 
name='run1.txt'
f=open('config.txt')
blank=False
for line in f.readlines():
    if line[0] != '#' and line != '\n':
        l2=line.split(':')
        #print(l2)
        if l2[0] == 'MODE':
            if len(l2[1])>0:
                if l2[1][0]==' ':
                    l2[1]=l2[1][1:]
                mode=l2[1].split('\n')[0]
        if l2[0] == 'NAME':
            if len(l2[1])>0:
                if l2[1][0]==' ':
                    l2[1]=l2[1][1:]
                name=l2[1].split('\n')[0]+'.txt'
        if l2[0] == 'TARGET':
            if len(l2[1])>0:
                if l2[1][0]==' ':
                    l2[1]=l2[1][1:]
                cap=int(l2[1].split('\n')[0])
        if l2[0] == 'BANLIST':
            if len(l2[1])>0:
                if l2[1][0]==' ':
                    l2[1]=l2[1][1:]
                l2a=l2[1].split('\n')[0]
                l3=l2a.split(',')
                ban=l3
        if l2[0] == 'FORCED':
            if len(l2[1])>0:
                if l2[1][0]==' ':
                    l2[1]=l2[1][1:]
                l2a=l2[1].split('\n')[0]
                l3=l2a.split(',')
                force=l3
        if l2[0] == 'BLANK':
            if len(l2[1])>0:
                if l2[1][0]==' ':
                    l2[1]=l2[1][1:]
                if l2[1] == 'True' or l2[1] == 'true' or l2[1] == 'True\n' or l2[1] == 'true\n':
                    blank=True
                    
f.close()

if blank: #if blank pattern has been allowed, add to pattern list
    patterns.append('Bl')
    
#extract data header
headers=templist[0]
templist.pop(0)
#print(headers)

#make and populate dictionary
list2=[]
for entry in templist:
    list2.append(entry)
for entry in templist:
    for banned in ban: #do banned here, or perform on dict?
        if banned in entry:
            z=0
            for forced in force:
                if forced in entry and forced != '':
                    z=1
            if z == 0:
                list2.remove(entry)
for entry in list2: 
    dinodict[entry[0]]={}
    if entry[0][0] not in alphabet:
        alphabet[entry[0][0]]=0
    for x in range(len(headers)):
        dinodict[entry[0]][headers[x]]=entry[x]  

for keys in list2:
    key=keys[0]
    canons=dinodict[key]['CANONICITY'].split(';')
    #print(canons)
    for banned in ban:
        if banned in canons:
            z=0
            for forced in force:
                if forced in canons and forced != '':
                    z=1
            if z == 0:
                try:
                    del dinodict[key]
                except:
                    nope='already removed'
                    
for key in dinodict:
    #print(key)
    gen=[]
    nums=int(dinodict[key]['GENES'])
    #print(key,nums)
    genb2=[0,0,0,0,0,0,0,0,0,0]
    for j in range(nums):
        k=random.randint(0,9)
        if genb2[k] < 3:
            genb2[k]+=1
        else:
            l=0
            while l == 0:
                k2=random.randint(0,9)
                if genb2[k2] < 3:
                    genb2[k2]+=1
                    l=1
    for gene in genb2:
        if gene == 0:
            gen.append('A')
        elif gene == 1:
            gen.append('C')
        elif gene == 2:
            gen.append('G')
        elif gene == 3:
            gen.append('T')
    #print(gen)
    dinodict[key]['GENOME']=('').join(gen)
    skin2=[]
    pat=random.choice(patterns)
    for sk in skins:
        if sk != '':
            skin2.append(sk+'/'+pat)
    for sk in dinodict[key]['SKINS'].split(';'):
        if sk != '':
            skin2.append(sk)
    dinodict[key]['COSMETIC']=random.choice(skin2)
      
keys=(list(dinodict))       

random.shuffle(keys)
#print(keys)

# generate species list with F species
species=[]
#for tier in tls[0:cap]:
#    for key in keys:
#        if int(dinodict[key]['TIER'])==tier and key not in species:
#            species.append(key)
#            break
##print(species)

#filter these further based on banlist and forced
bal2=balance[0:cap]
trad2=tradition[0:cap]

if mode == 'True Random':
    while len(species) < cap+1:
        for tier in tls:
            for key in keys:
                if int(dinodict[key]['TIER'])==tier and key not in species:
                    species.append(key)
                    break
                if len(species) > cap-1:
                    break
            if len(species) > cap-1:
                break
        break

elif mode == 'Alphabet':
    while len(species) < cap+1:
        for tier in tls:
            for key in keys:
                if int(dinodict[key]['TIER'])==tier and key not in species:
                    if alphabet[key[0]]==0:
                        alphabet[key[0]]=1
                        species.append(key)
                        break
                if len(species) > cap-1:
                    break
            if len(species) > cap-1:
                break
        break

elif mode == 'Balanced':
    while len(species) < cap+1:
        for tier in tls:
            for key in keys:
                if int(dinodict[key]['TIER'])==tier and key not in species and dinodict[key]['CLASS'] in bal2:
                    species.append(key)
                    bal2.remove(dinodict[key]['CLASS'])
                    break
                if len(species) > cap-1:
                    break
            if len(species) > cap-1:
                break
        break
    #repeat in case we missed a few
    if len(species) < cap+1 and len(bal2) > 0:
        while len(species) < cap+1:
            for tier in tls:
                for key in keys:
                    if int(dinodict[key]['TIER'])==tier and key not in species and dinodict[key]['CLASS'] in bal2:
                        species.append(key)
                        bal2.remove(dinodict[key]['CLASS'])
                        break
                    if len(species) > cap-1:
                        break
                if len(species) > cap-1:
                    break
            break

elif mode == 'Traditional':
    #print(trad2)
    while len(species) < cap+1:
        for tier in tls:
            for key in keys: #for a given dino...
                parms=[] #what params does it meet...
                if dinodict[key]['CLASS'] == 'ceratopsian' or dinodict[key]['CLASS'] == 'stegosaurid' or dinodict[key]['CLASS'] == 'ankylosaurid':
                    parms.append(dinodict[key]['CLASS'])
                parms.append(dinodict[key]['SIZE'])
                if dinodict[key]['SIZE'] == 'small' and dinodict[key]['DIET'] == 'plant':
                    parms.append('SH')
                if dinodict[key]['SIZE'] == 'small' and dinodict[key]['DIET'] == 'meat':
                    parms.append('SC')
                if dinodict[key]['SIZE'] == 'medium' and dinodict[key]['DIET'] == 'meat' or key == 'Baryonyx' or key == 'Suchomimus':
                    parms.append('MC')
                if dinodict[key]['SIZE'] == 'medium' or dinodict[key]['SIZE'] == 'small':
                    parms.append('SM')
                if dinodict[key]['SIZE'] == 'large' and dinodict[key]['DIET'] == 'meat' or key == 'Spinosaurus':
                    parms.append('LC')
                if dinodict[key]['CLASS'] == 'ichthyosaurid' or dinodict[key]['CLASS'] == 'mosasaurid' or dinodict[key]['CLASS'] == 'plesiosaurid':
                    parms=['Aq']
                if dinodict[key]['SIZE'] != 'small':
                    if dinodict[key]['CLASS'] == 'hadrosaur' or dinodict[key]['CLASS'] == 'ornithopod':    
                        parms.append('Orn')
                if dinodict[key]['CLASS'] == 'pterosaur':
                    parms=['pterosaur']
                if dinodict[key]['CLASS'] == 'sauropod' and dinodict[key]['SIZE'] == 'large':
                    parms.append('sauropod')
                d=0
                for parm in parms: #check each param...
                    if parm in trad2: #if it matches list...
                        if int(dinodict[key]['TIER'])==tier and key not in species: #if not a repeat and is correct tier...
                            #print(key,parm)
                            species.append(key)
                            trad2.remove(parm)
                            d=1
                            break
                if d==1:
                    break
                if len(species) > cap-1:
                    break
            if len(species) > cap-1:
                break
        break
    #repeat in case we missed a few
    if len(species) < cap+1 and len(trad2) > 0:
        while len(species) < cap+1:
            for tier in tls:
                for key in keys: #for a given dino...
                    parms=[] #what params does it meet...
                    if dinodict[key]['CLASS'] == 'ceratopsian' or dinodict[key]['CLASS'] == 'stegosaurid' or dinodict[key]['CLASS'] == 'ankylosaurid':
                        parms.append(dinodict[key]['CLASS'])
                    parms.append(dinodict[key]['SIZE'])
                    if dinodict[key]['SIZE'] == 'small' and dinodict[key]['DIET'] == 'plant':
                        parms.append('SH')
                    if dinodict[key]['SIZE'] == 'small' and dinodict[key]['DIET'] == 'meat':
                        parms.append('SC')
                    if dinodict[key]['SIZE'] == 'medium' or dinodict[key]['SIZE'] == 'small':
                        parms.append('SM')
                    if dinodict[key]['SIZE'] == 'medium' and dinodict[key]['DIET'] == 'meat' or key == 'Baryonyx' or key == 'Suchomimus':
                        parms.append('MC')
                    if dinodict[key]['SIZE'] == 'large' and dinodict[key]['DIET'] == 'meat' or key == 'Spinosaurus':
                        parms.append('LC')
                    if dinodict[key]['CLASS'] == 'ichthyosaurid' or dinodict[key]['CLASS'] == 'mosasaurid' or dinodict[key]['CLASS'] == 'plesiosaurid':
                        parms=['Aq']
                    if dinodict[key]['SIZE'] != 'small':
                        if dinodict[key]['CLASS'] == 'hadrosaur' or dinodict[key]['CLASS'] == 'ornithopod':    
                            parms.append('Orn')
                    if dinodict[key]['CLASS'] == 'pterosaur':
                        parms=['pterosaur']
                    if dinodict[key]['CLASS'] == 'sauropod' and dinodict[key]['SIZE'] == 'large':
                        parms.append('sauropod')
                    d=0
                    for parm in parms: #check each param...
                        if parm in trad2: #if it matches list...
                            if int(dinodict[key]['TIER'])==tier and key not in species: #if not a repeat and is correct tier...
                                #print(key,parm)
                                species.append(key)
                                trad2.remove(parm)
                                d=1
                                break
                    if d==1:
                        break
                    if len(species) > cap-1:
                        break
                if len(species) > cap-1:
                    break
            break    
#for key in dinodict:
   # print(key)
#read in save file
nameL=[]
cosmo=[]
gens=[]
try:
    f=open(name,'r')
    for line in f.readlines():
        #print(line)
        if line != '':
            nameL.append(line.split('\n')[0].split(',')[0])
            cosmo.append(line.split('\n')[0].split(',')[1])
            gens.append(line.split('\n')[0].split(',')[2])
    #print(nameL,gens,cosmo)
    f.close()
except:
    nul=0

if len(nameL)==len(species):
    species=nameL
    for spec in range(len(nameL)):
        dinodict[nameL[spec]]['COSMETIC']=cosmo[spec]
        dinodict[nameL[spec]]['GENOME']=gens[spec]
else:
    f=open(name,'w+')
    for dino in species:
        a=dinodict[dino]['COSMETIC']
        b=dinodict[dino]['GENOME']
        f.write(dino+','+a+','+b+'\n')
    f.close()
    
#generate UI
''' TEXT FUNCTION SECTION '''
def text_objects(text, font, color=white): 
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_display(textlist, x, y, direx='down', delay=0, fontsize=30, font='arialbold', color=None): #temporarily displayed text
    n=-1
    if direx == 'up':
            n=1
    for text in textlist:
        if direx == 'down':
            n+=1
        if direx == 'up':
            n-=1
        largeText = pygame.font.SysFont(font,int(fontsize))
        if color == None:
            TextSurf, TextRect = text_objects(text, largeText)
        else:
            TextSurf, TextRect = text_objects(text, largeText,color=color)
        TextRect.center = ((x),(y+30*n))
        gameDisplay.blit(TextSurf, TextRect)
    #pygame.display.update()
    pygame.time.delay(delay)
   
''' BUTTON FUNCTION SECTION '''
def btn(label,hover,x,y,w,h,ic,ac,x2=400,y2=500,fontsize=20,font='arialbold',fontsize2=28,font2='arialbold',color=None,tc=None,action=None,paramlist=None): #universal button code, for color fill buttons.
#hover=hover over text, label is button label, xywh=button coords, x2y2=hover text coords, ic,ac = colors or image
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if ic == 'image':
            gameDisplay.blit(ac, (x,y))
        else:
            pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        text_display(hover,x2,y2,'down',0,fontsize2,font2,color)
        event=pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN and action != None and paramlist != None:
            action(paramlist)
        elif event.type == pygame.MOUSEBUTTONDOWN and action != None and paramlist == None:
            action()
            
    else:
        if ic == 'image':
            gameDisplay.blit(ac, (x,y))
        else:
            pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont(font,fontsize)
    textSurf, textRect = text_objects(label, smallText)
    if tc != None:
        textSurf, textRect = text_objects(label, smallText,tc)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)            

global roster
roster=[]
      
def game_intro():
    intro = True
    global roster
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0,0))
        largeText = pygame.font.SysFont("arial bold",20)
        TextSurf, TextRect = text_objects('Mode: '+mode+', Roster: '+str(cap), largeText)
        TextRect.center = ((display_width/2),(10))
        #TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        x,y=0,20
        for t in ['0 Stars','1 Stars','2 Stars','3 Stars','4 Stars']:
            btn(t,'',x,y,60,25,green,bright_green,action=showdino,paramlist=t)
            x+=60
            if x >= 800:
                x=0
                y+=50
        for n in range(len(roster)):
            TextSurf, TextRect = text_objects(roster[n], largeText)
            TextRect.center = ((display_width/2),(55+15*n))
            gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        
def showdino(stars):  #update global variable with dinos to be displayed under game intro.
    global roster
    tierz=int(stars[0])+1
    if int(stars[0]) == 0:
        for dino in species:
            if dinodict[dino]['TIER']=='0':
                genet=dinodict[dino]['GENOME']
                if dino+' '+dinodict[dino]['COSMETIC']+' '+genet not in roster:
                    roster.append(dino+' '+dinodict[dino]['COSMETIC']+' '+genet)  
    for dino in species:
        if dinodict[dino]['TIER']==str(tierz):
            genet=dinodict[dino]['GENOME']
            if dino+' '+dinodict[dino]['COSMETIC']+' '+genet not in roster:
                roster.append(dino+' '+dinodict[dino]['COSMETIC']+' '+genet)
    
'''STARTING THE GAME SECTION'''

game_intro()
pygame.quit()
quit()
