from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import random
import string

# # Read the CSV file
# df = pd.read_csv('lecture_6.csv')
#
# # print(df)
#
# def add_user(username: str, birth_year: int, gender, income, password=None):
#     new_row = {
#         "username": username,
#         "age": datetime.now().year - birth_year,
#         "gender": gender,
#         "income": income,
#         "password": password}
#     return new_row
#
# username = input("Enter your username: ")
# # Use try and except blocks to handle possible errors
# try:
#     birth_year = int(input("Which year were you born: "))
# except ValueError:
#     print("Invalid input. Please enter a numeric value.")
#     exit()
# # Validate the user input for gender
# gender = input("Are you male(m) or female(f)? ")
# if gender == "m":
#     gender = "man"
# elif gender == "f":
#     gender = "woman"
# else:
#     print("Invalid input. Please enter m or f.")
#     exit()
# # Use try and except blocks to handle possible errors
# try:
#     income = int(input("How much do you earn per week? "))
# except ValueError:
#     print("Invalid input. Please enter a numeric value.")
#     exit()
# password = input("What is your password? ")
#
#
# new_row = add_user(username=username, birth_year=birth_year, gender=gender, password=password, income=income)
#
# df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
# df.to_csv('lecture_6.csv', index=False)
#
# print("New row added to the csv file.")
# print(df)


# # Add a new column
# df['Height'] = [175, 180, 178, 176]
#
# # Write the modified dataframe back to CSV
# df.to_csv('lecture_6.csv', index=False)
#
# # To add a new row, you can use the `append` function
#
# new_row = {'Name':'Mark', 'Age':22, 'Height':183}
#
# df = df.append(new_row, ignore_index=True)
#
# # Write the modified dataframe back to CSV
# df.to_csv('lecture_6.csv', index=False)

































# Load the CSV data into a DataFrame
df = pd.read_csv('lecture_6_exam.csv')

print(df)

# Calculate basic statistics for both subjects
stats = df[['math', 'english']].describe()

# Print the statistics
print(stats)


# Create a bar plot for the scores
fig, ax = plt.subplots(figsize=(20, 12))
width = 0.35  # the width of the bars
indices = df['index']  # the x locations for the groups

math_scores = ax.bar(indices - width/2, df['math'], width, label='Math')
english_scores = ax.bar(indices + width/2, df['english'], width, label='English')

# Add some text for labels, title, and axes ticks
ax.set_xlabel('Student')
ax.set_ylabel('Scores')
ax.set_title('Scores by student and subject')
ax.set_xticks(indices)
ax.set_xticklabels(df['name'])
ax.legend()

# Attach a text label above each bar displaying its height
for rect in math_scores + english_scores:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Save the plot as an image file
plt.tight_layout()
plt.savefig('scores_plot.png')

# Optionally, display the plot
# plt.show()