
import random
def play_hangman():

  # List of words for the game (only 6-letter words)
  word_list = ['banana', 'orange', 'cherry']

  # Select a random word from the list
  word_to_guess = random.choice(word_list)

  # Create a list with underscores representing the letters in the word
  hidden_word = ['_'] * 6

  # Number of allowed mistakes
  mistakes_left = 6

  # List to keep track of guessed letters
  guessed_letters = []

  # Hangman visualization: the stages of the hangman drawing
  hangman_visual = [
      '''
      -----
      |   |
      |
      |
      |
      |
      ''',
      '''
      -----
      |   |
      |   O
      |
      |
      |
      ''',
      '''
      -----
      |   |
      |   O
      |   |
      |
      |
      ''',
      '''
      -----
      |   |
      |   O
      |  /|
      |
      |
      ''',
      '''
      -----
      |   |
      |   O
      |  /|\ 
      |
      |
      ''',
      '''
      -----
      |   |
      |   O
      |  /|\ 
      |  /
      |
      ''',
      '''
        -----
      |   |
      |   O
      |  /|\ 
      |  / \  
      |
      ''',
      '''
        -----
      |   
      |
      |  \O/
      |   | 
      |  / \  
      '''
  ]

  print("🎮 Welcome to Hangman!\n")

  # Game loop: keep asking the player to guess until they win or run out of guesses
  while mistakes_left > 0 and '_' in hidden_word:
      # Display the current state of the word and remaining guesses
      print(f'Word to guess: {" ".join(hidden_word)}')
      print(f'Remaining guesses: {mistakes_left}')
      print(hangman_visual[6 - mistakes_left])  # Display the hangman image

      # Prompt the player for a guess
      guess = input('Guess a letter: ').strip().lower()

      # Check if the letter is valid
      if len(guess) != 1 or not guess.isalpha():
              print("❗ Please enter a single letter.\n")
              continue

      # Check if the letter has been guessed already
      if guess in guessed_letters:
          print("⛔ You've already guessed that letter.\n")
          continue

      # Add the guess to the list of guessed letters
      guessed_letters.append(guess)

      # Check if the guessed letter is in the word
      if guess in word_to_guess:
          print(f'✅ Good guess! The letter {guess} is in the word.')
          # Reveal the correctly guessed letter in the hidden word
          for index, letter in enumerate(word_to_guess):
              if letter == guess:
                  hidden_word[index] = guess
      else:
          print(f'❌ Sorry, the letter {guess} is not in the word.')
          mistakes_left -= 1  # Decrease the number of remaining guesses

  # Check if the player won or lost
  if '_' not in hidden_word:
      print(f'\n🎉 Congratulations! You guessed the word: {word_to_guess}')
      print(hangman_visual[7])
  else:
      print(f'\n💀Sorry, you lost! The correct word was: {word_to_guess}')
      print(hangman_visual[6 - mistakes_left])
