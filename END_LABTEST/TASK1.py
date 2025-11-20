"""
Product Rating Analyzer

This module finds the highest-rated product from a list of product ratings.
It demonstrates prompt engineering with zero-shot learning capabilities.
"""


def find_highest_rated_product(ratings: dict) -> tuple:
    """
    Find the product with the highest rating from a dictionary of products and ratings.
    
    Args:
        ratings (dict): A dictionary where keys are product names and values are ratings.
                       Example: {"Product A": 4.5, "Product B": 4.8, "Product C": 4.2}
    
    Returns:
        tuple: A tuple containing (product_name, rating) of the highest-rated product.
    
    Raises:
        TypeError: If ratings is not a dictionary or values are non-numeric.
        ValueError: If ratings dictionary is empty.
    """
    # Validate input type first
    if not isinstance(ratings, dict):
        raise TypeError("ratings must be a dict mapping product->rating")
    
    # Check if empty
    if not ratings:
        raise ValueError("Ratings dictionary cannot be empty")
    
    # Validate all values are numeric
    for key, value in ratings.items():
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError(f"Rating value must be numeric, got {type(value).__name__} for key {key}")
    
    # Find product with maximum rating using max() with key parameter
    highest_product = max(ratings.items(), key=lambda x: x[1])
    
    return highest_product


__all__ = ["find_highest_rated_product"]


# Test cases
if __name__ == "__main__":
    # Test 1: Normal case with multiple products
    test_ratings_1 = {
        "Laptop": 4.7,
        "Mouse": 4.2,
        "Keyboard": 4.9,
        "Monitor": 4.5
    }
    product, rating = find_highest_rated_product(test_ratings_1)
    print(f"Test 1 - Highest rated product: {product} with rating {rating}")
    assert product == "Keyboard" and rating == 4.9, "Test 1 failed"
    
    # Test 2: Single product
    test_ratings_2 = {"Headphones": 4.6}
    product, rating = find_highest_rated_product(test_ratings_2)
    print(f"Test 2 - Highest rated product: {product} with rating {rating}")
    assert product == "Headphones" and rating == 4.6, "Test 2 failed"
    
    # Test 3: Products with same ratings (returns first max found)
    test_ratings_3 = {"Phone": 4.8, "Tablet": 4.8, "Charger": 4.3}
    product, rating = find_highest_rated_product(test_ratings_3)
    print(f"Test 3 - Highest rated product: {product} with rating {rating}")
    assert rating == 4.8, "Test 3 failed"
    
    # Test 4: Error handling
    try:
        find_highest_rated_product({})
    except ValueError as e:
        print(f"Test 4 - Error handled correctly: {e}")
    
    print("\nAll tests passed! ✓")