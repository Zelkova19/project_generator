from project_gen.utils.download import download
from project_gen.utils.generate import generate_api, move_files, replace_import_in_file

download()

generate_api(
    package_name="register_service",
    swagger_url="http://5.63.153.31:8085/register/openapi.json"
)

move_files(package_name="register_service")
replace_import_in_file(directory="clients/http", package_name="register_service")
