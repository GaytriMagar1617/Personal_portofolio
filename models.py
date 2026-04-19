from database import db


# ────────────────────────────────────────────
# CONTACT MESSAGE MODEL
# ────────────────────────────────────────────

class ContactMessage:

    @staticmethod
    def create(name, email, subject, message):
        cur = db.connection.cursor()
        cur.execute("""
            INSERT INTO contact_messages (name, email, subject, message)
            VALUES (%s, %s, %s, %s)
        """, (name, email, subject, message))
        db.connection.commit()
        cur.close()

    @staticmethod
    def get_all():
        cur = db.connection.cursor()
        cur.execute("""
            SELECT id, name, email, subject, message, created_at
            FROM contact_messages
            ORDER BY created_at DESC
        """)
        rows = cur.fetchall()
        cur.close()
        return [
            {
                'id':         r[0],
                'name':       r[1],
                'email':      r[2],
                'subject':    r[3],
                'message':    r[4],
                'created_at': str(r[5]),
            }
            for r in rows
        ]

    @staticmethod
    def delete(msg_id):
        cur = db.connection.cursor()
        cur.execute("DELETE FROM contact_messages WHERE id = %s", (msg_id,))
        db.connection.commit()
        cur.close()


# ────────────────────────────────────────────
# VISITOR MODEL
# ────────────────────────────────────────────

class Visitor:

    @staticmethod
    def log(page, ip_address, user_agent):
        cur = db.connection.cursor()
        cur.execute("""
            INSERT INTO visitors (page, ip_address, user_agent)
            VALUES (%s, %s, %s)
        """, (page, ip_address, user_agent))
        db.connection.commit()
        cur.close()

    @staticmethod
    def get_stats():
        cur = db.connection.cursor()

        # Total visits
        cur.execute("SELECT COUNT(*) FROM visitors")
        total = cur.fetchone()[0]

        # Visits today
        cur.execute("""
            SELECT COUNT(*) FROM visitors
            WHERE DATE(visited_at) = CURDATE()
        """)
        today = cur.fetchone()[0]

        # Visits per page
        cur.execute("""
            SELECT page, COUNT(*) as visits
            FROM visitors
            GROUP BY page
            ORDER BY visits DESC
        """)
        by_page = [{'page': r[0], 'visits': r[1]} for r in cur.fetchall()]

        # Last 10 visitors
        cur.execute("""
            SELECT ip_address, page, visited_at
            FROM visitors
            ORDER BY visited_at DESC
            LIMIT 10
        """)
        recent = [
            {'ip': r[0], 'page': r[1], 'visited_at': str(r[2])}
            for r in cur.fetchall()
        ]

        cur.close()
        return {
            'total_visits': total,
            'today_visits': today,
            'by_page':      by_page,
            'recent':       recent,
        }


# ────────────────────────────────────────────
# PROJECT MODEL
# ────────────────────────────────────────────

class Project:

    @staticmethod
    def get_all():
        cur = db.connection.cursor()
        cur.execute("""
            SELECT id, title, description, stack, emoji, label, github_url, live_url
            FROM projects
            ORDER BY id ASC
        """)
        rows = cur.fetchall()
        cur.close()
        return [
            {
                'id':          r[0],
                'title':       r[1],
                'description': r[2],
                'stack':       r[3].split(',') if r[3] else [],
                'emoji':       r[4],
                'label':       r[5],
                'github_url':  r[6],
                'live_url':    r[7],
            }
            for r in rows
        ]

    @staticmethod
    def create(title, description, stack, emoji, label, github_url, live_url):
        cur = db.connection.cursor()
        cur.execute("""
            INSERT INTO projects (title, description, stack, emoji, label, github_url, live_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (title, description, stack, emoji, label, github_url, live_url))
        db.connection.commit()
        cur.close()

    @staticmethod
    def update(project_id, data):
        cur = db.connection.cursor()
        cur.execute("""
            UPDATE projects
            SET title=%s, description=%s, stack=%s, emoji=%s,
                label=%s, github_url=%s, live_url=%s
            WHERE id=%s
        """, (
            data.get('title'),
            data.get('description'),
            data.get('stack'),
            data.get('emoji'),
            data.get('label'),
            data.get('github_url'),
            data.get('live_url'),
            project_id,
        ))
        db.connection.commit()
        cur.close()

    @staticmethod
    def delete(project_id):
        cur = db.connection.cursor()
        cur.execute("DELETE FROM projects WHERE id = %s", (project_id,))
        db.connection.commit()
        cur.close()
