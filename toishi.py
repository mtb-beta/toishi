import click


@click.command()
@click.argument("filepath")
def toishi(filepath):
    """
    指定されたファイルをフォーマットする
    """
    raise NotImplementedError()


if __name__ == "__main__":
    toishi()
