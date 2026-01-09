print("Program started")

import matplotlib.pyplot as plt

# ✅ Example: automatic feedbacks (could be input() or read from file)
feedbacks = [
    "Food was very tasty and delivery was fast",
    "Worst experience ever, food was cold",
    "Service was okay, nothing special",
    "Amazing food quality and friendly staff",
    "Delivery was late and food taste was bad",
    "Not bad, but not great",
    "Excellent service and delicious food",
    "Very poor experience"
]

# Positive & Negative words for automatic decision
positive_words = [
    "good", "great", "excellent", "amazing", "tasty", "delicious",
    "fast", "friendly", "awesome", "love", "loved"
]

negative_words = [
    "bad", "worst", "poor", "slow", "cold", "late",
    "terrible", "rude", "hate"
]

# Counters
positive_count = 0
neutral_count = 0
negative_count = 0

# Results
results = []

# ✅ Automatic sentiment classification
for feedback in feedbacks:
    text = feedback.lower()
    score = 0

    for word in positive_words:
        if word in text:
            score += 1
    for word in negative_words:
        if word in text:
            score -= 1

    if score > 0:
        sentiment = "Positive 😊"
        positive_count += 1
    elif score < 0:
        sentiment = "Negative 😞"
        negative_count += 1
    else:
        sentiment = "Neutral 😐"
        neutral_count += 1

    results.append((feedback, sentiment))

# ✅ Print all feedbacks and sentiments
print("\nFeedback Analysis:")
for feedback, sentiment in results:
    print(f"Feedback: {feedback}")
    print("Sentiment:", sentiment)
    print()

# ✅ Final decision automatically
print("Summary:")
print("Positive:", positive_count)
print("Neutral:", neutral_count)
print("Negative:", negative_count)

if positive_count >= negative_count:
    print("\n✅ FINAL DECISION: SERVICE IS OK")
else:
    print("\n❌ FINAL DECISION: SERVICE NEEDS IMPROVEMENT")

# ✅ Plot the sentiment counts
sentiments = ["Positive", "Neutral", "Negative"]
counts = [positive_count, neutral_count, negative_count]

plt.bar(sentiments, counts, color=['green', 'blue', 'red'])
plt.xlabel("Sentiment")
plt.ylabel("Number of Feedbacks")
plt.title("Zomato User Feedback Sentiment Analysis")
plt.show()