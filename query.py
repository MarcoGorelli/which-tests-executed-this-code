import os
import pprint
import sqlite3

from coverage.numbits import register_sqlite_functions

conn = sqlite3.connect(".coverage")
register_sqlite_functions(conn)
c = conn.cursor()
result = c.execute(
    "select context.context "
    "from arc, context, file "
    "where arc.context_id = context.id "
    "and arc.file_id = file.id "
    "and arc.tono = ? "
    "and file.path = ?",
    (2, os.path.abspath("t.py")),
)
pprint.pprint(result.fetchall())
