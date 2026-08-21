import os
import sys

# Vercel loads this file with /api as the function directory.
# Add the repository root so local modules (main.py, xC4.py, Pb2, etc.) resolve reliably.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from main import app

# Vercel's Python runtime discovers the Flask WSGI application as `app`.
