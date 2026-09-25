from src.pipeline import run_pipeline
from src.load import read_table


def test_run_pipeline_end_to_end(tmp_path):
    csv_file = tmp_path / "orders.csv"
    csv_file.write_text(
        "order_id,customer,category,quantity,unit_price,order_date\n"
        "1,Jane,Books,1,10.0,2026-01-01\n"
        "2,,Books,2,10.0,2026-01-02\n"  # missing customer -> dropped
        "3,Amy,Toys,2,5.0,2026-01-03\n"
    )
    db_path = str(tmp_path / "sales.db")

    run_pipeline(str(csv_file), db_path)

    clean = read_table(db_path, "sales_clean")
    summary = read_table(db_path, "sales_by_category")

    assert len(clean) == 2  # one row dropped for missing customer
    assert set(summary["category"]) == {"Books", "Toys"}
    assert summary.loc[summary["category"] == "Books", "total_revenue"].iloc[0] == 10.0
    assert summary.loc[summary["category"] == "Toys", "total_revenue"].iloc[0] == 10.0
