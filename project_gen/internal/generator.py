from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from project_gen.internal.collector import ClientCollector
from inflection import camelize, underscore



class Generator:
    def __init__(self):
        self.clients = ClientCollector().collect_clients()
        self.templates_dir = Path(__file__).parent.parent / "templates" / "tests"
        self.env = Environment(loader=FileSystemLoader(self.templates_dir), autoescape=True)
        self.env.filters["underscore"] = underscore
        self.env.filters["camelize"] = camelize

    def generate(self):
        fixture_template = self.env.get_template("fixtures.jinja2")
        fixtures = fixture_template.render(clients=self.clients)
        with open("clients/fixtures.py", "w", encoding="utf-8") as f:
            f.write(fixtures)

        return fixtures
    