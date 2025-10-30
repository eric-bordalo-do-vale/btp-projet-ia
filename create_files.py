import os

# Créer les dossiers
os.makedirs('templates', exist_ok=True)
os.makedirs('static/css', exist_ok=True)

# Contenu des fichiers templates
templates = {
    'base.html': '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}La Tour - Plateforme de Mentorat{% endblock %}</title>
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="nav-brand">
                <h1>🗼 La Tour</h1>
            </div>
            <ul class="nav-menu">
                <li><a href="{{ url_for('index') }}">Accueil</a></li>
                <li><a href="{{ url_for('mentors') }}">Trouver un mentor</a></li>
                <li><a href="{{ url_for('mes_rdv') }}">Mes rendez-vous</a></li>
                <li><a href="{{ url_for('chatbot') }}">Chatbot IA</a></li>
            </ul>
        </div>
    </nav>

    <main class="container">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2025 La Tour - La Plateforme Marseille</p>
        </div>
    </footer>
</body>
</html>''',

    'index.html': '''{% extends "base.html" %}

{% block content %}
<div class="hero">
    <h1>Bienvenue sur La Tour 🗼</h1>
    <p class="subtitle">Votre plateforme d'entraide et de mentorat à La Plateforme</p>
</div>

<section class="features">
    <div class="feature-card">
        <h3>👥 Trouver un mentor</h3>
        <p>Connectez-vous avec des intervenants et étudiants expérimentés selon votre spécialisation</p>
        <a href="{{ url_for('mentors') }}" class="btn">Voir les mentors</a>
    </div>

    <div class="feature-card">
        <h3>🤖 Chatbot IA</h3>
        <p>Obtenez des réponses instantanées à vos questions techniques</p>
        <a href="{{ url_for('chatbot') }}" class="btn">Poser une question</a>
    </div>

    <div class="feature-card">
        <h3>📅 Planifier un RDV</h3>
        <p>Réservez des sessions d'accompagnement en ligne ou en présentiel</p>
        <a href="{{ url_for('mes_rdv') }}" class="btn">Mes rendez-vous</a>
    </div>
</section>

<section class="specialisations">
    <h2>Nos spécialisations</h2>
    <div class="spec-grid">
        <div class="spec-badge">💻 Développement Web</div>
        <div class="spec-badge">📊 Data Science</div>
        <div class="spec-badge">🔒 Cybersécurité</div>
        <div class="spec-badge">📱 Mobile</div>
        <div class="spec-badge">☁️ Cloud & DevOps</div>
        <div class="spec-badge">🎨 UI/UX Design</div>
    </div>
</section>
{% endblock %}''',

    'mentors.html': '''{% extends "base.html" %}

{% block title %}Trouver un mentor - La Tour{% endblock %}

{% block content %}
<h1>Trouver un mentor</h1>

<div class="filters">
    <form method="get" hx-get="{{ url_for('mentors') }}" hx-target="#mentors-list" hx-trigger="change">
        <select name="specialisation" id="specialisation">
            <option value="">Toutes les spécialisations</option>
            <option value="web">Développement Web</option>
            <option value="data">Data Science</option>
            <option value="cyber">Cybersécurité</option>
            <option value="mobile">Mobile</option>
            <option value="cloud">Cloud & DevOps</option>
            <option value="design">UI/UX Design</option>
        </select>
        <button type="submit" class="btn">Filtrer</button>
    </form>
</div>

<div id="mentors-list" class="mentors-grid">
    {% if mentors %}
        {% for mentor in mentors %}
        <div class="mentor-card">
            <div class="mentor-avatar">
                {{ mentor.prenom[0] }}{{ mentor.nom[0] }}
            </div>
            <h3>{{ mentor.prenom }} {{ mentor.nom }}</h3>
            <p class="role-badge">{{ mentor.role }}</p>
            <p class="spec-tag">{{ mentor.specialisation or 'Non spécifié' }}</p>
            <p class="bio">{{ mentor.bio or 'Pas de description' }}</p>
            <a href="{{ url_for('mentor_detail', id=mentor.id) }}" class="btn btn-small">Voir le profil</a>
        </div>
        {% endfor %}
    {% else %}
        <p class="no-results">Aucun mentor disponible pour le moment.</p>
    {% endif %}
</div>
{% endblock %}''',

    'mentor_detail.html': '''{% extends "base.html" %}

{% block title %}{{ mentor.prenom }} {{ mentor.nom }} - La Tour{% endblock %}

{% block content %}
<div class="mentor-profile">
    <div class="profile-header">
        <div class="mentor-avatar-large">
            {{ mentor.prenom[0] }}{{ mentor.nom[0] }}
        </div>
        <div class="profile-info">
            <h1>{{ mentor.prenom }} {{ mentor.nom }}</h1>
            <p class="role-badge">{{ mentor.role }}</p>
            <p class="spec-tag">{{ mentor.specialisation or 'Non spécifié' }}</p>
            <span class="status {% if mentor.disponible %}disponible{% else %}indisponible{% endif %}">
                {% if mentor.disponible %}✓ Disponible{% else %}✗ Indisponible{% endif %}
            </span>
        </div>
    </div>

    <div class="profile-content">
        <section class="bio-section">
            <h2>À propos</h2>
            <p>{{ mentor.bio or 'Pas de description disponible.' }}</p>
        </section>

        {% if mentor.disponible %}
        <section class="action-section">
            <a href="{{ url_for('demander_rdv', mentor_id=mentor.id) }}" class="btn btn-primary">
                📅 Demander un rendez-vous
            </a>
        </section>
        {% endif %}
    </div>

    <a href="{{ url_for('mentors') }}" class="btn-back">← Retour aux mentors</a>
</div>
{% endblock %}''',

    'demander_rdv.html': '''{% extends "base.html" %}

{% block title %}Demander un rendez-vous - La Tour{% endblock %}

{% block content %}
<div class="form-container">
    <h1>Demander un rendez-vous avec {{ mentor.prenom }} {{ mentor.nom }}</h1>

    <form method="post" class="rdv-form">
        <div class="form-group">
            <label for="sujet">Sujet du rendez-vous *</label>
            <input type="text" id="sujet" name="sujet" required placeholder="Ex: Aide sur React">
        </div>

        <div class="form-group">
            <label for="description">Description détaillée</label>
            <textarea id="description" name="description" rows="5" 
                      placeholder="Décrivez votre problème ou votre besoin..."></textarea>
        </div>

        <div class="form-group">
            <label for="date_rdv">Date et heure souhaitées *</label>
            <input type="datetime-local" id="date_rdv" name="date_rdv" required>
        </div>

        <div class="form-group">
            <label for="type_rdv">Type de rendez-vous *</label>
            <select id="type_rdv" name="type_rdv" required>
                <option value="en_ligne">En ligne (visio)</option>
                <option value="presentiel">En présentiel</option>
            </select>
        </div>

        <div class="form-actions">
            <button type="submit" class="btn btn-primary">Envoyer la demande</button>
            <a href="{{ url_for('mentor_detail', id=mentor.id) }}" class="btn btn-secondary">Annuler</a>
        </div>
    </form>
</div>
{% endblock %}''',

    'mes_rdv.html': '''{% extends "base.html" %}

{% block title %}Mes rendez-vous - La Tour{% endblock %}

{% block content %}
<h1>Mes rendez-vous</h1>

<div class="rdv-sections">
    <section class="rdv-section">
        <h2>Mes demandes de mentorat</h2>
        {% if rdv_demandes %}
            <div class="rdv-list">
                {% for rdv in rdv_demandes %}
                <div class="rdv-card status-{{ rdv.statut }}">
                    <div class="rdv-header">
                        <h3>{{ rdv.sujet }}</h3>
                        <span class="status-badge">{{ rdv.statut }}</span>
                    </div>
                    <p><strong>Mentor:</strong> {{ rdv.mentor.prenom }} {{ rdv.mentor.nom }}</p>
                    <p><strong>Date:</strong> {{ rdv.date_rdv.strftime('%d/%m/%Y à %H:%M') }}</p>
                    <p><strong>Type:</strong> {{ rdv.type_rdv }}</p>
                    {% if rdv.description %}
                    <p class="description">{{ rdv.description }}</p>
                    {% endif %}
                </div>
                {% endfor %}
            </div>
        {% else %}
            <p class="no-results">Vous n'avez pas encore demandé de rendez-vous.</p>
            <a href="{{ url_for('mentors') }}" class="btn">Trouver un mentor</a>
        {% endif %}
    </section>

    <section class="rdv-section">
        <h2>Rendez-vous à donner (en tant que mentor)</h2>
        {% if rdv_a_donner %}
            <div class="rdv-list">
                {% for rdv in rdv_a_donner %}
                <div class="rdv-card status-{{ rdv.statut }}">
                    <div class="rdv-header">
                        <h3>{{ rdv.sujet }}</h3>
                        <span class="status-badge">{{ rdv.statut }}</span>
                    </div>
                    <p><strong>Étudiant:</strong> {{ rdv.etudiant.prenom }} {{ rdv.etudiant.nom }}</p>
                    <p><strong>Date:</strong> {{ rdv.date_rdv.strftime('%d/%m/%Y à %H:%M') }}</p>
                    <p><strong>Type:</strong> {{ rdv.type_rdv }}</p>
                    {% if rdv.description %}
                    <p class="description">{{ rdv.description }}</p>
                    {% endif %}
                </div>
                {% endfor %}
            </div>
        {% else %}
            <p class="no-results">Aucun rendez-vous à donner pour le moment.</p>
        {% endif %}
    </section>
</div>
{% endblock %}''',

    'chatbot.html': '''{% extends "base.html" %}

{% block title %}Chatbot IA - La Tour{% endblock %}

{% block content %}
<div class="chatbot-container">
    <h1>🤖 Assistant IA</h1>
    <p class="subtitle">Posez vos questions techniques, je suis là pour vous aider !</p>

    <div id="chat-messages" class="chat-messages">
        <div class="message bot-message">
            <strong>Assistant IA:</strong>
            <p>Bonjour ! Je suis votre assistant IA pour La Tour. Comment puis-je vous aider aujourd'hui ?</p>
        </div>
    </div>

    <form id="chat-form" class="chat-form" 
          hx-post="{{ url_for('chat_api') }}"
          hx-target="#chat-messages"
          hx-swap="beforeend"
          hx-on::after-request="document.getElementById('message').value = ''">
        <input type="text" 
               id="message" 
               name="message" 
               placeholder="Posez votre question..." 
               required 
               autocomplete="off">
        <button type="submit" class="btn">Envoyer</button>
    </form>

    <div class="chat-suggestions">
        <p><strong>Exemples de questions :</strong></p>
        <button class="suggestion-btn" onclick="askQuestion('Comment déboguer mon code Python ?')">
            Comment déboguer mon code Python ?
        </button>
        <button class="suggestion-btn" onclick="askQuestion('Explique-moi HTMX')">
            Explique-moi HTMX
        </button>
        <button class="suggestion-btn" onclick="askQuestion('Aide sur Flask et SQLAlchemy')">
            Aide sur Flask et SQLAlchemy
        </button>
    </div>
</div>

<script>
function askQuestion(question) {
    document.getElementById('message').value = question;
    document.getElementById('chat-form').requestSubmit();
}

htmx.on('#chat-messages', 'htmx:afterSwap', function() {
    const chatMessages = document.getElementById('chat-messages');
    chatMessages.scrollTop = chatMessages.scrollHeight;
});
</script>
{% endblock %}'''
}

# Créer les fichiers templates
for filename, content in templates.items():
    with open(os.path.join('templates', filename), 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Créé: templates/{filename}")

# CSS
css_content = '''* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --primary-color: #6366f1;
    --secondary-color: #8b5cf6;
    --success-color: #10b981;
    --danger-color: #ef4444;
    --warning-color: #f59e0b;
    --text-color: #1f2937;
    --bg-color: #f9fafb;
    --card-bg: #ffffff;
    --border-color: #e5e7eb;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: var(--text-color);
    background-color: var(--bg-color);
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Navigation */
.navbar {
    background-color: var(--card-bg);
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    padding: 1rem 0;
    margin-bottom: 2rem;
}

.navbar .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-brand h1 {
    color: var(--primary-color);
    font-size: 1.5rem;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 2rem;
}

.nav-menu a {
    text-decoration: none;
    color: var(--text-color);
    font-weight: 500;
    transition: color 0.3s;
}

.nav-menu a:hover {
    color: var(--primary-color);
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 3rem 0;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    border-radius: 12px;
    margin-bottom: 3rem;
}

.hero h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
}

/* Features */
.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
}

.feature-card {
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    text-align: center;
    transition: transform 0.3s;
}

.feature-card:hover {
    transform: translateY(-5px);
}

.feature-card h3 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
    color: var(--primary-color);
}

/* Buttons */
.btn {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    background-color: var(--primary-color);
    color: white;
    text-decoration: none;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.3s;
    margin-top: 1rem;
}

.btn:hover {
    background-color: var(--secondary-color);
}

.btn-secondary {
    background-color: #6b7280;
}

.btn-secondary:hover {
    background-color: #4b5563;
}

.btn-small {
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
}

/* Specializations */
.specialisations {
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 12px;
    margin-bottom: 3rem;
}

.specialisations h2 {
    text-align: center;
    margin-bottom: 1.5rem;
}

.spec-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
}

.spec-badge {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 20px;
    font-weight: 500;
}

/* Mentors Grid */
.mentors-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.mentor-card {
    background: var(--card-bg);
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    text-align: center;
    transition: transform 0.3s;
}

.mentor-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.mentor-avatar {
    width: 80px;
    height: 80px;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    font-weight: bold;
    margin: 0 auto 1rem;
}

.role-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    background-color: var(--success-color);
    color: white;
    border-radius: 12px;
    font-size: 0.85rem;
    margin: 0.5rem 0;
}

.spec-tag {
    color: var(--primary-color);
    font-weight: 600;
    margin: 0.5rem 0;
}

.bio {
    color: #6b7280;
    font-size: 0.9rem;
    margin: 1rem 0;
}

/* Filters */
.filters {
    background: var(--card-bg);
    padding: 1.5rem;
    border-radius: 12px;
    margin-bottom: 2rem;
}

.filters form {
    display: flex;
    gap: 1rem;
    align-items: center;
}

.filters select {
    padding: 0.75rem;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    font-size: 1rem;
    flex: 1;
}

/* Mentor Profile */
.mentor-profile {
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 12px;
}

.profile-header {
    display: flex;
    gap: 2rem;
    align-items: center;
    margin-bottom: 2rem;
    padding-bottom: 2rem;
    border-bottom: 2px solid var(--border-color);
}

.mentor-avatar-large {
    width: 120px;
    height: 120px;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    font-weight: bold;
}

.status {
    display: inline-block;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    font-weight: 500;
    margin-top: 1rem;
}

.status.disponible {
    background-color: #d1fae5;
    color: var(--success-color);
}

.status.indisponible {
    background-color: #fee2e2;
    color: var(--danger-color);
}

/* Forms */
.form-container {
    max-width: 600px;
    margin: 0 auto;
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 12px;
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
}

.form-group input,
.form-group textarea,
.form-group select {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    font-size: 1rem;
}

.form-actions {
    display: flex;
    gap: 1rem;
    margin-top: 2rem;
}

/* RDV Cards */
.rdv-sections {
    display: grid;
    gap: 2rem;
}

.rdv-list {
    display: grid;
    gap: 1rem;
}

.rdv-card {
    background: var(--card-bg);
    padding: 1.5rem;
    border-radius: 12px;
    border-left: 4px solid var(--primary-color);
}

.rdv-card.status-en_attente {
    border-left-color: var(--warning-color);
}

.rdv-card.status-accepte {
    border-left-color: var(--success-color);
}

.rdv-card.status-refuse {
    border-left-color: var(--danger-color);
}

.rdv-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}

.status-badge {
    padding: 0.25rem 0.75rem;
    border-radius: 12px;
    background-color: var(--bg-color);
    font-size: 0.85rem;
    font-weight: 500;
}

/* Chatbot */
.chatbot-container {
    max-width: 800px;
    margin: 0 auto;
}

.chat-messages {
    background: var(--card-bg);
    border-radius: 12px;
    padding: 1.5rem;
    height: 400px;
    overflow-y: auto;
    margin-bottom: 1rem;
}

.message {
    margin-bottom: 1rem;
    padding: 1rem;
    border-radius: 8px;
}

.bot-message {
    background-color: #f3f4f6;
}

.user-message {
    background-color: #dbeafe;
    margin-left: 20%;
}

.chat-form {
    display: flex;
    gap: 1rem;
}

.chat-form input {
    flex: 1;
    padding: 0.75rem;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    font-size: 1rem;
}

.chat-suggestions {
    margin-top: 1.5rem;
    text-align: center;
}

.suggestion-btn {
    display: inline-block;
    margin: 0.5rem;
    padding: 0.5rem 1rem;
    background-color: var(--bg-color);
    border: 1px solid var(--border-color);
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.3s;
}

.suggestion-btn:hover {
    background-color: var(--primary-color);
    color: white;
}

/* Alerts */
.alert {
    padding: 1rem;
    border-radius: 8px;
    margin-bottom: 1rem;
}

.alert-success {
    background-color: #d1fae5;
    color: var(--success-color);
}

.alert-danger {
    background-color: #fee2e2;
    color: var(--danger-color);
}

/* Footer */
footer {
    background-color: var(--text-color);
    color: white;
    text-align: center;
    padding: 2rem 0;
    margin-top: 4rem;
}

/* Responsive */
@media (max-width: 768px) {
    .nav-menu {
        flex-direction: column;
        gap: 1rem;
    }
    
    .profile-header {
        flex-direction: column;
        text-align: center;
    }
    
    .features {
        grid-template-columns: 1fr;
    }
}'''

# Créer le fichier CSS
with open('static/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)
print(f"✓ Créé: static/css/style.css")

print("\n✅ Tous les fichiers ont été créés avec succès!")
print("\nPour démarrer le projet :")
print("1. Exécutez: setup.bat")
print("2. Ou manuellement:")
print("   - python -m venv venv")
print("   - venv\\Scripts\\activate")
print("   - pip install -r requirements.txt")
print("   - flask init-db")
print("   - flask seed-db")
print("   - python app.py")
