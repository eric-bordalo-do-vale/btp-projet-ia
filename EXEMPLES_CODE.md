# 📝 EXEMPLES DE CODE - La Tour

Ce fichier contient des exemples de code pour implémenter les fonctionnalités futures.

---

## 🔐 1. Authentification avec Flask-Login

### Installation
```bash
pip install Flask-Login Flask-Bcrypt
```

### Mise à jour du modèle User
```python
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

class User(UserMixin, db.Model):
    # ... champs existants ...
    password_hash = db.Column(db.String(128))
    
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
```

### Configuration Flask-Login
```python
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

### Routes d'authentification
```python
@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        
        # Vérifier si l'email existe déjà
        if User.query.filter_by(email=email).first():
            flash('Cet email est déjà utilisé', 'danger')
            return redirect(url_for('inscription'))
        
        # Créer le nouvel utilisateur
        user = User(
            email=email,
            nom=nom,
            prenom=prenom,
            role='etudiant'
        )
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Inscription réussie ! Vous pouvez maintenant vous connecter.', 'success')
        return redirect(url_for('login'))
    
    return render_template('inscription.html')

@app.route('/connexion', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user, remember=True)
            flash('Connexion réussie !', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Email ou mot de passe incorrect', 'danger')
    
    return render_template('login.html')

@app.route('/deconnexion')
@login_required
def logout():
    logout_user()
    flash('Vous êtes déconnecté', 'info')
    return redirect(url_for('index'))

@app.route('/profil')
@login_required
def profil():
    return render_template('profil.html', user=current_user)
```

### Template de connexion (templates/login.html)
```html
{% extends "base.html" %}

{% block content %}
<div class="form-container">
    <h1>Connexion</h1>
    <form method="post">
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
            <label for="password">Mot de passe</label>
            <input type="password" id="password" name="password" required>
        </div>
        <button type="submit" class="btn">Se connecter</button>
    </form>
    <p>Pas encore de compte ? <a href="{{ url_for('inscription') }}">S'inscrire</a></p>
</div>
{% endblock %}
```

---

## 🤖 2. Chatbot avec OpenAI

### Installation
```bash
pip install openai
```

### Configuration
```python
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

SYSTEM_PROMPT = """Tu es un assistant pour La Tour, une plateforme de mentorat 
pour étudiants en informatique. Tu dois aider les étudiants avec leurs questions 
techniques en Python, Flask, HTMX, SQL, etc. Sois pédagogue et donne des exemples."""

@app.route('/api/chat', methods=['POST'])
def chat_api():
    user_message = request.json.get('message', '')
    specialisation = request.json.get('specialisation', 'general')
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"[{specialisation}] {user_message}"}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        bot_response = response.choices[0].message.content
        
        # Sauvegarder l'historique si nécessaire
        if current_user.is_authenticated:
            conversation = ChatHistory(
                user_id=current_user.id,
                question=user_message,
                reponse=bot_response
            )
            db.session.add(conversation)
            db.session.commit()
        
        return {
            'reponse': bot_response,
            'status': 'success'
        }
    
    except Exception as e:
        return {
            'reponse': "Désolé, je n'ai pas pu traiter votre demande.",
            'status': 'error',
            'error': str(e)
        }, 500
```

### Alternative gratuite : Chatbot simple avec FAQ
```python
FAQ_DATABASE = {
    'python': {
        'keywords': ['python', 'py', 'script'],
        'responses': [
            "Python est un langage de programmation polyvalent...",
            "Pour déboguer en Python, utilisez print() ou le module pdb...",
            "Les meilleures pratiques Python incluent le PEP 8..."
        ]
    },
    'flask': {
        'keywords': ['flask', 'route', 'render_template'],
        'responses': [
            "Flask est un micro-framework web Python...",
            "Pour créer une route : @app.route('/path')...",
            "render_template() permet d'afficher des templates HTML..."
        ]
    },
    'htmx': {
        'keywords': ['htmx', 'hx-get', 'hx-post'],
        'responses': [
            "HTMX permet de créer des interfaces dynamiques sans JavaScript...",
            "hx-get envoie une requête GET et met à jour le contenu...",
            "hx-target définit où afficher la réponse..."
        ]
    }
}

def simple_chatbot(message):
    message_lower = message.lower()
    
    for topic, data in FAQ_DATABASE.items():
        for keyword in data['keywords']:
            if keyword in message_lower:
                import random
                return random.choice(data['responses'])
    
    return "Je ne suis pas sûr de comprendre. Pouvez-vous reformuler ou contacter un mentor ?"
```

---

## 📧 3. Système de notifications par email

### Installation
```bash
pip install Flask-Mail
```

### Configuration
```python
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@latour.io'

mail = Mail(app)

def send_rdv_notification(rdv):
    """Envoyer une notification pour un nouveau RDV"""
    msg = Message(
        'Nouvelle demande de rendez-vous',
        recipients=[rdv.mentor.email]
    )
    
    msg.body = f"""
    Bonjour {rdv.mentor.prenom},
    
    Vous avez reçu une nouvelle demande de rendez-vous :
    
    Sujet : {rdv.sujet}
    Date : {rdv.date_rdv.strftime('%d/%m/%Y à %H:%M')}
    Étudiant : {rdv.etudiant.prenom} {rdv.etudiant.nom}
    
    Connectez-vous pour accepter ou refuser cette demande.
    
    Cordialement,
    L'équipe La Tour
    """
    
    msg.html = render_template('emails/nouveau_rdv.html', rdv=rdv)
    
    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Erreur d'envoi d'email : {e}")
        return False
```

---

## 💬 4. Messagerie interne

### Modèle de base de données
```python
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expediteur_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    destinataire_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sujet = db.Column(db.String(200))
    contenu = db.Column(db.Text, nullable=False)
    lu = db.Column(db.Boolean, default=False)
    date_envoi = db.Column(db.DateTime, default=datetime.utcnow)
    
    expediteur = db.relationship('User', foreign_keys=[expediteur_id], backref='messages_envoyes')
    destinataire = db.relationship('User', foreign_keys=[destinataire_id], backref='messages_recus')
```

### Routes
```python
@app.route('/messages')
@login_required
def messages():
    messages_recus = Message.query.filter_by(destinataire_id=current_user.id).order_by(Message.date_envoi.desc()).all()
    messages_envoyes = Message.query.filter_by(expediteur_id=current_user.id).order_by(Message.date_envoi.desc()).all()
    
    return render_template('messages.html', 
        messages_recus=messages_recus,
        messages_envoyes=messages_envoyes
    )

@app.route('/messages/envoyer/<int:destinataire_id>', methods=['GET', 'POST'])
@login_required
def envoyer_message(destinataire_id):
    destinataire = User.query.get_or_404(destinataire_id)
    
    if request.method == 'POST':
        nouveau_message = Message(
            expediteur_id=current_user.id,
            destinataire_id=destinataire_id,
            sujet=request.form.get('sujet'),
            contenu=request.form.get('contenu')
        )
        db.session.add(nouveau_message)
        db.session.commit()
        
        flash('Message envoyé !', 'success')
        return redirect(url_for('messages'))
    
    return render_template('envoyer_message.html', destinataire=destinataire)

@app.route('/messages/lire/<int:message_id>')
@login_required
def lire_message(message_id):
    message = Message.query.get_or_404(message_id)
    
    if message.destinataire_id != current_user.id:
        abort(403)
    
    message.lu = True
    db.session.commit()
    
    return render_template('lire_message.html', message=message)
```

### Template avec HTMX (refresh auto)
```html
<div hx-get="/api/messages/non-lus" 
     hx-trigger="every 10s"
     hx-target="#notification-badge">
    <span id="notification-badge" class="badge">0</span>
</div>
```

---

## ⭐ 5. Système de notation

### Modèle
```python
class Avis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    etudiant_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rdv_id = db.Column(db.Integer, db.ForeignKey('rendez_vous.id'))
    note = db.Column(db.Integer, nullable=False)  # 1 à 5
    commentaire = db.Column(db.Text)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
    
    mentor = db.relationship('User', foreign_keys=[mentor_id], backref='avis_recus')
    etudiant = db.relationship('User', foreign_keys=[etudiant_id], backref='avis_donnes')

    def __repr__(self):
        return f'<Avis {self.note}/5 pour {self.mentor.nom}>'
```

### Routes
```python
@app.route('/avis/donner/<int:rdv_id>', methods=['GET', 'POST'])
@login_required
def donner_avis(rdv_id):
    rdv = RendezVous.query.get_or_404(rdv_id)
    
    # Vérifier que le RDV est terminé et que c'est l'étudiant
    if rdv.statut != 'termine' or rdv.etudiant_id != current_user.id:
        flash('Vous ne pouvez pas donner d\'avis pour ce rendez-vous', 'danger')
        return redirect(url_for('mes_rdv'))
    
    # Vérifier qu'un avis n'a pas déjà été donné
    avis_existant = Avis.query.filter_by(rdv_id=rdv_id).first()
    if avis_existant:
        flash('Vous avez déjà donné un avis pour ce rendez-vous', 'info')
        return redirect(url_for('mes_rdv'))
    
    if request.method == 'POST':
        avis = Avis(
            mentor_id=rdv.mentor_id,
            etudiant_id=current_user.id,
            rdv_id=rdv_id,
            note=int(request.form.get('note')),
            commentaire=request.form.get('commentaire')
        )
        db.session.add(avis)
        db.session.commit()
        
        flash('Merci pour votre avis !', 'success')
        return redirect(url_for('mes_rdv'))
    
    return render_template('donner_avis.html', rdv=rdv)

def calculer_note_moyenne(mentor_id):
    """Calculer la note moyenne d'un mentor"""
    avis = Avis.query.filter_by(mentor_id=mentor_id).all()
    
    if not avis:
        return None
    
    total = sum(a.note for a in avis)
    return round(total / len(avis), 1)
```

### Affichage des étoiles (CSS)
```html
<div class="rating">
    {% set note_moyenne = calculer_note_moyenne(mentor.id) %}
    {% if note_moyenne %}
        {% for i in range(5) %}
            <span class="star {% if i < note_moyenne %}filled{% endif %}">★</span>
        {% endfor %}
        <span class="note-text">{{ note_moyenne }}/5</span>
    {% else %}
        <span class="no-rating">Pas encore d'avis</span>
    {% endif %}
</div>
```

---

## 📊 6. Statistiques et Dashboard

```python
@app.route('/stats')
@login_required
def stats():
    # Stats générales
    total_users = User.query.count()
    total_mentors = User.query.filter(User.role.in_(['intervenant', 'partenaire'])).count()
    total_etudiants = User.query.filter_by(role='etudiant').count()
    total_rdv = RendezVous.query.count()
    
    # Stats personnelles
    if current_user.role == 'etudiant':
        mes_rdv = RendezVous.query.filter_by(etudiant_id=current_user.id).count()
        rdv_termines = RendezVous.query.filter_by(
            etudiant_id=current_user.id, 
            statut='termine'
        ).count()
    else:
        mes_rdv = RendezVous.query.filter_by(mentor_id=current_user.id).count()
        rdv_termines = RendezVous.query.filter_by(
            mentor_id=current_user.id, 
            statut='termine'
        ).count()
    
    # RDV par spécialisation
    from sqlalchemy import func
    rdv_par_spec = db.session.query(
        User.specialisation,
        func.count(RendezVous.id)
    ).join(RendezVous, RendezVous.mentor_id == User.id)\
     .group_by(User.specialisation).all()
    
    return render_template('stats.html',
        total_users=total_users,
        total_mentors=total_mentors,
        total_etudiants=total_etudiants,
        total_rdv=total_rdv,
        mes_rdv=mes_rdv,
        rdv_termines=rdv_termines,
        rdv_par_spec=rdv_par_spec
    )
```

---

## 🔔 7. Notifications en temps réel avec HTMX

### API pour les notifications
```python
@app.route('/api/notifications')
@login_required
def get_notifications():
    # RDV en attente pour un mentor
    if current_user.role in ['intervenant', 'partenaire']:
        rdv_attente = RendezVous.query.filter_by(
            mentor_id=current_user.id,
            statut='en_attente'
        ).count()
        
        messages_non_lus = Message.query.filter_by(
            destinataire_id=current_user.id,
            lu=False
        ).count()
        
        return render_template('partials/notifications.html',
            rdv_attente=rdv_attente,
            messages_non_lus=messages_non_lus
        )
    
    return render_template('partials/notifications.html',
        rdv_attente=0,
        messages_non_lus=0
    )
```

### Template (templates/partials/notifications.html)
```html
{% if rdv_attente > 0 %}
<div class="notification-item">
    <a href="{{ url_for('mes_rdv') }}">
        📅 {{ rdv_attente }} demande{% if rdv_attente > 1 %}s{% endif %} de RDV en attente
    </a>
</div>
{% endif %}

{% if messages_non_lus > 0 %}
<div class="notification-item">
    <a href="{{ url_for('messages') }}">
        💬 {{ messages_non_lus }} message{% if messages_non_lus > 1 %}s{% endif %} non lu{% if messages_non_lus > 1 %}s{% endif %}
    </a>
</div>
{% endif %}
```

### Intégration dans base.html
```html
<div id="notifications" 
     hx-get="/api/notifications" 
     hx-trigger="every 15s"
     hx-swap="innerHTML">
</div>
```

---

## 📅 8. Calendrier de disponibilités

### Modèle
```python
class Disponibilite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    jour_semaine = db.Column(db.Integer)  # 0=Lundi, 6=Dimanche
    heure_debut = db.Column(db.Time, nullable=False)
    heure_fin = db.Column(db.Time, nullable=False)
    recurrent = db.Column(db.Boolean, default=True)
    
    mentor = db.relationship('User', backref='disponibilites')
```

### Routes
```python
@app.route('/disponibilites')
@login_required
def mes_disponibilites():
    if current_user.role == 'etudiant':
        flash('Cette page est réservée aux mentors', 'danger')
        return redirect(url_for('index'))
    
    dispos = Disponibilite.query.filter_by(mentor_id=current_user.id).all()
    return render_template('disponibilites.html', disponibilites=dispos)

@app.route('/disponibilites/ajouter', methods=['POST'])
@login_required
def ajouter_disponibilite():
    nouvelle_dispo = Disponibilite(
        mentor_id=current_user.id,
        jour_semaine=int(request.form.get('jour')),
        heure_debut=datetime.strptime(request.form.get('heure_debut'), '%H:%M').time(),
        heure_fin=datetime.strptime(request.form.get('heure_fin'), '%H:%M').time()
    )
    db.session.add(nouvelle_dispo)
    db.session.commit()
    
    return '', 200  # Pour HTMX
```

---

Voilà ! Ces exemples vous donneront une bonne base pour développer les fonctionnalités avancées de La Tour. 🚀
