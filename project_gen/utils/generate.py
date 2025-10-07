import os
import pathlib
import shutil

from project_gen.utils.utils import run_command


def generate_api(
    package_name: str, swagger_url: str, templates: str | None = None
) -> None:
    templates = templates or str(
        pathlib.Path(__file__).parent.parent / "templates" / "python"
    )
    command = [
        "java",
        "-jar",
        ".venv/bin/openapi-generator-cli-7.16.0.jar",
        "generate",
        "-i",
        swagger_url,
        "-g",
        "python",
        "-o",
        package_name,
        "--library",
        "asyncio",
        "--package-name",
        package_name,
        "--skip-validate-spec",
    ]
    if templates:
        command.extend(["-t", templates])
    run_command(command)


def replace_import_in_file(directory: str, package_name: str) -> None:
    from_search_pattern = f"from {package_name}"
    import_search_pattern = f"import {package_name}"
    replace_pattern = f"clients.http.{package_name}"
    path = pathlib.Path(directory)
    for file_path in path.rglob("*.py"):
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        update_lines = []
        for line in lines:
            line = line.replace(from_search_pattern, f"from {replace_pattern}")
            line = line.replace(import_search_pattern, f"import {replace_pattern}")
            line = line.replace(
                f"klass = getattr({package_name}.models, klass)",
                f"klass = getattr(clients.http.{package_name}.models, klass)"
            )
            update_lines.append(line)

        with file_path.open("w", encoding="utf-8") as file:
            file.writelines(update_lines)


def move_files(package_name: str) -> None:
    if os.path.exists(f"clients/http/{package_name}"):
        shutil.rmtree(f"clients/http/{package_name}")
    shutil.move(f"{package_name}/{package_name}", f"clients/http/{package_name}")
    shutil.rmtree(package_name)
