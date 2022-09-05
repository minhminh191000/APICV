from app import app ,db
# from controller.TestController import *



class ViewController:
    
    def index(self):
        return 'hello word'
    def hello(self,name):
        print("hello ", name)
        return 'hello' + name
    def score(self, score):
        return "Score is : " + str(score)

viewcontroller = ViewController()

app.add_enpoint('/view','view',viewcontroller.index)


