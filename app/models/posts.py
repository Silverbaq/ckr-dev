from . import db

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80), required=True)
    date_created = db.Column(db.Datetime, required=True)
    description = db.Column(db.String(), required=True)

    def __rep__(self):
        return '<Post :%s>' % (self.subject)