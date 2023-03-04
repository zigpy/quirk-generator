import click

from quirk_generator.generate_quirk import generate_stub_quirk
from quirk_generator.locate_matches import locate_quirk_matches
from quirk_generator.utils import prepare_input


@click.group()
def cli():
    pass


@cli.command()
@click.argument("signature", type=click.File("r"))
@click.option("--output", type=click.File("w"), default="-")
def generate_quirk(signature, output):
    json = prepare_input(signature.read())
    quirk = generate_stub_quirk(json)
    output.write(quirk)
    output.close()


@cli.command()
@click.argument("signature", type=click.File("r"))
def locate_matches(signature):
    click.echo("Locating matches...")
    json = prepare_input(signature.read())
    matches = locate_quirk_matches(json)
    if matches:
        click.echo("Possible matches:\n")
        for match in matches:
            click.echo(match)
    else:
        click.echo("No matches found.")
