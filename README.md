# KNN-implementation
A beginner-friendly **K-Nearest Neighbours (KNN)** classifier implemented entirely from scratch in Python — **no machine learning libraries** like scikit-learn used.

This project demonstrates:
- How to calculate Euclidean distances between points.
- How to find the `k` nearest neighbours.
- How to perform majority voting for classification.

---

##  What is KNN?

KNN is a simple, non-parametric classification algorithm.  
It works by:
1. Calculating the distance from the input sample to all training samples.
2. Finding the closest `k` samples (`k = 3` by default in this script).
3. Voting among those `k` neighbours — whichever class appears most is the prediction.


##  Dataset

We are classifying whether a person likes **Action** or **Romance** movies based on:
- Age
- Hours spent watching movies per week

| Age | Hours/Week | Movie Type |
|-----|-----------|------------|
| 19  | 15        | Action     |
| 22  | 12        | Action     |
| 25  | 10        | Action     |
| 27  |  7        | Romance    |
| 29  |  8        | Romance    |
| 31  |  5        | Romance    |

##  Notes
- You can change `k` in the script to experiment with results.
- This is meant as an **educational implementation** — for large datasets, it's better to use optimised libraries.
- Great for understanding how KNN works internally.

## Author
Made by **Aryan**  
If you like this project, ⭐ it on GitHub!
