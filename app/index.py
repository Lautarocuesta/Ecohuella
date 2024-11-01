import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, render_template, Blueprint, request, jsonify
import functions_framework

# Inicializar Firebase con el archivo de credenciales
cred = credentials.Certificate("config/ecohuella-bee0b-firebase-adminsdk-gfl5b-99b2ab0a4b.json")
firebase_admin.initialize_app(cred)

# Crear una instancia de Blueprint
bp = Blueprint('main', __name__)
db = firestore.client()  # Inicializar Firestore para usar la base de datos

@bp.route('/')
def base():
    return render_template('base.html')

@bp.route('/blog')
def blog():
    return render_template('blog.html')

@bp.route('/np')
def np():
    return render_template('np.html')

@bp.route('/api')  # Ruta para la API
def api_page():
    return render_template('api.html')  # Asegúrate de tener un archivo 'api.html'

@bp.route('/aceite')
def aceite():
    return render_template('aceite.html')

@bp.route('/basura')
def basura():
    return render_template('basura.html')

# Ruta para responder preguntas
@bp.route('/api/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question', '')

    # Ejemplo de guardado en Firestore
    db.collection('questions').add({"question": question})

    # Lógica de respuesta para la pregunta
    if "hola" in question.lower():
        answer = "¡Hola! ¿Cómo puedo ayudarte hoy?"
    elif "adiós" in question.lower():
        answer = "¡Hasta luego! Cuídate."
    else:
        answer = "Lo siento, no puedo responder esa pregunta."

    return jsonify({"question": question, "answer": answer})

@functions_framework.http
def flask_app(request):
    return app(request)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)  # Registrar el blueprint
    return app

# Ejecutar la aplicación
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
