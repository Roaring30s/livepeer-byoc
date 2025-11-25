import time
import requests
import urllib3

# Suppress SSL warnings for local Docker network
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


PAYLOAD = {
    "name": "pulse",
    "url": "http://byoc_pulse:5000",
    "capacity": 1,
    "price_per_unit": 0,
    "price_scaling": 1,
    "currency": "wei",
}

HEADERS = {"Authorization": "orch-secret"}

if __name__ == "__main__":
    for _ in range(10):
        # wait 1 second then try
        time.sleep(1)
        try:
            registered = requests.post(
                "https://byoc_orchestrator:8935/capability/register",
                json=PAYLOAD,
                headers=HEADERS,
                verify=False,
            )
            if registered.status_code == 200:
                break
            print(f"registration not completed: {registered.text}")
        except Exception as e:
            print(f"Error during registration: {e}")

