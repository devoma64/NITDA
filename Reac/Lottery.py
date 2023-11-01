# import random

# class LotteryGame:
#      def __init__(self) -> None:
#           # creating a list containing numbers and letters
          
#           self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
          
#           self.winning_criteria = [1,2, 'A', 'B']
#           self.attempts = 0
#           self.found_winner = False
          
#      def play(self):
#           while not self.found_winner:
#                # randomly select 4 elements from the list
#                selected_elements = random.sample(self.data, 4)
#                self.attempts +=1
               
#                # check if the selected elements match the wining criteria
#                if selected_elements == self.winning_criteria:
#                     self.found_winner = True
     
#      def report_result(self):
#           print(f"Congratulations! You've won a prize after {self.attempts} attempts.")
          
# lottery = LotteryGame()

# lottery.play()


# lottery.report_result()
          
          
import random

data =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

selected_numbers = random.sample(data, 4)

print("Selected elements:", selected_numbers)

winning_criteria = [1,2, 'A', 'B']

if any(element in selected_numbers for element in winning_criteria):
     print("Congratulations! You've won a prize!")
else:
     print("Sorry, no winning ticker this time.")
          