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
