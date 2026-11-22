import pytest

from orderlab.csv_report import revenue_from_csv


def test_csv_revenue(tmp_path):
    csv_file = tmp_path / "orders.csv"
    csv_file.write_text(
        "price,quantity\n10000,2\n5000,3\n",
        encoding="utf-8",
    )
    assert revenue_from_csv(csv_file) == 35_000


def test_csv_empty(tmp_path):
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("price,quantity\n", encoding="utf-8")
    assert revenue_from_csv(csv_file) == 0


def test_fixture_revenue(sample_csv):
    assert revenue_from_csv(sample_csv) == 35_000


def test_csv_missing_file(tmp_path):
    missing_file = tmp_path / "missing.csv"
    with pytest.raises(FileNotFoundError):
        revenue_from_csv(missing_file)


def test_csv_invalid_number(tmp_path):
    csv_file = tmp_path / "invalid.csv"
    csv_file.write_text(
        "price,quantity\ninvalid,2\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError):
        revenue_from_csv(csv_file)
