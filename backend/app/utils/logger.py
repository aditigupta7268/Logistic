import logging
import os
from datetime import datetime
from pathlib import Path

# Create logs directory if it doesn't exist
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Log file with timestamp
log_file = log_dir / f"app_{datetime.now().strftime('%Y_%m_%d')}.log"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file),  # Write to file
        logging.StreamHandler()          # Print to console
    ]
)

logger = logging.getLogger(__name__)