from collections import Counter
import math 


# Step 1: Define the distance function

def distance(x1, y1, x2, y2):
    """
    Calculate Euclidean distance between two 2D points.
    """
    result=((x1-x2)**2+(y1-y2)**2)**0.5
    return result


# Step 2: Training dataset

# Format: [Age, Hours per week, Label]
train_data = [
    [19, 15, 'Action'],
    [22, 12, 'Action'],
    [25, 10, 'Action'],
    [27,  7, 'Romance'],
    [29,  8, 'Romance'],
    [31,  5, 'Romance']
]


# Step 3: KNN prediction function

def knn_predict(train, test_point, k):
    distances = []

    # Calculate distance from test point to training points
    for x in train:
        dist = distance(x[0], x[1], test_point[0], test_point[1])
        distances.append((dist, x[2]))  # (distance, label)

    # Sort by distance (smallest first)
    distances.sort(key=lambda x: x[0])

    # Select top k neighbors
    nearest_neighbors = distances[:k]

    # Majority voting
    labels = [label for _, label in nearest_neighbors]
    vote_counts = Counter(labels)
    prediction = vote_counts.most_common(1)[0][0]

    return prediction


# Step 4: Test cases

test_cases = [
    ([24, 11], 'Action'),    # Expected: Action
    ([28,  7], 'Romance'),   # Expected: Romance
    ([20, 14], 'Action'),    # Expected: Action
    ([30,  6], 'Romance'),   # Expected: Romance
    ([26,  9], 'Action/Romance (tie possible)') # Tie case
]


if __name__ == "__main__":
    k = 3
    print(f"KNN classifier from scratch (k = {k})\n")
    print("Training Data:")
    for row in train_data:
        print(row)
    print("\nPredictions:\n")

    for test_point, expected in test_cases:
        pred = knn_predict(train_data, test_point, k)
        print(f"Test Point: {test_point} -> Predicted: {pred} | Expected: {expected}")

