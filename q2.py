import random

# Define the updated dataset
news_data = [
    ("The tech company unveiled a new smartphone model.", "Technology"),
    ("A major software update is rolling out next week.", "Technology"),
    ("New AI technology is revolutionizing the industry.", "Technology"),
    ("A cybersecurity breach affected thousands of users.", "Technology"),
    ("The startup secured significant venture capital funding.", "Technology"),
    ("A famous artist is exhibiting their work at the museum.", "Arts"),
    ("The annual film festival starts this weekend.", "Arts"),
    ("A new musical is premiering on Broadway.", "Arts"),
    ("The gallery is showcasing contemporary sculptures.", "Arts"),
    ("A renowned writer released their latest novel.", "Arts"),
    ("The city is hosting a major food festival.", "Lifestyle"),
    ("A new fitness trend is taking over gyms nationwide.", "Lifestyle"),
    ("The travel industry is seeing a surge in bookings.", "Lifestyle"),
    ("A popular fashion brand launched a new collection.", "Lifestyle"),
    ("Home renovation projects are becoming increasingly popular.", "Lifestyle"),
    ("The local team won the championship game last night.", "Sports"),
    ("A new world record was set at the Olympics.", "Sports"),
    ("The football season is starting next week.", "Sports"),
    ("A famous athlete announced their retirement today.", "Sports"),
    ("A new sports complex is being built in the city.", "Sports"),
]

# Define the updated classes
classes = ["Technology", "Arts", "Lifestyle", "Sports"]

# Random model to predict a class
def random_predict():
    return random.choice(classes)

# Calculate the accuracy
correct_predictions = 0

# Iterate through the dataset and make predictions
for news, true_class in news_data:
    predicted_class = random_predict()
    if predicted_class == true_class:
        correct_predictions += 1

# Calculate the accuracy as a percentage
accuracy = correct_predictions / len(news_data)
accuracy_percentage = accuracy * 100

# Print the accuracy
print(f"Accuracy of the random model: {accuracy_percentage:.2f}%")
