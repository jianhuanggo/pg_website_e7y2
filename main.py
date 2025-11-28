from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__, static_folder="static", template_folder="templates")


def get_db_connection():
    conn = sqlite3.connect("instance/portfolio.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/health")
def health_check():
    """Healthcheck endpoint for Replit and monitoring"""
    try:
        # Test database connection
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT 1")
        conn.close()

        return jsonify({"status": "healthy", "database": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 503


@app.route("/")
def read_root():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM socials")
    socials = c.fetchall()
    c.execute("SELECT * FROM projects")
    projects = c.fetchall()
    c.execute("SELECT * FROM skills")
    skills = c.fetchall()
    c.execute("SELECT * FROM profile")
    profile = c.fetchone()
    conn.close()
    return render_template("index.html",
                           socials=socials,
                           skills=skills,
                           projects=projects,
                           profile=profile)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, use_reloader=True)
