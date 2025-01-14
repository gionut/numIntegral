from flask import Flask, jsonify, abort
import math

app = Flask(__name__)

@app.route('/integral/<lower>/<upper>', methods=['GET'])
def calculate_integral(lower, upper):
    lower = float(lower)
    upper = float(upper)
    if lower > upper:
        abort(400, description="The values of lower and upper path parameters should be increasing.")
    
    result = {}
    loops = 6
    N = 1
    
    for _ in range(loops):
        N *= 10
        dx = upper / N
        integral = 0.0
        
        for i in range(N):
            x = (i + 0.5) * dx
            integral += math.fabs(math.sin(x)) * dx
        
        result[N] = integral

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
