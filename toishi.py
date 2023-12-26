import click
from pathlib import Path


def is_startswith_end_parenthesis(text: str) -> bool:
    """
    カッコ閉じで始まっているかどうか

    例:
    - "」テスト" は True
    - ")テスト" は True
    """
    return text.startswith("」") or text.startswith(")") or text.startswith("）")


def insert_newline_after_period(text: str) -> str:
    """
    「。」の後に改行を入れる
    """
    segments = text.split("。")
    for index, segment in enumerate(segments):
        if index == len(segments) - 1:
            break

        next_segment = segments[index + 1] if index + 1 < len(segments) else ""

        if not next_segment.startswith("\n") and not is_startswith_end_parenthesis(
            next_segment
        ):
            result_segment = segment + "。\n"
        else:
            result_segment = segment + "。"

        segments[index] = result_segment

    text = "".join(segments)
    return text


@click.command()
@click.argument("filepath")
def toishi(filepath: str):
    """
    指定されたファイルをフォーマットする
    """
    filepath = Path(filepath)
    filetext = filepath.read_text(encoding="utf-8")

    # 「。」の後に改行を入れる
    filetext = insert_newline_after_period(filetext)

    filepath.write_text(filetext, encoding="utf-8")
    click.echo("Done!")


if __name__ == "__main__":
    toishi()
