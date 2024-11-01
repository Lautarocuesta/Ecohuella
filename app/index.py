from flask import Flask, render_template, Blueprint, request, jsonify

# Crear una instancia de Blueprint
bp = Blueprint('main', __name__)


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

    # Aquí puedes agregar la lógica para generar una respuesta a la pregunta
    # Por ahora, solo devolveremos una respuesta estática como ejemplo
    if "hola" in question.lower():
        answer = "¡Hola! ¿Cómo puedo ayudarte hoy?"
    elif "adiós" in question.lower():
        answer = "¡Hasta luego! Cuídate."
    else:
        answer = "Lo siento, no puedo responder esa pregunta."

    return jsonify({"question": question, "answer": answer})

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)  # Registrar el blueprint
    return app

# Ejecutar la aplicación
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)