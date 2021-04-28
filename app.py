from app import app, db, cli
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

