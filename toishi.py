import click


@click.command()
@click.argument("filename")
def toishi(filename):
    """
    指定されたファイルをフォーマットする
    """
    raise NotImplementedError()


if __name__ == "__main__":
    toishi()
