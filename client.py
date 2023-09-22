import requests

server_url = "http://127.0.0.1:5000"
res = requests.get(server_url, params={"led": "on"})
print(res.text)

# def send_req():


# if __name__ == "__main__":
#     send_req()