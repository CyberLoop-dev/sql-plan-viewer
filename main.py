#!/usr/bin/env python3
"""Show SQLite EXPLAIN QUERY PLAN output as a readable tree."""
import argparse
import json
import sqlite3
from pathlib import Path

def make_demo():
    connection = sqlite3.connect(":memory:")
    connection.executescript("""
        CREATE TABLE products(id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price REAL NOT NULL);
        INSERT INTO products(name, category, price) VALUES
          ('Notebook','stationery',4.5),('Desk lamp','home',24.0),('Pen set','stationery',8.0),
          ('Cable organizer','office',6.0),('Monitor stand','office',31.0),('Folder','stationery',2.0);
        CREATE INDEX idx_products_category ON products(category);
    """)
    return connection

def plan_rows(connection, query):
    cursor = connection.execute("EXPLAIN QUERY PLAN " + query)
    return [{"id": row[0], "parent": row[1], "detail": row[3]} for row in cursor.fetchall()]

def render_tree(rows):
    by_id = {row["id"]: row for row in rows}
    children = {}
    roots = []
    for row in rows:
        parent = row["parent"]
        if parent == 0 or parent not in by_id:
            roots.append(row)
        else:
            children.setdefault(parent, []).append(row)
    lines = []
    def walk(row, depth):
        lines.append("  " * depth + "- " + row["detail"])
        for child in children.get(row["id"], []):
            walk(child, depth + 1)
    for root in roots:
        walk(root, 0)
    return lines or ["(SQLite returned no plan rows)"]

def main():
    parser = argparse.ArgumentParser(description="Inspect a SQLite query plan without executing the query itself.")
    parser.add_argument("database", nargs="?", help="path to an existing SQLite database")
    parser.add_argument("query", nargs="?", help="read-only SELECT or WITH query")
    parser.add_argument("--demo", action="store_true", help="use a temporary in-memory sample database")
    parser.add_argument("--json", action="store_true", help="print the plan as JSON")
    args = parser.parse_args()
    if args.demo:
        connection = make_demo()
        query = args.query or "SELECT name FROM products WHERE category = 'stationery' ORDER BY name"
    else:
        if not args.database or not args.query:
            parser.error("provide DATABASE and QUERY, or use --demo")
        if not args.query.lstrip().lower().startswith(("select", "with")):
            parser.error("only SELECT and WITH queries are accepted")
        path = Path(args.database).expanduser().resolve()
        if not path.is_file():
            parser.error("database file does not exist: " + str(path))
        uri = path.as_uri() + "?mode=ro"
        try:
            connection = sqlite3.connect(uri, uri=True)
        except sqlite3.Error as exc:
            parser.error(str(exc))
        query = args.query
    try:
        rows = plan_rows(connection, query)
    except sqlite3.Error as exc:
        parser.error("SQLite could not explain this query: " + str(exc))
    finally:
        connection.close()
    if args.json:
        print(json.dumps({"query": query, "plan": rows}, indent=2))
    else:
        print("SQL PLAN VIEWER")
        print("=" * 48)
        print("Query: " + query)
        print("\nPlan:")
        print("\n".join(render_tree(rows)))
        print("\nThis report describes the planner's strategy; it does not measure query runtime.")

if __name__ == "__main__":
    main()
