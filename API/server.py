from api import app  # Import your Flask app object
import gunicorn
if __name__ == "__main__":
    app.run(debug=True)

