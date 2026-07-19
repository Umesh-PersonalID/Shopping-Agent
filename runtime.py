import os
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
VENV_PYTHON = PROJECT_ROOT / "agent" / "bin" / "python"
VENV_SITE_PACKAGES = PROJECT_ROOT / "agent" / "lib" / "python3.11" / "site-packages"


def bootstrap_project_python() -> None:
    """Ensure this app runs with the bundled virtualenv when available."""
    if VENV_PYTHON.exists() and Path(sys.executable).resolve() != VENV_PYTHON.resolve():
        os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), *sys.argv])

    if VENV_SITE_PACKAGES.exists() and str(VENV_SITE_PACKAGES) not in sys.path:
        sys.path.insert(0, str(VENV_SITE_PACKAGES))
