from chartsite import db


class Chart(db.Model):
    __tablename__ = 'charts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    embed_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Chart('{self.name}')"
