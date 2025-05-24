"""Grading"""

import os
import subprocess

def test_01():
    script_path = os.path.join(os.path.dirname(__file__), "..", "run.sh")
    assert os.path.isfile(script_path), f"Script no encontrado: {script_path}"

    try:
        subprocess.run(
            [script_path],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")

    assert os.path.exists("mlruns"), "mlruns directory does not exist."

    experiments = [
        d for d in os.listdir("mlruns") if os.path.isdir(os.path.join("mlruns", d))
    ]
    assert len(experiments) > 0, "No experiments found in mlruns directory."
