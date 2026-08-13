import click

@click.command()
def hello():
    """Hello from practice app"""
    click.echo("welcome to frappe")
commands=[hello]
