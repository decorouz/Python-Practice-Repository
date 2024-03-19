"""Commands Module."""
# The Business layer: The part the determine what gets
# put in and take out of the persistent layer.

import sys
from datetime import datetime

from database import DatabaseManager

db = DatabaseManager("bookmark.db")


class CreateBookmarksTableCommand:
    """Initialize bookmark database table."""

    def execute(self):
        """Create table for bookmarks."""
        db.create_table("bookmarks", {
            'id': 'integer primary key autoincrement',
            'title': 'text not null',
            'url': 'text not null',
            'notes': 'text',
            'date_added': 'text not null',
        })


class AddBookmarkCommand:
    """Add bookmark."""

    def execute(self, data):
        data["date_added"] = datetime.utcnow().isoformat()
        db.add_data("bookmarks", data)
        return "Bookmark Added!"


class ListBookmarksCommand:
    """Display the bookmarks in the database."""

    def __init__(self, order_by="date_added"):
        self.order_by = order_by

    def execute(self):
        """List all bookmarks"""
        return db.select("bookmarks", order_by=self.order_by).fetchall()


class DeleteBookmarkCommand:
    """Delete bookmark from db."""

    def execute(self, data):
        db.delete('bookmarks', {'id': data})
        return 'Bookmark deleted!'


class QuitCommand:
    """Exit the program."""

    def execute(self):
        sys.exit()
