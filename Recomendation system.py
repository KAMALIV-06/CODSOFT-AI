import numpy as np

# Sample user-item matrix (rows represent users, columns represent items)
# Each cell (i, j) contains the rating of user i for item j (0 means no rating)
user_item_matrix = np.array([
    [4, 5, 0, 0, 0],
    [0, 0, 5, 4, 0],
    [3, 0, 0, 0, 5],
    [0, 4, 0, 5, 0],
    [0, 0, 3, 0, 4]
])

# Function to calculate similarity between users using cosine similarity
def cosine_similarity(user_item_matrix):
    norm = np.linalg.norm(user_item_matrix, axis=1)
    return np.dot(user_item_matrix, user_item_matrix.T) / (norm[:, None] * norm)

# Function to make recommendations using collaborative filtering
def recommend(user_item_matrix, user_id, num_recommendations=2):
    sim_matrix = cosine_similarity(user_item_matrix)

    # Get the user's preferences
    user_preferences = user_item_matrix[user_id]

    # Calculate the weighted sum of preferences based on similarity
    weighted_sum = np.dot(sim_matrix[user_id], user_item_matrix)

    # Exclude items the user has already rated
    weighted_sum -= user_preferences

    # Sort items by the weighted sum in descending order
    recommended_items = np.argsort(weighted_sum)[::-1]

    # Filter out items with zero weight
    recommended_items = [item for item in recommended_items if weighted_sum[item] > 0]

    # Return top N recommendations
    return recommended_items[:num_recommendations]

# Example: Recommend items for user 1
user_id_to_recommend = 1
recommendations = recommend(user_item_matrix, user_id_to_recommend)
print(f"Recommended items for user {user_id_to_recommend}: {recommendations}")
