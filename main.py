import random
import data

class WordDataLoader:
    def __init__(self, allowed_guesses_file_path: str, possible_target_words_file_path: str):
        self.allowed_guesses_file_path = allowed_guesses_file_path
        self.possible_target_words_file_path = possible_target_words_file_path

    # Returns each line from a text file as a list
    def read_words_from_file(self, file_path: str) -> set:
        with open(file_path, "r") as file:
            words = set()

            for line in file.readlines():
                words.add(line.strip())

            return words
    
    # Returns a tuple consisting of the list of allowed words a player can guess and a list of target words (possible answers)
    def load_all_word_data(self) -> tuple[set, list]:
        allowed_guesses = self.read_words_from_file(self.allowed_guesses_file_path)  # Leave as a set to allow for faster lookup of words
        possible_target_words = list(self.read_words_from_file(self.possible_target_words_file_path))
        return allowed_guesses, possible_target_words

class WordleBot:
    def __init__(self, allowed_guesses: set, possible_target_words: list):
        self.allowed_guesses = allowed_guesses
        self.possible_target_words = possible_target_words
    
    def load_feedback_combinations(self, ):
        with open(data.combinations.txt, "r") as file:
            feedback_combinations = []

            for line in file.readlines():
                feedback_combinations.append(line)

    def calculate_feedback_probability(self):
        pass

    def calculate_guess_entropy(self):
        pass

    def generate_guess_entropy_dict(self):
        pass

    def choose_best_guess(self):
        pass

    
    def simulate_games(self):
        pass

class WordleGame:
    def __init__(self, allowed_guesses: set, possible_target_words: list):
        self.allowed_guesses = allowed_guesses
        self.possible_target_words = possible_target_words
        self.target_word = self.choose_target_word()
        self.current_guess = ""
        self.attempts = 0
        self.game_over = False
        self.won = False
    
    # Returns a target word
    def choose_target_word(self) -> str:
        return random.choice(self.possible_target_words)
    
    # Returns the feedback from a given guess, represented using symbols (G = green, Y = yellow, B = grey)
    def get_feedback(self, current_guess: str, target_word: str) -> list:
        feedback = ["B", "B", "B", "B", "B"]

        for i in range(len(current_guess)):
            if current_guess[i] == target_word[i]:
                feedback[i] = "G"
                target_word[i] = None  # Deals with duplicate letters in target word

        for i in range(len(current_guess)):
            if feedback[i] != "G" and current_guess[i] in target_word:
                feedback[i] = "Y"
                target_word[i] = None  # Deals with duplicate letters in target word

        return feedback
    
    def play_game(self, player: str) -> list:
        MAX_ATTEMPTS = 6
        
        while not self.game_over and self.attempts < MAX_ATTEMPTS:
            self.attempts += 1

            if player == "human":
                current_guess = input("Input guess: ")
            elif player == "bot":
                current_guess = wordle

            feedback = self.get_feedback(self.current_guess, self.target_word)
            bot.receive_feedback(self.current_guess, feedback)

            if self.current_guess == self.target_word:
                self.target_word_guessed = True
                self.game_over = True
            elif self.attempts >= MAX_ATTEMPTS:
                self.game_over = True

        if not self.game_over:
            print("The game has ended prematurely.")

if __name__ == "__main__":
    wordle_bot = WordleBot
    results = wordle_bot.play_game()




        