from flask_mysqldb import MySQL

db = MySQL()

def init_db(app):
    """Initialize MySQL connection and create tables."""
    db.init_app(app)

    with app.app_context():
        cur = db.connection.cursor()

        # ── CONTACT MESSAGES TABLE ──
        cur.execute("""
            CREATE TABLE IF NOT EXISTS contact_messages (
                id         INT AUTO_INCREMENT PRIMARY KEY,
                name       VARCHAR(100) NOT NULL,
                email      VARCHAR(150) NOT NULL,
                subject    VARCHAR(200),
                message    TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # ── VISITORS TABLE ──
        cur.execute("""
            CREATE TABLE IF NOT EXISTS visitors (
                id         INT AUTO_INCREMENT PRIMARY KEY,
                page       VARCHAR(200) DEFAULT '/',
                ip_address VARCHAR(50),
                user_agent TEXT,
                visited_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # ── PROJECTS TABLE ──
        cur.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id          INT AUTO_INCREMENT PRIMARY KEY,
                title       VARCHAR(200) NOT NULL,
                description TEXT,
                stack       VARCHAR(300),
                emoji       VARCHAR(10),
                label       VARCHAR(100),
                github_url  VARCHAR(300),
                live_url    VARCHAR(300)
            )
        """)


        db.connection.commit()
        cur.close()

        # Seed default projects if table is empty
        _seed_projects(app)
       


def _seed_projects(app):
    """Insert default projects on first run."""
    with app.app_context():
        cur = db.connection.cursor()
        cur.execute("SELECT COUNT(*) FROM projects")
        count = cur.fetchone()[0]

        if count == 0:
            default_projects = [
                (
                    'Fraud Detection in Banking',
                    'A machine learning system that detects fraudulent transactions in banking data using classification models trained on real-world patterns.',
                    'Python,Scikit-learn,Pandas,ML Classification,Data Analysis',
                    '🏦', 'AI / ML', '#', ''
                ),
                (
                    'Women Safety App',
                    'A safety application designed to help women in emergency situations — with SOS alerts, location sharing, and quick access to emergency contacts.',
                    'Python,Location API,Alert System,Database',
                    '🛡️', 'Mobile / Safety', '#', ''
                ),
                (
                    'Portfolio Website',
                    'The very site you are looking at — built from scratch with HTML, CSS, and JavaScript. Now powered by a Flask + MySQL backend!',
                    'HTML5,CSS3,JavaScript,Flask,MySQL',
                    '🌐', 'Full Stack', '#', ''
                ),
            ]
            cur.executemany("""
                INSERT INTO projects (title, description, stack, emoji, label, github_url, live_url)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, default_projects)
            db.connection.commit()

        cur.close()
