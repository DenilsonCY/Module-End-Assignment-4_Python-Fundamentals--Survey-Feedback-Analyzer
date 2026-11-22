# Step 1: Preloaded Feedbacks
feedback_data = {
    'S No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        'Very GOOD Service!!!',
        'poor support, not happy',
        'GREAT experience! will come again.',
        'okay not okay...',
        'BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

# Step 2: Add More Feedbacks
more_count = int(input("How many more feedbacks do you want to add? "))
next_sno = max(feedback_data['S No']) + 1 if feedback_data['S No'] else 1

for i in range(more_count):
    print(f"\n--- Adding Feedback #{i + 1} ---")
    name = input("Enter Name: ")
    fb_text = input("Enter Written Feedback: ")
    rating = int(input("Enter Rating (1-5): "))

    feedback_data['S No'].append(next_sno)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(fb_text)
    feedback_data['Rating'].append(rating)
    next_sno += 1

# Step 3: Text Cleaning
cleaned_feedbacks = []
for text in feedback_data['Feedback']:
    # Remove punctuation (., !, ?)
    for ch in ['.', ',', '!', '?']:
        text = text.replace(ch, ' ')
    # Replace multiple spaces with single space & strip leading/trailing spaces & lowercase
    cleaned_text = ' '.join(text.split()).lower()
    cleaned_feedbacks.append(cleaned_text)

feedback_data['Feedback'] = cleaned_feedbacks

# Step 4: Word Count Insights
def count_word_in_feedbacks(word):
    target = word.lower()
    count = 0
    for fb in feedback_data['Feedback']:
        words_in_fb = fb.split()
        if target in words_in_fb:
            count += 1
    return count

print("\n--- Word Count Insights ---")
print('Feedbacks containing "good":', count_word_in_feedbacks("good"))
print('Feedbacks containing "poor":', count_word_in_feedbacks("poor"))
print('Feedbacks containing "excellent":', count_word_in_feedbacks("excellent"))

# Step 5: Final Summary & Insights
print("\n--- Final Cleaned feedback_data ---")
print(feedback_data)

avg_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print(f"\nAverage Rating: {avg_rating:.2f}")

# Longest comment in terms of word count
longest_fb = max(feedback_data['Feedback'], key=lambda x: len(x.split()))
print(f"Longest Feedback ({len(longest_fb.split())} words): {longest_fb}")

# Unique words across all feedbacks
unique_words = sorted({w for fb in feedback_data['Feedback'] for w in fb.split()})
print("\nUnique Words across all feedbacks:")
print(unique_words)

# Optional: Sort feedbacks by rating (highest to lowest) using zip() and sorted()
sorted_entries = sorted(
    zip(feedback_data['Rating'], feedback_data['S No'], feedback_data['Name'], feedback_data['Feedback']),
    key=lambda item: item[0],
    reverse=True
)

print("\n--- Feedbacks Sorted by Rating (High to Low) ---")
for rating, sno, name, fb in sorted_entries:
    print(f"Rating: {rating} | S No: {sno} | Name: {name} | Feedback: {fb}")
