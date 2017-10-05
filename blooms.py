import click

class Config(object):
    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)

#click group works like click.command except groups can have sub-commands
@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home_directory', type=click.Path())
@pass_config
def cli(config, verbose, home_directory):
    config.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    config.home_directory = home_directory

@cli.command()
@click.option('--string', default="World", help='Your name')
## click types
# File that is opened for w writable
# output file is not required
# default will print to stdout
@pass_config
@click.argument('out', type=click.File('w'), default='-', required=False)
def say(config, string, out):
    ### documentation string
    """This script greets you. OUT is the file output"""
    click.echo('Home directory is %s' %config.home_directory)
    if config.verbose:
        click.echo('Hello!!! We are in verbose mode')
    ## click.echo handles python unicode better than python2.X print statement and python3.X print function
    click.echo('Hello %s' %string, file=out)