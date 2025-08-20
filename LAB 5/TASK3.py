import random

# Sample product database with brands and categories
products = [
    {"name": "Apple iPhone 14", "brand": "Apple", "category": "Smartphone"},
    {"name": "Samsung Galaxy S23", "brand": "Samsung", "category": "Smartphone"},
    {"name": "Sony WH-1000XM5", "brand": "Sony", "category": "Headphones"},
    {"name": "Bose QuietComfort 45", "brand": "Bose", "category": "Headphones"},
    {"name": "Dell XPS 13", "brand": "Dell", "category": "Laptop"},
    {"name": "HP Spectre x360", "brand": "HP", "category": "Laptop"},
]

# User purchase history (simulate with a list)
user_history = []

# Feedback storage for learning
feedback = {}

def recommend_product(history, feedback):
    # Find categories the user bought before
    categories = set([p["category"] for p in history])
    # Find brands the user bought before
    brands = set([p["brand"] for p in history])
    # Candidates: products in same category, but different brand
    candidates = []
    for prod in products:
        if prod["category"] in categories and prod["brand"] not in brands:
            candidates.append(prod)
    # If no candidates, suggest random product not bought before
    if not candidates:
        candidates = [p for p in products if p not in history]
    # Sort candidates by positive feedback
    candidates.sort(key=lambda p: feedback.get(p["name"], 0), reverse=True)
    # Pick one randomly among top 2 to be fair
    top_candidates = candidates[:2] if len(candidates) >= 2 else candidates
    suggestion = random.choice(top_candidates)
    # Explanation
    if suggestion["category"] in categories:
        explanation = f"Suggested because you bought {suggestion['category']} before, but this is a different brand ({suggestion['brand']}) for fairness."
    else:
        explanation = f"Suggested because you haven't tried this product yet."
    return suggestion, explanation

def main():
    print("Welcome to the Product Recommender!")
    while True:
        print("\nYour purchase history:", [p["name"] for p in user_history])
        suggestion, explanation = recommend_product(user_history, feedback)
        print(f"\nWe recommend: {suggestion['name']} ({suggestion['brand']})")
        print("Reason:", explanation)
        # Get user feedback
        user_input = input("Do you like this suggestion? (like/dislike/quit): ").strip().lower()
        if user_input == "quit":
            break
        elif user_input == "like":
            feedback[suggestion["name"]] = feedback.get(suggestion["name"], 0) + 1  # Increase positive feedback
            print("Thanks for your feedback!")
        elif user_input == "dislike":
            feedback[suggestion["name"]] = feedback.get(suggestion["name"], 0) - 1  # Decrease feedback
            print("Thanks for your feedback!")
        else:
            print("Invalid input. Please type 'like', 'dislike', or 'quit'.")
        # Simulate user buying the product if liked
        if user_input == "like":
            user_history.append(suggestion)

if __name__ == "__main__":
    main()