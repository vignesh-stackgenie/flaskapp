from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    """
    Home endpoint that returns a simple welcome message.
    """
    return "Hello, this is a simple Flask app for AWS ECS!"

@app.route('/health')
def health_check():
    """
    Health check endpoint for the load balancer.
    Returns a JSON response indicating the service is healthy.
    """
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    # Run the app on port 8080, accessible from any host
    app.run(host='0.0.0.0', port=8080)
