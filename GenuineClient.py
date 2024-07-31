import requests
import time

URL = "http://127.0.0.1:5000/"

def access_server():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print("Genuine User - Page accessed successfully!")
        else:
            print(f"Genuine User - Received unexpected status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Genuine User - Request failed: {e}")

if __name__ == "__main__":
    # Simulate a genuine user accessing the server once every few seconds
    while True:
        access_server()
        time.sleep(2)  # Adjust the sleep duration as needed

~                                                                                                                                                                                                           
~                                                                
