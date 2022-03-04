"""Project configurations."""
import os
from dotenv import load_dotenv  # type: ignore

load_dotenv()

STATS_ANVIL_API = os.getenv("STATS_ANVIL_API")
CHART_ANVIL_API = os.getenv("CHART_ANVIL_API")