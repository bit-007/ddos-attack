import requests
from multiprocessing import Pool
import time

URL = "http://127.0.0.1:5000/"

def send_request(_):
    try:
        response = requests.get(URL)
        print(f"Hacker - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Hacker - Request failed: {e}")

if __name__ == "__main__":
    num_requests = 100000  # Total number of requests to send
    num_workers = 10      # Number of concurrent workers

    start_time = time.time()

    with Pool(num_workers) as p:
        p.map(send_request, range(num_requests))

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")
