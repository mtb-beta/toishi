import pytest
from click.testing import CliRunner


class TestToishi:
    @pytest.fixture
    def target(self):
        from toishi import toishi

        return toishi

    def _setup_test_file(self, tmp_path, original_text):
        test_filepath = tmp_path.joinpath("test.txt")
        test_filepath.write_text(original_text, encoding="utf-8")
        return test_filepath

    @pytest.mark.xfail
    def test_toishi_call(self, tmp_path, target):
        # arrange
        original_text = (
            "テストです。\nテスト2行目です。\n\nテスト3行目です。テスト4行目です。"
        )
        expected_text = (
            "テストです。\nテスト2行目です。\n\n\nテスト3行目です。\nテスト4行目です。"
        )
        test_filepath = self._setup_test_file(tmp_path, original_text)

        # act
        runner = CliRunner()
        result = runner.invoke(target, [str(test_filepath.absolute())])

        # assert
        assert result.exit_code == 0
        actual_text = test_filepath.read_text(encoding="utf-8")
        assert actual_text == expected_text

    @pytest.mark.parametrize(
        "original_text, expected_text",
        [
            ("テストです。", "テストです。\n"),
            ("テストです。\n", "テストです。\n"),
            ("テストです。\nテスト。", "テストです。\nテスト。\n"),
            ("テストです。「テスト。」です。", "テストです。\n「テスト。」です。\n"),
            ("テストです。（テスト。）です。", "テストです。\n（テスト。）です。\n"),
            ("テストです。(テスト。)です。", "テストです。\n(テスト。)です。\n"),
        ],
    )
    def test_insert_newline_after_period(
        self, tmp_path, target, original_text, expected_text
    ):
        """
        「。」の後に改行を入れるテストケース
        """
        # arrange
        test_filepath = self._setup_test_file(tmp_path, original_text)

        # act
        runner = CliRunner()
        result = runner.invoke(target, [str(test_filepath.absolute())])

        # assert
        assert result.exit_code == 0
        actual_text = test_filepath.read_text(encoding="utf-8")
        assert actual_text == expected_text
