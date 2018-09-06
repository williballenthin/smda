import os
import logging

CONFIG_FILE_PATH = str(os.path.abspath(__file__))
PROJECT_ROOT = str(os.path.abspath(os.sep.join([CONFIG_FILE_PATH, ".."])))

VERSION = "1.0.1"

### An (optional) WinAPI database as generated by ApiScout (https://github.com/danielplohmann/apiscout)
API_COLLECTION_FILE = PROJECT_ROOT + os.sep + os.sep.join(["data", "apiscout_winxp_prof_sp3.json"])

### global logging-config setup
LOG_PATH = "./"
LOG_LEVEL = logging.INFO
LOG_FORMAT = "%(asctime)-15s: %(name)-32s - %(message)s"
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

### SMDA disassembler config
TIMEOUT = 120
HIGH_ACCURACY = True
RESOLVE_TAILCALLS = True
RESOLVE_REGISTER_CALLS = True