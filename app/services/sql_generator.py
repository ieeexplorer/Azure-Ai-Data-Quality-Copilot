from __future__ import annotations


def generate_sql(question: str, table_name: str = "customers") -> str:
    q = question.strip().lower()

    if "count" in q and "by" in q and "country" in q and "churn" in q:
        return (
            "SELECT country, COUNT(*) AS total_customers, SUM(churn) AS churned\n"
            f"FROM {table_name}\n"
            "GROUP BY country;"
        )

    if "duplicate" in q:
        return (
            "SELECT *, COUNT(*) AS duplicate_count\n"
            f"FROM {table_name}\n"
            "GROUP BY 1\n"
            "HAVING COUNT(*) > 1;"
        )

    if "null" in q or "missing" in q:
        return (
            "-- Replace <column_name> with the column you want to inspect\n"
            f"SELECT COUNT(*) AS missing_count FROM {table_name} WHERE <column_name> IS NULL;"
        )

    if "top" in q and "country" in q:
        return (
            "SELECT country, COUNT(*) AS total\n"
            f"FROM {table_name}\n"
            "GROUP BY country\n"
            "ORDER BY total DESC\n"
            "LIMIT 10;"
        )

    return (
        "-- Could not confidently map your request to a safe SQL template in V1\n"
        f"SELECT * FROM {table_name} LIMIT 100;"
    )
