import random
import time
import threading


# Python code for Dining philosophers
# tested under Python 2.6
 
class Phi(threading.Thread):
 
    running = True
    def __init__(self, num, leftfork, rightfork):               #initiate threads
        threading.Thread.__init__(self)
        self.num = num
        self.leftfork = leftfork
        self.rightfork = rightfork
 
    def run(self):
        while(self.running):
            time.sleep( random.uniform(20,50))                  #time before hungry
            print '%s is hungry and start waiting' % self.num
            self.dine()
 
    def dine(self):
        fork1, fork2 = self.leftfork, self.rightfork
 
        while self.running:
            fork1.acquire(True)
            occupy = fork2.acquire(False)
            if occupy: break
            fork1.release()
            print '%s swaps fork order, keep on waiting' % self.num  
            fork1, fork2 = fork2, fork1                         #pick up the other fork first next time
        else:
            return
 
        self.dining()                                           
        fork2.release()                                         #put down forks
        fork1.release()
 
    def dining(self):            
        print '%s starts eating '% self.num
        time.sleep(random.uniform(10,20))                       #time before finish eating, should less than time of thinking
        print '%s finishes eating and take a nap.' % self.num
 
def DiningPhilosophers():
    forks = [threading.Lock() for jj in range(5)]
    phi_nums = ('Phi1','Phi2','Phi3','Phi4', 'Phi5')
 
    phis= [Phi(phi_nums[ii], forks[ii%5], forks[(ii+1)%5]) for ii in range(5)]    
                                                                #choose fork next to them 
            
    Phi.running = True
    for num in phis: num.start()
    time.sleep(200)
    Phi.running = False
 
DiningPhilosophers()
