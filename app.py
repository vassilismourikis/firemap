from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def random_number():
    print("USED THIS TO PRODUCE")
    return str(random.randint(1, 100))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

