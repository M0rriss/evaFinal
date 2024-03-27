from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <style>
        .card {
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            max-width: 300px;
            margin: auto;
            text-align: center;
        }
        .title {
            color: grey;
            font-size: 18px;
        }
        button {
            border: none;
            outline: 0;
            display: inline-block;
            padding: 8px;
            color: white;
            background-color: #000;
            text-align: center;
            cursor: pointer;
            width: 100%;
            font-size: 18px;
        }
        a {
            text-decoration: none;
            font-size: 22px;
            color: black;
        }
        button:hover, a:hover {
            opacity: 0.7;
        }
    </style>
    <html>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <div class="card">
        <img src="https://scontent.fjau3-1.fna.fbcdn.net/v/t39.30808-6/434197167_954295129541986_8349706509575865870_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeF0fc0I6fXZfOScQ2av-PqInrG9mLL1QBKesb2YsvVAEisBbaALEcE8l60aeJpObqAZxQwBNw8Bs9Jg-suwMX0I&_nc_ohc=F0ZC5Oxk6jAAX8SFHLZ&_nc_ht=scontent.fjau3-1.fna&oh=00_AfD6iILqd0VlwKHtKzvd74IKdkJ6ITAzsz0AxlS9UF8D3Q&oe=660987D4" alt="John" style="width:100%">
        <h1>John Doe</h1>
        <p class="title">CEO & Founder, Example</p>
        <p>Harvard University</p>
        <a href="#"><i class="fa fa-dribbble"></i></a>
        <a href="#"><i class="fa fa-twitter"></i></a>
        <a href="#"><i class="fa fa-linkedin"></i></a>
        <a href="#"><i class="fa fa-facebook"></i></a>
        <p><button>Contact</button></p>
    </div>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
