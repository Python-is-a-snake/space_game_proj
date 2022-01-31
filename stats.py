class Stats():
    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

#Changing stats here
    def reset_stats(self):
        self.guns_left = 2 #LIVES HERE
        self.score = 0