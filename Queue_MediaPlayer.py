from random import randint
import time




class queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.count = 0


    def enqueue(self, x):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(x)
        self.count += 1
        

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        if len(self.s1) == 0:
            print("Queue is empty")

        name = self.s1[-1]
        self.s1.pop()
        self.count -= 1
        return name




    

class Track:
    def __init__(self, title = None, artist = None):
        self.title = title
        self.artist = artist
        self.length = randint(5,10)

class MediaPlayerQueue(queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()


    def add_track(self, track):
        self.enqueue(track)


    def play(self):
        while self.count > 0:
            current_track_node = self.dequeue()
            print("Now playing {} - by {}".format(current_track_node.title,current_track_node.artist))
            time.sleep(current_track_node.length)

track1 = Track("Chúng ta rồi sẽ hạnh phúc", "Jack97")
track2 = Track("Tại vì sao?", "MCK")
track3 = Track("Không thể say", "HIEUTHUHAI")
track4 = Track("Champion", "Obito")


media_player = MediaPlayerQueue()

media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.play()






        
            
            
    
