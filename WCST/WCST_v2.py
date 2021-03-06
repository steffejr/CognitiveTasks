import numpy as np
from psychopy import visual,core,monitors,event,gui, data
import os
import sys
import time
import wx

# #################
# Store info about the experiment session
expName = u'WCST'  # from the Builder filename that created this script
task = ''
expInfo = {u'session': u'01', u'Participant ID': u'9999999'}

expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
if len(sys.argv) > 1:
    #tempFile.write("Entered if clause\n")
    #tempFile.write('%s\n'%(sys.argv[2]))
    expInfo['Participant ID'] = sys.argv[1]
    #tempFile.write('%s\n'%(sys.argv[1]))
    #tempFile.write('%s\n'%(sys.argv[2]))

    PartDataFolder = sys.argv[2]
    Tag = '1'
else:
    dlg = gui.DlgFromDict(dictionary=expInfo)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    DataFolder = "../../data"
    PartDataFolder = 'unorganized'
    OutDir = os.path.join(DataFolder, PartDataFolder)
    if not os.path.exists(OutDir):
        os.mkdir(OutDir)
    Tag = '1'
    PartDataFolder = OutDir
    
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = os.path.join(PartDataFolder, '%s_%s_%s_%s_%s.csv' % (expInfo['Participant ID'],expName, task, Tag, expInfo['date']))
print(filename)
FontSize = 40

DisplayChoiceTime = 0.25 # Was 1
FeedbackDisplayTime = 1.5 # Was 2
InstructTime = 2 
# #################
#V Load up the Card Order
FileName = '../WCST/CardOrder.csv'
CardOrder = np.genfromtxt(FileName, delimiter=',')

INSTRUCTIONS = ('Select one of the four cards displayed at the top of the screen such '
                              +'that the selected card matches the card displayed at the bottom of the screen. '
                              +'The cards can be matched based on three dimensions - color, number of objects '
                              +'or the shape of the objects they display. You will be given feedback whether the '
                              +'selected card was RIGHT or WRONG. Use the feedback to determine which '
                              +'dimension is targeted by feedback and based on it select the right card. The '
                              +'targeted dimension may change from time to time without notice.\n\nPress any key to begin')

X = 0
Y = 1
def pointInTriangle(t1,t2,t3,pt):
    """ determines whether point PT is located inside
        triangle with vertices at points T1, T2 and T3
    """
    def sign(p1,p2,p3):
        return (p1[X]-p3[X])*(p2[Y]-p3[Y])-(p2[X]-p3[X])*(p1[Y]-p3[Y])
    b1=sign(pt,t1,t2)<0
    b2=sign(pt,t2,t3)<0
    b3=sign(pt,t3,t1)<0
    return b1==b2 and b2==b3

def drawTriangle(M,t,value=1):
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if pointInTriangle(t[0],t[1],t[2],(i,j)):
                M[i,j]=value
    return M

def drawCircle(M,pos,radius,value=1):
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if np.sqrt((i-pos[X])**2+(j-pos[Y])**2)<radius:
                M[i,j]=value
    return M
def drawStar(M,pos,nv, ocr,icr):
    """ pos - location of the star
        nv - number of vertices
        ocr - radius of outer circle
        icr - radius of inner circle
    """
    M=drawCircle(M,pos,icr)
    phi=np.linspace(0,2*np.pi,nv+1)[:-1]
    ops=np.array([np.cos(phi)*ocr,np.sin(phi)*ocr])+np.array(pos,ndmin=2).T
    phi+= phi[1]/2.0
    ips=np.array([np.cos(phi)*icr,np.sin(phi)*icr])+np.array(pos,ndmin=2).T
    for i in range(phi.size):
        M=drawTriangle(M,[ips[:,i-1],ips[:,i],ops[:,i]])
    return M


class Experiment():
    def __init__(self):


        
        # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
        # #################
        #myDlg = gui.Dlg(title="Wisconsin Card Sorting Task",pos=(SZ[0]/2,SZ[1]/2))
        #myDlg.addField('Subject ID:',1)
        #myDlg.addField('Number of Trials:',128)
        #myDlg.show()#show dialog and wait for OK or Cancel
        #vpInfo = myDlg.data
        #self.vp = vpInfo[0]

        self.win = visual.Window(size=SZ,units='height',fullscr=True, monitor='testMonitor', winType = "pyglet",allowGUI=False, waitBlanking=True)        
        self.mouse = event.Mouse(True, None, win=self.win)#(True,None,self.win)

        self.cards = []
        self.elems = []
        ElementSize = 0.05
        for i in range(4):
            self.cards.append(visual.Rect(self.win,CARDW,CARDH,fillColor='white',
                pos = ((i-1.5)*(CARDX+CARDW),CARDY),lineColor='black',interpolate=False, units = 'height'))
 
#        # # Add the probe card to the screen
            self.elems.append(visual.ElementArrayStim(self.win,nElements=4,sizes=ElementSize,colors='black',
                fieldPos = TPOS,elementTex=None, units = 'height'))            

        # Add the probe card to the screen
        self.cards.append(visual.Rect(self.win,CARDW,CARDH,fillColor='white',
            pos = TPOS,lineColor='black',interpolate=False, units = 'height'))
        self.elems.append(visual.ElementArrayStim(self.win,nElements=4,sizes=ElementSize,colors='black',
            fieldPos = TPOS,elementTex=None, units = 'height'))            
        
        # Make the piles
        #for i in range(4):
        self.cards.append(visual.Rect(self.win,CARDW,CARDH,fillColor='grey',
                        pos = DiscardPOS,lineColor='black',interpolate=False, units = 'height'))
        self.elems.append(visual.ElementArrayStim(self.win,nElements=4,sizes=ElementSize,colors='grey',
                        fieldPos = DiscardPOS,elementTex=None, units = 'height'))
            

        self.text = visual.TextStim(self.win,pos=FPOS,height=0.08, units = 'height')
        #if not os.path.exists('data'):
        #    os.makedirs('data')
        #fname = os.path.join('data', 'wcst_s%03d_%s.csv' % (self.vp, time.strftime("%Y%m%d-%H%M%S")))




    def runTrial(self, t, target):
        clock = core.Clock()

        # Randomly create the choice cards
        # Four cards need to be created, each card has 3 attributes
        #choice=[]
        #for i in range(3):
        #    choice.append(np.random.permutation(4))
        #choice=(np.array(choice).T).tolist()
        # Setup the four cards to be fixed
        choice = [[0,1,0],[1,2,1],[3,3,2],[2,0,3]]
        
        
        # The attributes map onto to these numbers:
        # CLRS=['red','green','blue','orange']
        # SHAPES=[CIRCLE,SQUARE,STAR,CROSS]
        #target=np.random.randint(4,size=3) # Create the attributes of the target
        
        # These are randomly chosen providing three numbers between 0 and 3 which are:
        # colorm shape, number of items on the card
        # display problem
        
        # Put all cards on the screen
        for i in range(4):
            self.cards[i].draw()
            self.elems[i].setColors(CLRS[choice[i][0]])
            self.elems[i].setMask(SHAPES[choice[i][1]])
            self.elems[i].setXYs(SPOS[choice[i][2]])
            self.elems[i].draw()
        # Put the test card on the screen (on the bottom)
        self.cards[4].setPos(TPOS)
        self.cards[4].draw()
        self.elems[4].setFieldPos(TPOS)
        self.elems[4].setColors(CLRS[target[0]])
        self.elems[4].setMask(SHAPES[target[1]])
        self.elems[4].setXYs(SPOS[target[2]])
        self.elems[4].draw()
        # Add piles of previous cards
        #for i in range(5,9):
        self.cards[5].draw()

        self.elems[5].draw()
        self.win.flip()

        # wait for response
        self.mouse.clickReset()
        while True:
            
            mkey,mtime = self.mouse.getPressed(getTime=True)
            if sum(mkey)>0:
                card = -1
                mpos = self.mouse.getPos()
                print(mpos)
                for i in range(4):
                    #if self.cards[i].contains(mpos):
                    if self.cards[i].contains(self.mouse):
                        card = i
                        mtime = mtime[0]
                if card>-1: break
                else: self.mouse.clickReset()
               
            theseKeys = event.getKeys(keyList=['1', '2','3','4','escape'])
            # dots still there at this point    
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0: 
                print(theseKeys[-1])
                card = int(theseKeys[-1]) - 1
                mtime = clock.getTime()
                break
                
        
        
        # display choice
        #self.cards[4].setPos((self.cards[card].pos[X],-1))
        #self.elems[4].setFieldPos((self.cards[card].pos[X],-1))
        print("choice was:")

        print(str(card))
        
        #self.cards[4+card+1].setPos((self.cards[card].pos[X],-1))
        #self.elems[4+card+1].setFieldPos((self.cards[card].pos[X],-1))
        self.cards[5].fillColor = self.cards[card].fillColor
        self.cards[5].setPos(DiscardPOS)
        self.elems[5].setFieldPos(TPOS)
        self.elems[5].setColors(CLRS[target[0]])
        self.elems[5].setMask(SHAPES[target[1]])
        self.elems[5].setXYs(SPOS[target[2]])
        self.elems[5].setFieldPos(DiscardPOS)
        # Dots are still there

        for i in range(4):
            self.cards[i].draw()
            self.elems[i].draw()
        
        
        #for i in range(5,9):
        self.cards[5].draw()
        self.elems[5].draw()
        # Display cards and choice  
        
        self.win.flip()
        
        core.wait(DisplayChoiceTime)
        # write self.output and display feedback
        self.output.write('%d,%d,%d,%0.3f,' % ( t+1, card+1, self.rule, mtime))
        if target[self.rule]==choice[card][self.rule]:
            self.text.setText('RIGHT')
            self.corstreak+=1
            self.output.write('1,')
        else:
            self.text.setText('WRONG')
            self.corstreak=0
            self.output.write('0,')

       
        for i in range(4):
            self.cards[i].draw()
            self.elems[i].draw()
            if i<4:self.output.write('%d,%d,%d,'%tuple(choice[i]))
        
        self.output.write('%d,%d,%d\n'%tuple(target))
        self.output.flush()
        self.text.draw()
        #for i in range(5,9):
        self.cards[5].draw()
        self.elems[5].draw()
        self.win.flip()
        core.wait(FeedbackDisplayTime)

#    def run(self, num_trials, rule_delta=10):
#        # Pick a number between 0 and 2: 0,1,2
#        self.rule=np.random.randint(3)
#        self.corstreak=0
#        for t in range(num_trials):
#            if self.corstreak>=rule_delta:
#                
#                sel=range(3)
#                sel.remove(self.rule)
#                self.rule=sel[np.random.randint(2)]
#            self.runTrial(t)
    def run(self, num_trials, rule_delta=10):
        #At the beginning reset the discard piles
        #for i in range(5,9):
        self.cards[5].fillColor = 'grey'
            
        self.elems[5].color = 'grey'
            
        self.cards[5].draw()
            #self.elems[i].draw()
        self.rule = 0
        self.corstreak = 0
        for t in range(num_trials):
            # Get the target card
            targetCard = [int(CardOrder[t,0]), int(CardOrder[t,1]), int(CardOrder[t,2])]
            print('Trial num=%d, Streak = %d, Rule = %d'%(t, self.corstreak, self.rule))
            if self.corstreak == rule_delta:
                #print('Trial num=%d, Rule = %d'%(t,self.rule))
                if self.rule == 2 :
                    self.rule = 0
                else:
                    self.rule += 1
            
            self.runTrial(t, targetCard)

            
    def instruct(self, inst_text, go_text):
        # inst = visual.TextStim(self.win, pos=(0,0), height=0.05, units = 'height', alignHoriz='center', wrapWidth=1.4)
        inst = visual.TextStim(self.win, pos=(0,0), height=1.4, units = 'deg', alignHoriz='center', wrapWidth=38)

        inst.setText(inst_text)
        inst.draw()
        self.win.flip()
        
        k = ['']
        KeyBoardCount = 0       
        while k[0] not in ['escape', 'esc'] and KeyBoardCount < 1:
            k = event.waitKeys()
            KeyBoardCount += 1
        inst.setText(go_text)
        inst.draw()
        self.win.flip()
                
        
        core.wait(InstructTime)
        inst.setText('')
        inst.draw()
        self.win.flip()
        core.wait(1)
        
    def ThankYou(self):
        ThankYou = visual.TextStim(self.win, pos = (0,0), height = 1.4, units = 'deg')
        ThankYou.setText('Thank You')
        ThankYou.draw()
        self.win.flip()
        core.wait(3)
        self.sin.flip()
        
    def CardInstruct(self):

        # inst = visual.TextStim(self.win, pos=(0,0), height=0.05, alignHoriz='center', wrapWidth=22, units = 'height')
        inst = visual.TextStim(self.win, pos=(0,0), height=1, alignHoriz='center', wrapWidth=22, units = 'deg')
        # Display the cards on the screen to allow the experimenter to provide 
        # verbal instructions
        choice = [[0,1,0],[1,2,1],[3,3,2],[2,0,3]]
        
        
        # The attributes map onto to these numbers:
        # CLRS=['red','green','blue','orange']
        # SHAPES=[CIRCLE,SQUARE,STAR,CROSS]
        target=np.random.randint(4,size=3) # Create the attributes of the target
        # These are randomly chosen providing three numbers between 0 and 3 which are:
        # colorm shape, number of items on the card
        # display problem
        for i in range(4):
            self.cards[i].draw()
            self.elems[i].setColors(CLRS[choice[i][0]])
            self.elems[i].setMask(SHAPES[choice[i][1]])
            self.elems[i].setXYs(SPOS[choice[i][2]])
            self.elems[i].draw()
        self.win.flip()
        k = ['']
        KeyBoardCount = 0       
        while k[0] not in ['escape', 'esc'] and KeyBoardCount < 1:
            k = event.waitKeys()
            KeyBoardCount += 1

        inst.setText('Starting the test...')
        inst.draw()
        self.win.flip()
        core.wait(1)
        inst.setText('')
        inst.draw()
        self.win.flip()
        core.wait(1)
        
        
        



# setup masks of different shape
N=128
mid=N/2-0.5

CIRCLE=np.ones((N,N))*-1
CIRCLE=drawCircle(CIRCLE,(mid,mid),N/2)

CROSS=np.ones((N,N))*-1
w=N/4
for i in range(CROSS.shape[0]):
    for j in range(CROSS.shape[1]):
        if i>mid-w/2 and i<mid+w/2 or j>mid-w/2 and j<mid+w/2 :
            CROSS[i,j]=1
STAR=np.ones((N,N))*-1
STAR=drawStar(STAR,(mid,mid),5,N/2,N/5)
SQUARE=np.ones((N,N))

TRIANGLE = drawTriangle(np.ones((N,N))*-1,[[0,0],[N,N/2-0.5],[0,N]])

SZ = (1280,1024)

# Settings
# MON=monitors.Monitor('dell', width=37.8, distance=50); MON.setSizePix(SZ)
##
TPOS=(0,-0.3)#(0,-9) # position of the target card
FPOS=(0, 0.15) #(0,3.8) # position of the feedback
CARDY=0.3 # 9 # vertical position of choice cards
PrevCARDY = 0
DiscardPOS = (0, PrevCARDY)
CARDX = 0.05# 1 # horizontal space between choice cards
CARDW=0.15# 4 # card width
CARDH=0.225# 6 # card height
CLRS=['red','green','blue','orange']
SHAPES=[CIRCLE,TRIANGLE,STAR,CROSS]

#SHAPES=[TRIANGLE,TRIANGLE,TRIANGLE,TRIANGLE]

SPOS = [[[0,0],[np.nan,np.nan],[np.nan,np.nan],[np.nan,np.nan]],
        [[0,CARDH/4.0],[0,-CARDH/4.0],[np.nan,np.nan],[np.nan,np.nan]],
        [[-CARDW/4.0,CARDH/3.0],[-CARDW/4.0,-CARDH/3.0],[CARDW/4.0,0],[np.nan,np.nan]],
        [[-CARDW/4.0,CARDH/4.0],[-CARDW/4.0,-CARDH/4.0],
         [CARDW/4.0,-CARDH/4.0],[CARDW/4.0,CARDH/4.0]]]

# #################
E = Experiment()
E.output = open(filename, 'w')
E.output.write('TrialNum,Card,Rule,RespTime,Correct,') 
# Write out the header 
E.output.write('Card01Color,Card01Shape,Card01Count,')
E.output.write('Card02Color,Card02Shape,Card02Count,')
E.output.write('Card03Color,Card03Shape,Card03Count,')
E.output.write('Card04Color,Card04Shape,Card04Count,')
E.output.write('ProbeColor,ProbeShape,ProbeCount\n')

E.instruct(INSTRUCTIONS+' practice.', 'Starting the practice...')
E.run(num_trials=12, rule_delta=3) 


E = Experiment()
E.output = open(filename, 'a')
E.output.write('TrialNum,Card,Rule,RespTime,Correct,') 
E.output.write('Card01Color,Card01Shape,Card01Count,')
E.output.write('Card02Color,Card02Shape,Card02Count,')
E.output.write('Card03Color,Card03Shape,Card03Count,')
E.output.write('Card04Color,Card04Shape,Card04Count,')
E.output.write('ProbeColor,ProbeShape,ProbeCount\n')
E.instruct('Remember: '+INSTRUCTIONS+' the test', 'Starting the test...')
E.CardInstruct()
E.run(num_trials=64, rule_delta=10)
E.ThankYou() 
E.output.close()
E.win.close()

    