from flask import Blueprint, render_template, request, redirect
from app import db
from .models import Expense
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form['category']
        amount = float(request.form['amount'])
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        expense = Expense(category=category, amount=amount, date=date)
        db.session.add(expense)
        db.session.commit()
        return redirect('/')
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    return render_template('index.html', expenses=expenses)
