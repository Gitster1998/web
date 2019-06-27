from app import app
@app.route('/')
@app.route('/index')
def index():
    return '<html><head><title>hello smitt</title></head><body>head of hydra is alexandera pierce</body></html>'
