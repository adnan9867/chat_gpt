import requests

def fetch_facebook_profile(username):
    # Construct the Facebook Graph API endpoint
    api_endpoint = f"https://graph.facebook.com/{username}"

    # Specify the fields you want to retrieve from the user's profile
    fields = "id,name,email,gender,birthday"

    # Set your access token (You need to generate a Facebook API access token)
    access_token = "EAAOB8U7NApUBAFlekE9neFVCvWwRG6jh8UhNfPLYyrq0h1j7BDVEiyFtruXnlqZAeQMiBpfxtcLEwauku0iseQZCAuLKSTm2TCcqtsrOXo6G2kKAVXEuFauRctvQIiATksQD9Lut1kW4xz2ZAuiexCCoZCkdZBZCAgaZBRmI0gRRZAMPmIRbyvuY8YFRXTKpVhWfX3tdfMVEETxAl88z5cQ8unxDpKdICpAUjdjfTwRfRP1PT7a9A6wh"

    # Send a GET request to the API endpoint
    response = requests.get(api_endpoint, params={"access_token": access_token})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        profile_data = response.json()
        return profile_data
    else:
        # Request was unsuccessful
        print(f"Error: {response.status_code} - {response.text}")
        return None
