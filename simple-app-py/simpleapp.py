from flask import Flask, render_template, request, jsonify
from datetime import datetime
import subprocess
import os

app = Flask(__name__)

SCRIPTS_FOLDER = "scripts"

def list_scripts():
    files = []
    for f in os.listdir(SCRIPTS_FOLDER):
        if f.endswith(".py"):
            files.append(f)
    return files


@app.route("/")
def index():
    scripts = list_scripts()
    current_datetime = datetime.now()
    datetimeformated = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
    return render_template("index.html", scripts=scripts, datetimeformated=datetimeformated)


@app.route("/run", methods=["POST"])
def run_script():

    script_name = request.form.get("script")
    user_input = request.form.get("input", "")

    script_path = os.path.join(SCRIPTS_FOLDER, script_name)

    try:
        result = subprocess.run(
            ["python3", script_path],
            input=user_input,
            capture_output=True,
            text=True,
            timeout=10
        )

        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        })

    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out"}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
