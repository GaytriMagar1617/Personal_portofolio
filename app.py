from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from database import db, init_db
from models import ContactMessage, Visitor, Project
from datetime import datetime
import os

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)

# ── CONFIG ──
app.config['MYSQL_HOST']     = 'localhost'
app.config['MYSQL_USER']     = 'root'         # change to your MySQL username
app.config['MYSQL_PASSWORD'] = 'Gaytri@1216' # change to your MySQL password
app.config['MYSQL_DB']       = 'portfolio_db'
app.config['MYSQL_CHARSET'] = 'utf8mb4'
init_db(app)

# ── SERVE FRONTEND ──
@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

# ────────────────────────────────────────────
# CONTACT FORM
# ────────────────────────────────────────────

@app.route('/api/contact', methods=['POST'])
def contact():
    """Save contact form message to DB."""
    data = request.get_json()

    name    = data.get('name', '').strip()
    email   = data.get('email', '').strip()
    subject = data.get('subject', '').strip()
    message = data.get('message', '').strip()

    if not all([name, email, message]):
        return jsonify({'success': False, 'error': 'Name, email and message are required.'}), 400

    ContactMessage.create(name, email, subject, message)
    return jsonify({'success': True, 'message': 'Message saved successfully!'})


@app.route('/api/contact', methods=['GET'])
def get_messages():
    """Admin: get all contact messages."""
    messages = ContactMessage.get_all()
    return jsonify({'success': True, 'data': messages})


@app.route('/api/contact/<int:msg_id>', methods=['DELETE'])
def delete_message(msg_id):
    """Admin: delete a contact message."""
    ContactMessage.delete(msg_id)
    return jsonify({'success': True, 'message': 'Deleted.'})

# ────────────────────────────────────────────
# VISITOR TRACKING
# ────────────────────────────────────────────

@app.route('/api/visit', methods=['POST'])
def track_visit():
    """Log a visitor."""
    data       = request.get_json() or {}
    page       = data.get('page', '/')
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent', '')

    Visitor.log(page, ip_address, user_agent)
    return jsonify({'success': True})


@app.route('/api/visitors', methods=['GET'])
def get_visitors():
    """Admin: get visitor stats."""
    stats = Visitor.get_stats()
    return jsonify({'success': True, 'data': stats})

# ────────────────────────────────────────────
# PROJECTS (Admin CRUD)
# ────────────────────────────────────────────

@app.route('/api/projects', methods=['GET'])
def get_projects():
    """Get all projects (public)."""
    projects = Project.get_all()
    return jsonify({'success': True, 'data': projects})


@app.route('/api/projects', methods=['POST'])
def add_project():
    """Admin: add a new project."""
    data = request.get_json()
    Project.create(
        title       = data.get('title', ''),
        description = data.get('description', ''),
        stack       = data.get('stack', ''),
        emoji       = data.get('emoji', '💻'),
        label       = data.get('label', 'Project'),
        github_url  = data.get('github_url', '#'),
        live_url    = data.get('live_url', ''),
    )
    return jsonify({'success': True, 'message': 'Project added!'})


@app.route('/api/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Admin: update a project."""
    data = request.get_json()
    Project.update(project_id, data)
    return jsonify({'success': True, 'message': 'Project updated!'})


@app.route('/api/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Admin: delete a project."""
    Project.delete(project_id)
    return jsonify({'success': True, 'message': 'Project deleted!'})

# ────────────────────────────────────────────
# ADMIN PANEL
# ────────────────────────────────────────────

@app.route('/admin')
def admin():
    return send_from_directory('frontend', 'admin.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
