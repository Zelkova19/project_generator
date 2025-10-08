import os
import platform
import shutil

import requests


def download() -> None:
    url = "https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.16.0/openapi-generator-cli-7.16.0.jar"
    with requests.get(url, stream=True, timeout=100, verify=False) as response:
        response.raise_for_status()
        file_name = "openapi-generator-cli-7.16.0.jar"
        with open(file_name, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        if platform.system() != "Windows":
            os.chmod(file_name, 0o755)

    shutil.move(file_name, f".venv/bin/{file_name}")
