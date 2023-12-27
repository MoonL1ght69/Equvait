from flask import Flask, render_template
from webserver import keep_alive

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


if __name__ == '__main__':
  # Змініть порт, якщо це необхідно
  app.run(host='0.0.0.0', port=5000, debug=True)

keep_alive()
