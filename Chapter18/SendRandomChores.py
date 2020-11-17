""" 
write a program that takes a list of people’s email addresses and a list of chores that need to be done and randomly assigns chores to people. Email each person their assigned chores. If you’re feeling ambitious, keep a record of each person’s previously assigned chores so that you can make sure the program avoids assigning anyone the same chore they did last time. For another possible feature, schedule the program to run once a week automatically.

Here’s a hint: if you pass a list to the random.choice() function, it will return a randomly selected item from the list. Part of your code could look like this:

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
randomChore = random.choice(chores)
chores.remove(randomChore)    # this chore is now taken, so remove it
 """
import os, ezgmail, random, schedule, time

ezgmail.init()#set up our email tokens for your gmail dev account stores token in same folder
chorelist_src = r'config\choreList.txt'
emailList_src = r'config\emailList.txt'
prev_run = [" ", " "]#set up to compare to the last run we have done


def readEmailList():#read our emails from config folder
    with open(emailList_src, 'r') as e:
        emailList = e.read().splitlines() 
        return emailList

def readChoreList():#read chores from config.txt
    with open(chorelist_src, 'r') as e:
        choreList = e.read().splitlines() 
        return choreList

def sendOutEmails(jobs):#send out some emails with the assigned chores
    for email, chore in jobs.items():
        ezgmail.send( email, 'Chore', "Your task should you choose to accept it is\n" + chore + '\nthanks for your cooperation')

def assignChores(choreList, emailList):#assign some chores and check to make sure they didn't have them last weeek
    random.shuffle(choreList)
    check = checkList(choreList)
    if check == False:
        shuffle = dict(zip(emailList, choreList))
        prev_run = choreList
        return shuffle
    if check == True:
        assignChores(choreList, emailList)

def checkList(check):# check the chores compared to the last run
    for i in range(len(prev_run)):
        if prev_run[i] == check[i]:
            return True
        else:
            return False

def run():
    print('~~Shuffling The Chores and Sending Emails~~')
    eList = readEmailList()
    cList = readChoreList()
    jobs = assignChores(cList, eList)
    sendOutEmails(jobs)


schedule.every().monday.at("23:22").do(run)#when do we want this job to run

while True:
    schedule.run_pending()
    time.sleep(1)
