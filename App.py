import random


max_number_of_exercises = 100

def input(message):
  while True:
    try:
      return int(input(message))
    except: pass
    
    
def main():
  print("Python Multiplication Table Learner 1.0\n")
  
  
  message = "Select number of exercises, maximum {}".format(max_number_of_exercises)
  number_of_exercises = min(input(message), max_number_of_messages)
  
  exercises = [(0, 1), (3, 4)]
  
  for exercise in exercises:
    print(exercise)
  
  

if __name__ == "__main__":
  main()
