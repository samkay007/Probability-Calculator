import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = list()
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
    

  def draw(self,number):
    balls = list()
    if (number > len(self.contents)):
      return (self.contents)
    else:
      for i in range(number):
        rand = random.randrange(len(self.contents))
        balls.append(self.contents[rand])
        self.contents.pop(rand)
      return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  total = 0

  for i in range(num_experiments):
    exp = copy.deepcopy(hat)
    draw = exp.draw(num_balls_drawn)
    draw_dict = dict()

    for i in draw:
      if i not in draw_dict:
        draw_dict[i] = 1
      else:
        draw_dict[i] = draw_dict[i] + 1
    print (draw_dict)

    test = 0     
    for key, value in expected_balls.items():
      if (key in draw_dict.keys()) and (value <= draw_dict[key]):
          test += 1

    if (test == len(expected_balls)):
      total +=1
        

      
  return(total/num_experiments)

  
