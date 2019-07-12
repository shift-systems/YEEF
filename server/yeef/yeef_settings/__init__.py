"""Define settings using values of environment variables."""
import os
from dotenv import load_dotenv

load_dotenv()

if os.getenv('DEBUG',False):
    from .prod import *
else:
    from .dev import *
