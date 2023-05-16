from database import db

class CategoryModel(db.Model):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    expenses = db.relationship('expenseModel', back_populates="store", lazy="dynamic", cascade="all, delete")