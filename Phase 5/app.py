from flask import Flask, render_template
from flask_socketio import SocketIO
import eventlet

# Initialize Flask and Socket.IO
app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

# Route for the main dashboard
@app.route('/')
def index():
    return render_template('dashboard.html')

# Function to emit real-time car data
def emit_car_data(car_data):
    socketio.emit('car_data', car_data)

# Start the Flask app
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
