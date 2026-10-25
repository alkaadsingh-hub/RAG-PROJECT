import os
from dotenv import load_dotenv
import os

load_dotenv()
print("API KEY USED:", os.getenv("GOOGLE_API_KEY"))
