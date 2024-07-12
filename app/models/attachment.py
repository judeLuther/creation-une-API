from app.extensions import db

# Define model
class Attachment(db.Model):
    # Define columns for the model
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    path = db.Column(db.String(150))
    content = db.Column(db.String)

    def __repr__(self):
            # Define a string representation for the model
        return f'<Post "{self.path}">'
     
