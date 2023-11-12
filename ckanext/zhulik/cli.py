import click


@click.group(short_help="zhulik CLI.")
def zhulik():
    """zhulik CLI.
    """
    pass


@zhulik.command()
@click.argument("name", default="zhulik")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [zhulik]
