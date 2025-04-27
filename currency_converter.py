from main import apikey_curr
import requests

def convt_curr(u, a, fc, tc, api):
    url = f"{u}?access_key={api}&from={fc}&to={tc}&amount={a}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data.get("success"):
        result = data["result"]
        print(f"\n{a} {fc.upper()} = " \
              f"{result:.2f} {tc.upper()}")
    else:
        print("Error fetching conversion rate. " \
              "Please check currency codes.")

if __name__ == "__main__":
    print("Currency Converter")
    base_url = "https://api.exchangerate.host/convert"
    from_curr = input("Convert from (eg: USD): ").upper()
    to_curr = input("Convert from (eg: INR): ").upper()
    amt = float(input("Enter amount: "))
    api_key = apikey_curr

    convt_curr(base_url, amt, from_curr, to_curr, api_key)