from edvalpy import Edval
import typer


def main(
    token: str = typer.Option("", help="Your Edval WebCode"),
    path: str = typer.Option("", help="Path where your Edval csvs will be saved"),
):
    edval = Edval(token)
    for file in edval.ischolaris.files():
        edval.ischolaris.save_file(file, path)


typer.run(main)
