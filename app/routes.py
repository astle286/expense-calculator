from flask import Blueprint, render_template, request, redirect, send_file, render_template_string, jsonify
from . import db
from .models import Expense
from datetime import datetime, timedelta
import csv
import io
from xhtml2pdf import pisa

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

    # Filters
    filter_type = request.args.get('filter', 'all')
    today = datetime.today().date()
    if filter_type == 'week':
        start_date = today - timedelta(days=7)
        expenses = Expense.query.filter(Expense.date >= start_date).order_by(Expense.date.desc()).all()
    elif filter_type == 'month':
        start_date = today.replace(day=1)
        expenses = Expense.query.filter(Expense.date >= start_date).order_by(Expense.date.desc()).all()
    else:
        expenses = Expense.query.order_by(Expense.date.desc()).all()

    return render_template('index.html', expenses=expenses, filter_type=filter_type)

@main.route('/export')
def export_csv():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Date', 'Category', 'Amount'])
    for e in expenses:
        writer.writerow([e.date, e.category, e.amount])
    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode()), mimetype='text/csv', as_attachment=True, download_name='expenses.csv')

# Export to PDF
@main.route('/export/pdf')
def export_pdf():
    filter_type = request.args.get('filter', 'all')
    today = datetime.today().date()
    if filter_type == 'week':
        start_date = today - timedelta(days=7)
        expenses = Expense.query.filter(Expense.date >= start_date).order_by(Expense.date.desc()).all()
    elif filter_type == 'month':
        start_date = today.replace(day=1)
        expenses = Expense.query.filter(Expense.date >= start_date).order_by(Expense.date.desc()).all()
    else:
        expenses = Expense.query.order_by(Expense.date.desc()).all()

    html = render_template_string("""
    <h1>Expense Report</h1>
    <table border="1" cellspacing="0" cellpadding="5">
      <tr><th>Date</th><th>Category</th><th>Amount</th></tr>
      {% for e in expenses %}
        <tr>
          <td>{{ e.date }}</td>
          <td>{{ e.category }}</td>
          <td>{{ "%.2f"|format(e.amount) }}</td>
        </tr>
      {% endfor %}
    </table>
    """, expenses=expenses)

    pdf = io.BytesIO()
    pisa.CreatePDF(io.StringIO(html), dest=pdf)
    pdf.seek(0)
    return send_file(pdf, mimetype='application/pdf', as_attachment=True, download_name='expenses.pdf')

@main.route('/add-expense', methods=['POST'])
def add_expense():
    data = request.get_json()
    category = data['category']
    amount = float(data['amount'])
    date = datetime.strptime(data['date'], '%Y-%m-%d')
    expense = Expense(category=category, amount=amount, date=date)
    db.session.add(expense)
    db.session.commit()
    return jsonify({
        'date': expense.date.strftime('%Y-%m-%d'),
        'category': expense.category,
        'amount': expense.amount
    })
    
@main.route('/delete-expense/<int:id>', methods=['DELETE'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return jsonify({'success': True})

#one more test comment