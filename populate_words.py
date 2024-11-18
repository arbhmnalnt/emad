from words.models import Word

# List of 25 easy English words for Level 1
words = [
    "Apple", "Banana", "Car", "Dog", "Elephant", "Fish", "Grass", "House",
    "Ice", "Juice", "Kite", "Lamp", "Mountain", "Nest", "Orange", "Pencil",
    "Queen", "River", "Sun", "Tree", "Umbrella", "Van", "Window",
    "Xylophone", "Zoo"
]

# Language and level settings
language = "en"
level = 1

# Populate the database
for word in words:
    Word.objects.create(text=word, language=language, level=level)

print(f"Successfully added {len(words)} words to the database!")
