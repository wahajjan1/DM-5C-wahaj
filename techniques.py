import pandas as pd
import numpy as np

# Step 1: Create dataset with Urdu-style names
passenger_data = {
    'PassengerId': [101, 102, 103, 104, 105, 106, 107, 108],
    'Survived': [1, 0, 1, 0, 1, 0, 1, 0],
    'Pclass': [1, 3, 2, 1, 3, 2, 1, 3],
    'Name': [
        "Khan, Mrs. Amina",
        "Raza, Mr. Junaid",
        "Siddiqui, Miss. Hira",
        "Iqbal, Miss. Mehwish",
        "Farooq, Mr. Usman",
        "Tariq, Miss. Nida",
        "Baig, Mr. Salman",
        "Zehra, Miss. Laiba"
    ],
    'Sex': ['female', 'male', 'female', 'female', 'male', 'female', 'male', 'female'],
    'Age': [28, np.nan, 55, 30, 8, 22, 65, np.nan],
    'SibSp': [0, 2, 1, 0, 1, 0, 0, 1],
    'Parch': [1, 0, 0, 2, 1, 0, 0, 0],
    'Ticket': ['A101', 'B202', 'C303', 'D404', 'E505', 'F606', 'G707', 'H808'],
    'Fare': [75.50, 12.75, 90.00, 150.00, 25.00, 30.50, 110.00, 9.99],
    'Cabin': ["C50", np.nan, "A10", np.nan, "G10", np.nan, "B80", "Unknown"],
    'Embarked': ['S', 'C', 'Q', 'S', 'C', np.nan, 'S', 'Q']
}

df = pd.DataFrame(passenger_data)

# Step 2: Display missing values
print("Before Cleaning:\n", df.isna().sum(), "\n")

# Step 3: Fill missing values
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Cabin'] = df['Cabin'].fillna("Not Assigned")

# Step 4: Age Binning Function
def assign_age_group(age):
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 35:
        return "Adult"
    elif age <= 60:
        return "Middle-Aged"
    else:
        return "Senior"

df['AgeGroup'] = df['Age'].apply(assign_age_group)

# Step 5: Extract surname from name
df['Surname'] = df['Name'].apply(lambda name: name.split(',')[0].strip())

# Final Output
print("After Cleaning:\n", df.isna().sum(), "\n")
print("Preview of Cleaned Data:\n", df[['PassengerId', 'Survived', 'Age', 'AgeGroup', 'Embarked', 'Cabin', 'Surname']])
