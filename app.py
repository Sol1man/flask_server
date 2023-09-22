from flask import Flask, request
from gpiozero import LED

app = Flask(__name__)
# led = LED(12) 

@app.route("/")
def led_control():
    state = request.args.get('led')
    # if state == "on":
    #     led.on()
    # elif state == "off":
    #     led.off()
    return f"OK, Led is {state}"

if __name__ == "__main__":
    app.run()
    #led_control()

