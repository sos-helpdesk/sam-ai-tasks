"""
Task 3: Recommendation System
"""

DATABASE = {
    "action": ["Leo", "Vikram", "Beast"],
    "comedy": ["Dhilluku Dhillu", "Chennai 600028"],
    "romance": ["96", "Vinnaithaandi Varuvaaya"],
    "scifi": ["Enthiran", "Indru Netru Naalai"]
}

def recommend(genre):
    return DATABASE.get(genre.lower(), [])

if __name__ == "__main__":
    print("Available Genres:", ", ".join(DATABASE.keys()))
    choice = input("Enter your preferred genre: ")
    recommendations = recommend(choice)
    
    if recommendations:
        print(f"\nRecommended {choice} titles:")
        for item in recommendations:
            print(f"- {item}")
    else:
        print("No recommendations found for this genre.")
        
