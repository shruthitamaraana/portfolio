from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    from pyngrok import ngrok
    public_url = ngrok.connect(5000)
    print("Public URL:", public_url)
    app.run(debug=True)

