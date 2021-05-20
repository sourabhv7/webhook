from flask import Flask, request, abort, render_template, redirect, url_for, Response
# curl -X POST -H "Content-Type: text/plain" --data "this is raw data" http://127.0.0.1:5000/webhook

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'Sourabh@123':
            error = 'Invalid Credentials. Please try again.'
        else:
            with open('file.txt', 'r') as f:
                return render_template('index1.html', text=f.read())
    return render_template('index.html', error=error)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(str(request.data))
        with open('file.txt', 'a+') as data:
            data.write(str(request.data))
            data.write('\n')

        return 'success', 200

    else:
		
        abort(Response('Operation Failed. Some error occured .'))




if __name__ == '__main__':
    # app.run()
    app.run(debug=False, host='0.0.0.0', port=5000)
