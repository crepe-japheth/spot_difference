import random
import math

class SpotDifferenceGame:
    
    def __init__(self) -> None:
        self.data = [['O', '0'], ['l', '1'], ['u', 'v']]
        self.number_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
        self.level = 1
        self.col = 3
        self.row = 3
        self.game_ended = False
        self.first_level = True

    def start_message(self):
        print('Input cell number (e.g. A1) of the different character.')


    def section_message(self):
        print('level: ' + str(self.level))

    def view_question(self):
        choice_data = random.randint(0, 2)
        mistake_number = random.randint(0, (self.col * self.row) - 1)
        question = self.data[choice_data]
        print(question)
        i = 0
        j = 0
        question_str1 = '/|'
        question_str2 = '--'
        while i < self.col:
            question_str1 += self.number_data[i] + ''
            question_str2 += '-'
            i += 1
        print(question_str1)
        print(question_str2)
        i = 0
        while i < self.row:
            question_str = str(i + 1) + '|'
            while j < self.col:
                if (i * self.col + j) == mistake_number:
                    question_str += question[1]
                else:
                    question_str += question[0]
                j += 1
            print(question_str)
            i += 1
            j = 0
        return mistake_number
    

    def change_input_number(self, input_str):
        str_data = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                    'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12}
        input_str_split = list(input_str)
        col_number = str_data[input_str_split[0]]
        row_number = int(input_str_split[1]) - 1
        input_number = row_number * self.col + col_number
        return input_number
    
    
    def is_correct_number(self, mistake_number, input_number):
        if mistake_number == input_number:
            return True
        else:
            return False
        
    def view_result(self, is_correct, mistake_number):
        if is_correct:
            print('Correct!')
            self.level += 1
            self.level_up()
        else:
            print('Wrong')
            print('Correct answer is ' + self.change_string(mistake_number))
            if self.level <= 2:
                if self.first_level:
                    self.is_first_level()
                self.level -= 1
                self.row = 3
                self.col = 3
            else:
                self.level -= 2
                self.row -= 1
                self.col -= 1

    # check if the level is on first level to play two times
    def is_first_level(self):
        if self.level == 1:
            self.first_level = False
            self.play()

    def change_string(self, number):
        col_number = number % self.col
        row_number = math.floor(number / self.col) + 1
        string = self.number_data[col_number] + str(row_number)
        return string
    
    #this increases the level each time you input correct answer
    def level_up(self):
        if self.level % 2 == 0:
            self.col += 1
        if self.level % 2 != 0:
            self.row += 1
    
    def play(self):
        if self.level >= 1 and self.level <= 13:
            self.section_message()
            mistake_number = self.view_question()
            choice = input('(e.g. A1) or (clear) to End Game: ')
            if choice == 'clear':
                self.game_ended = True
            else:
                print('Debug: choice = ' + choice)
                input_number = self.change_input_number(choice)
                print('Debug: input_number = ' + str(input_number))
                is_correct = self.is_correct_number(mistake_number, input_number)
                self.view_result(is_correct, mistake_number)
        else:
            self.game_ended = True


game = SpotDifferenceGame()
while not game.game_ended:
    game.play()