import requests

def get_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        joke = response.json()["joke"]
        print("Here's a joke for you: ")
        print(f"\n{joke}")
    else:
        print("Couldn't fetch a joke. Try again.")

if __name__ == "__main__":
    get_joke()