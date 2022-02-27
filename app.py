import shutil
import os
import subprocess
from datetime import datetime


# Define link or path to ruleset
CONFIG = "p/owasp-top-ten"
SRC_FOLDER = "./src"
RES_FOLDER = "./res"


class Application(object):
    def __init__(self, zipfile, prj_name) -> None:
        self.src_location = self.extract(zipfile, prj_name)
        self.prj_name = prj_name

    # Delete src_location after scan to save storage space
    def __del__(self) -> None:
        shutil.rmtree(self.src_location)

    # Extract source code to src_location
    def extract(self, zipfile, prj_name) -> str:
        src_location = os.path.join(SRC_FOLDER, prj_name)
        shutil.unpack_archive(zipfile, src_location)
        return src_location

    def scan(self) -> str:
        now = datetime.now()
        filename = now.strftime(f"{self.prj_name}-%m-%d-%Y-%H-%M-%S.txt")
        result_path = os.path.join(RES_FOLDER, filename)
        command = ['semgrep',
                   f'--config={CONFIG}', self.src_location, '--error', '--json', '--output', result_path]
        p = subprocess.run(command, stdout=subprocess.PIPE)

        # Return code of semgrep: https://semgrep.dev/docs/cli-usage/
        if(p.returncode == 0):
            return f"Semgrep ran successfully and found no errors. Find result at '{result_path}'."
        elif(p.returncode == 1):
            return f"Semgrep ran successfully and found issues in your code. Find result at '{result_path}'."
        else:
            return "Something may be wrong with semgrep"
