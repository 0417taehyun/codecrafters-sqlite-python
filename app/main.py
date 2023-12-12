import sys

from dataclasses import dataclass

# import sqlparse - available if you need it!

database_file_path = sys.argv[1]
command = sys.argv[2]

if command == ".dbinfo":
    with open(database_file_path, "rb") as database_file:

        # Database header
        # The first 100 bytes of the database file comprise the database file header.
        
        # From 0 to 16 bytes of the database file is the header string: "SQLite format 3\000."
        database_file.seek(16)

        # From 16 to 18 bytes of the database file is the database page size in bytes.
        # All multibyte fields in the database file header are stored with the most significant byte first (big-endian).
        # This is why we use "big" for byteorder.
        page_size: int = int.from_bytes(database_file.read(2), byteorder="big")
        print(f"database page size: {page_size}")
else:
    print(f"Invalid command: {command}")
    