import time


class ChildPet(object):
    def __init__(self, childName, petName, energy=5, hunger=0,
                 hygiene=10, sleep=10, points=0, lastTime=None):
        self.childName=childName
        self.petName=petName
        self.energy=float(energy)
        self.hunger=float(hunger)
        self.hygiene=float(hygiene)
        self.sleep=float(sleep)
        self.points=int(points)
        self.lastTime=float(lastTime) or time.time()
        self.updateStats()

    def doAction(self, action):
        """
        Does an action with the pet - feed, wash or sleep
        Stats then updates accordingly
        """
        if action=="feed":
            self.hunger-=3
            self.hunger=max(self.hunger, 0)
            self.updateStats()
            return "Thanks for feeding me"
        elif action=="wash":
            self.hygiene+=4
            self.hygiene=min(self.hygiene, 10)
            self.updateStats()
            return "Thanks for washing me"
        elif action=="sleep":
            self.sleep+=6
            self.sleep=min(self.sleep, 10)
            self.updateStats()
            return "Zzzzzzzzzz..."
        elif action=="play":
            if self.energy>=1:
                self.energy-=1
                self.updateStats()
                return "That was fun!"
            return "I've not got enough energy"

    def __str__(self):
        """
        Returns attributes as a string for use in .txt file
        """
        response=str(self.childName)+"\n"+\
        str(self.petName)+"\n"+\
        str(self.energy)+"\n"+\
        str(self.hunger)+"\n"+\
        str(self.hygiene)+"\n"+\
        str(self.sleep)+"\n"+\
        str(self.points)+"\n"+\
        str(self.lastTime)
        return response

    def updateStats(self):
        """
        Updates pet's stats
        Hunger, hygiene and sleep degrade over time
        Energy recharges over time
        """
        #Rates at which attributes decay (in hours)
        hungerRate = 1
        hygieneRate = 2
        sleepRate = 2.5
        #Calculates time difference between last update in hours
        now=time.time()
        timeDifference=(now-self.lastTime)/(1000*60*60)
        #Updates stats and writes to .txt file
        self.hunger=min(self.hunger+timeDifference/hungerRate,10)
        self.hygiene=max(self.hygiene-timeDifference/hygieneRate,0)
        self.sleep=max(self.sleep-timeDifference/sleepRate,0)
        self.energy=min(self.energy+timeDifference/0.1,5)
        #write(self)