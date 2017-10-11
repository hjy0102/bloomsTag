"""
bloomsTag

A CLI application built using Python utilizing the natural language processing library, nltk,
to auto-generate Bloom's Taxonomy classifiers based on inputted questions.

:copyright: (c) Hyojin Yi 2017

"""
import click
from textProcess import classify
from textProcess import synReplace

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

class Config(object):
    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)

#click group works like click.command except groups can have sub-commands
# @click.group()
@click.command(context_settings=CONTEXT_SETTINGS)
@pass_config
@click.option('--tag', '-t', is_flag=True, default=True)
@click.option('--rephrase', '-r', is_flag=True, default=False)
@click.argument('question', type=str)
def cli(config, tag, rephrase, question):

    """
    QUESTION is a string to be classified according to Blooms taxonomy
    """
    config.tag = tag
    if rephrase:
        output = synReplace(question)
        click.echo("Another way of saying '" + question + "' is :"  + output)
        return
    if tag:
        classify(question)
        return
    


# @cli.command()
# @click.option('--string', default="World", help='Your name')
# ## click types
# # File that is opened for w writable
# # output file is not required
# # default will print to stdout
# @pass_config
# @click.argument('out', type=click.File('w'), default='-', required=False)
# def say(config, string, out):
#     ### documentation string
#     """This script greets you. OUT is the file output"""
#     click.echo('Home directory is %s' %config.home_directory)
#     if config.verbose:
#         click.echo('Hello!!! We are in verbose mode')
#     ## click.echo handles python unicode better than python2.X print statement and python3.X print function
#     click.echo('Hello %s' %string, file=out)