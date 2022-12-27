import sqlite3
import os
from coverage.numbits import register_sqlite_functions
import pprint

conn = sqlite3.connect('.coverage')
register_sqlite_functions(conn)
c = conn.cursor()
# Find all tests which hit line 47 from file src/my_file.py
result = c.execute(
    "select context.context "
    "from line_bits, context, file "
    "where line_bits.context_id = context.id "
    "and line_bits.file_id = file.id "
    "and num_in_numbits(?, numbits) "
    "and file.path = ?",
    (2, os.path.abspath('t.py'))
)
pprint.pprint(result.fetchall())
