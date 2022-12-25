class testscore:
    def __init__(self,first_score, second_score  ):
        self.first_score = first_score
        self.second_score = second_score
    def setscore(self,first_score, second_score  ):
        self.first_score = first_score
        self.second_score = second_score
    def addscores(self):
        result = self.first_score + self.second_score
        return result
    def mulscores(self):
        result = self.first_score * self.second_score
        return result
    def average_scores(self):
        result = (self.first_score + self.second_score)/2
        return result
    def compare_scores(self):
        if self.first_score > self.second_score:
            print(f"first score({self.first_score}) is higher than second score")
        else:
            print(f"second score({self.second_score}) is higher than first score")

class moretestscore(testscore):
    def scorediff(self):
        if self.first_score > self.second_score:
            result = self.first_score - self.second_score
            return result
        else:
            result = self.second_score - self.first_score
            return result 

score = moretestscore(70, 80)

score.addscores()
score.mulscores()
score.average_scores()
score.compare_scores()