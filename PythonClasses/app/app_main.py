from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/dodaj', methods=['POST'])
def dodaj():
    try:
        data = request.get_json()
        a = data['a']
        b = data['b']
        result = a + b
        return jsonify({'result': result})
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid payload'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/odejmij', methods=['POST'])
def odejmij():
    try:
        data = request.get_json()
        a = data['a']
        b = data['b']
        result = a - b
        return jsonify({'result': result})
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid payload'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/pomnoz', methods=['POST'])
def pomnoz():
    try:
        data = request.get_json()
        a = data['a']
        b = data['b']
        result = a * b
        return jsonify({'result': result})
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid payload'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/podziel', methods=['POST'])
def podziel():
    try:
        data = request.get_json()
        a = data['a']
        b = data['b']
        if b == 0:
            return jsonify({'error': 'Cannot divide by zero'}), 400
        result = a / b
        return jsonify({'result': result})
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid payload'}), 400
    except ZeroDivisionError:
        return jsonify({'error': 'Cannot divide by zero'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
