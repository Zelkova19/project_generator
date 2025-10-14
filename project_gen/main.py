import click

from project_gen.utils.download import init
from project_gen.utils.generate import generate
from project_gen.utils.utils import setup
from project_gen.internal.generator import Generator
from project_gen.internal.test_generator import TestsGenerator


@click.group()
def cli() -> None:
    pass


@cli.command("setup")
@click.option("--template", "-t", required=False, default=None)
def setup_command(template: str | None) -> None:
    setup(template=template)
    init()


@cli.command("generate")
def generate_command() -> None:
    generate()
    Generator().generate()
    TestsGenerator().generate()


@cli.command("init")
def init_command() -> None:
    init()


cli.add_command(generate_command)
cli.add_command(setup_command)
cli.add_command(init_command)


if __name__ == "__main__":
    cli()
