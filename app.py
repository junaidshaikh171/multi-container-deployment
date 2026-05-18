from flask import Flask, render_template
import redis

app = Flask(__name__)

redis_client = redis.Redis(
    host='redis',
    port=6379,
    decode_responses=True
)

@app.route('/')
def home():

    visits = redis_client.incr('counter')

    return render_template(
        'index.html',
        visits=visits
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)