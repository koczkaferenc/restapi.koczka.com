from flask import Flask, request, jsonify
import math 

app = Flask(__name__)

def solve_quadratic(a, b, c):
    D = b**2 - 4*a*c  # diszkrimináns
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return {"x1": x1, "x2": x2}
    elif D == 0:
        x = -b / (2 * a)
        return {"x": x}
    else:
        return {"error": "No real solution."}


# GET végpont - visszaad egy üdvözlő üzenetet
@app.route('/', methods=['GET'])
def index():
    return """
    <p>Usage:</p>
    <ul>
      <li>Get: /hello</li>
      <li>Get: /hello?name=Anna</li>
      <li>Post: /greet</li>
      <li>Post: /greet  { "name":"Anna" }</li>
      <li>Get/Post: /solve: ax<sup>2</sup>+bx+c=0 e.g.: /solve?a=3&b=3&c=3</li>
    </ul>
    """

# GET: visszaad egy általános üdvözlő üzenetet    
@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name')
    if name:
        return jsonify({"message": f"Hello, {name}!"})
    else:
        return jsonify({"message": "Hello, world!"})

# POST: fogad egy JSON adatot, és visszaküldi a nevet
@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()  # JSON adatok lekérése
    if 'name' in data:
        name = data['name']
        return jsonify({"message": f"Hello, {name}!"})
    else:
        return jsonify({"error": "Name not provided"}), 400


@app.route('/solve', methods=['GET', 'POST'])
def solve():
    try:
        if request.method == 'GET':
            # Paraméterek kinyerése GET kérésből (query string)
            a = float(request.args.get('a'))
            b = float(request.args.get('b'))
            c = float(request.args.get('c'))
        
        elif request.method == 'POST':
            # Paraméterek kinyerése POST kérésből (JSON body)
            data = request.get_json()
            a = float(data['a'])
            b = float(data['b'])
            c = float(data['c'])

        if a == 0:
            return jsonify({"error": "Value of 'a' can't be zero!"}), 400

        # Másodfokú egyenlet megoldása
        result = solve_quadratic(a, b, c)
        
        # Válasz visszaadása JSON formátumban
        return jsonify(result)

    except (TypeError, ValueError, KeyError):
        return jsonify({"error": "Wrong parameters!"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')