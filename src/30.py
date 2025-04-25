import requests

def get_random_data():
    # Example: Fetching a random movie from the internet
    response = requests.get("https://api.example.com/movies")
    if response.status_code == 200:
        data = response.json()
        return data["title"]
    else:
        print(f"Error fetching data. Status code: {response.status_code}")
        return None

# Example usage
random_movie = get_random_data()
if random_movie:
    print(f"The random movie is: {random_movie}")
else:
    print("No random movie found.")
