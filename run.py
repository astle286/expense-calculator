from app import create_app, db
import logging
from logging.handlers import RotatingFileHandler
import os

app = create_app()

with app.app_context():
    db.create_all()

# --- Logging Setup ---
if not os.path.exists("logs"):
    os.makedirs("logs")

log_file = os.path.join(os.path.dirname(__file__), "logs/expense_calculator.txt")
handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# Attach handler to Flask app logger
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

logging.getLogger().addHandler(handler) 
logging.getLogger().setLevel(logging.INFO)

app.logger.info("Expense Calculator app started")
# ----------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
