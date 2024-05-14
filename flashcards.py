import random
import time
# import pyttsx3
from dictionaries.updated_data import data

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# Flatten the list of dictionaries to a single dictionary
flash_cards = {list(item.keys())[0]: list(item.values())[0] for item in data}

# Generate a list of characters based on their frequency
characters = [char for char, details in flash_cards.items() for _ in range(details['frequency'])]

# Initialize the counter
counter = 0

# def speak(text):
#     """Function to speak the provided text."""
#     engine.say(text)
#     engine.runAndWait()

while True:
    # Randomly select a character/phrase
    flash_card = random.choice(characters)

    # Extract details from the dictionary
    card_details = flash_cards[flash_card]

    # Increment the counter
    counter += 1

    # Display the character/phrase, pinyin, example, translation, example translation, and usage notes
    print("=" * 50)
    print(f"Flashcard #{counter}")
    print(f"Character/Phrase  : {flash_card}")
    print(f"Pinyin            : {card_details['pinyin']}")
    print(f"Translation       : {card_details['translation']}")
    print(f"Example           : {card_details['example']}")
    print(f"Example Translation: {card_details['example_translation']}")
    print(f"Usage Notes       : {card_details['usage_notes']}")
    print("=" * 50 + "\n")

    # Speak the pinyin aloud
    # speak(card_details['pinyin'])

    # Wait for the user to press a key to continue
    input("Press enter to continue...")