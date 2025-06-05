
from flask import Flask, render_template, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", result=False)

@app.route("/run", methods=["POST"])
def run_simulation():
    try:
        # Exécuter le script principal
        subprocess.run(["python3", "simulateur/main_squelette.py"], check=True)
        return render_template("index.html", result=True)
    except subprocess.CalledProcessError:
        return "Erreur lors de l'exécution de la simulation.", 500

@app.route("/download")
def download_result():
    path = "simulateur/resultats_uniforme.csv"
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return "Fichier non trouvé", 404

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

