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
# 파이썬 메서드 이름으로 __init__를 사용하면 이 메서드는 생성자가 된다
# 생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.

a = testscore(70, 90)
a.addscores()
a.mulscores()
a.average_scores()
a.compare_scores()