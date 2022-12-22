class testscore:
    def setscore(self,first_score, second_score  ):
        self.first_score = first_score
        self.second_score = second_score
    def addscores(self):
        result = self.first_score + self.second_score
        return result
    def mulscores(self):
        result = self.first * self.second
        return result
    def average_scores(self):
        result = (self.first_score + self.second_score)/2
        return result
    def compare_scores(self):
        if self.first_score > self.second_score:
            print(f"first score({self.first_score}) is higher than second score")
        else:
            print(f"second score({self.second_score}) is higher than first score")

a = testscore()
a.setscore(80, 90)
a.average_scores() 
a.addscores()
a.mulscores()
a.compare_scores()
