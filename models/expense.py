from database import db

class ExpenseModel(db.Model):

    __tablename__ = "expense"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    value  = db.Column(db.Float(precision=2), unique=False)
    data = db.Column(db.DateTime, nullable=False)
    person = db.Column(db.String(80), unique=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), unique=False, nullable=False)
    store = db.relationship("CategoryModel", back_populates = "items")