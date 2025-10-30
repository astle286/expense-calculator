import time
from sqlalchemy.exc import OperationalError
from app import create_app, db

app = create_app()

MAX_RETRIES = 10
RETRY_DELAY = 5  # seconds

with app.app_context():
    for attempt in range(MAX_RETRIES):
        try:
            db.create_all()
            print("Database initialized successfully.")
            break
        except OperationalError as e:
            print(f"Attempt {attempt + 1}: Database not ready — retrying in {RETRY_DELAY}s...")
            time.sleep(RETRY_DELAY)
    else:
        print("Failed to connect to the database after multiple attempts.")
        exit(1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
