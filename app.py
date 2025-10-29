from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-this')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///latour.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modèles de base de données
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)  # etudiant, intervenant, partenaire
    specialisation = db.Column(db.String(100))  # web, data, cyber, etc
    bio = db.Column(db.Text)
    disponible = db.Column(db.Boolean, default=True)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relations
    rendez_vous_demandes = db.relationship('RendezVous', foreign_keys='RendezVous.etudiant_id', backref='etudiant')
    rendez_vous_donnes = db.relationship('RendezVous', foreign_keys='RendezVous.mentor_id', backref='mentor')

class RendezVous(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    etudiant_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mentor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sujet = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    date_rdv = db.Column(db.DateTime, nullable=False)
    type_rdv = db.Column(db.String(20), default='en_ligne')  # en_ligne ou presentiel
    statut = db.Column(db.String(20), default='en_attente')  # en_attente, accepte, refuse, termine
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)

# Routes principales
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mentors')
def mentors():
    specialisation = request.args.get('specialisation', '')
    query = User.query.filter(User.role == 'intervenant')
    
    if specialisation:
        query = query.filter_by(specialisation=specialisation)
    
    mentors = query.filter_by(disponible=True).all()
    return render_template('mentors.html', mentors=mentors)

@app.route('/mentor/<int:id>')
def mentor_detail(id):
    mentor = User.query.get_or_404(id)
    return render_template('mentor_detail.html', mentor=mentor)

@app.route('/rendez-vous/demander/<int:mentor_id>', methods=['GET', 'POST'])
def demander_rdv(mentor_id):
    mentor = User.query.get_or_404(mentor_id)
    
    if mentor.role != 'intervenant':
        flash('Cet utilisateur n\'est pas un mentor disponible.', 'error')
        return redirect(url_for('mentors'))
    
    if not mentor.disponible:
        flash('Ce mentor n\'est pas disponible actuellement.', 'warning')
        return redirect(url_for('mentor_detail', id=mentor_id))
    
    if request.method == 'POST':
        # Simuler un étudiant connecté (à remplacer par un vrai système d'auth)
        etudiant = User.query.filter_by(role='etudiant').first()
        if not etudiant:
            flash('Erreur: Aucun étudiant trouvé. Veuillez créer un compte étudiant.', 'error')
            return redirect(url_for('mentors'))
        
        try:
            date_rdv = datetime.strptime(request.form.get('date_rdv'), '%Y-%m-%dT%H:%M')
            
            if date_rdv < datetime.now():
                flash('La date du rendez-vous doit être dans le futur.', 'error')
                return render_template('demander_rdv.html', mentor=mentor)
            
            nouveau_rdv = RendezVous(
                etudiant_id=etudiant.id,
                mentor_id=mentor_id,
                sujet=request.form.get('sujet'),
                description=request.form.get('description'),
                date_rdv=date_rdv,
                type_rdv=request.form.get('type_rdv')
            )
            
            db.session.add(nouveau_rdv)
            db.session.commit()
            
            flash('Votre demande de rendez-vous a été envoyée !', 'success')
            return redirect(url_for('mes_rdv'))
        except ValueError:
            flash('Format de date invalide.', 'error')
            return render_template('demander_rdv.html', mentor=mentor)
        except Exception as e:
            db.session.rollback()
            flash(f'Erreur lors de la création du rendez-vous: {str(e)}', 'error')
            return render_template('demander_rdv.html', mentor=mentor)
    
    return render_template('demander_rdv.html', mentor=mentor)

@app.route('/mes-rendez-vous')
def mes_rdv():
    # Simuler un utilisateur connecté (récupère le premier étudiant)
    user = User.query.filter_by(role='etudiant').first()
    if not user:
        flash('Aucun utilisateur trouvé. Veuillez créer un compte.', 'error')
        return redirect(url_for('index'))
    
    rdv_demandes = RendezVous.query.filter_by(etudiant_id=user.id).all()
    rdv_a_donner = RendezVous.query.filter_by(mentor_id=user.id).all()
    
    return render_template('mes_rdv.html', rdv_demandes=rdv_demandes, rdv_a_donner=rdv_a_donner)

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/devenir-mentor')
def devenir_mentor():
    return render_template('devenir_mentor.html')

@app.route('/api/chat', methods=['POST'])
def chat_api():
    if not request.json:
        return {'erreur': 'Requête invalide'}, 400
    
    message = request.json.get('message', '').strip()
    
    if not message:
        return {'erreur': 'Message vide'}, 400
    
    if len(message) > 500:
        return {'erreur': 'Message trop long (max 500 caractères)'}, 400
    
    # Échapper le message pour éviter XSS
    from markupsafe import escape
    message_safe = escape(message)
    
    # Réponse simple du chatbot (à améliorer avec une vraie IA)
    reponse = f"Merci pour votre question : '{message_safe}'. Notre chatbot est en cours de développement pour mieux vous répondre !"
    
    return {'reponse': reponse}

# Initialisation de la base de données
@app.cli.command()
def init_db():
    """Initialise la base de données"""
    db.create_all()
    print("Base de données initialisée !")

@app.cli.command()
def seed_db():
    """Ajoute des données de test"""
    # Créer des utilisateurs de test
    users = [
        User(nom='Dupont', prenom='Jean', email='jean.dupont@laplateforme.io', 
             role='intervenant', specialisation='web', bio='Expert en développement web', disponible=True),
        User(nom='Martin', prenom='Sophie', email='sophie.martin@laplateforme.io',
             role='intervenant', specialisation='data', bio='Spécialiste Data Science', disponible=True),
        User(nom='Durand', prenom='Pierre', email='pierre.durand@laplateforme.io',
             role='etudiant', specialisation='cyber', bio='Étudiant en cybersécurité', disponible=True),
        User(nom='Leroy', prenom='Marie', email='marie.leroy@laplateforme.io',
             role='intervenant', specialisation='web', bio='Mentor bénévole en React', disponible=True),
    ]
    
    for user in users:
        existing = User.query.filter_by(email=user.email).first()
        if not existing:
            db.session.add(user)
    
    db.session.commit()
    print("Données de test ajoutées !")

if __name__ == '__main__':
    app.run(debug=True)
