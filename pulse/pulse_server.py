from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/pulse', methods=['POST'])
def pulse():
    # Pulse check endpoint - returns OK to indicate service is alive
    return Response(
        json.dumps({'status': 'OK', 'code': 200}),
        mimetype='application/json',
        status=200
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)