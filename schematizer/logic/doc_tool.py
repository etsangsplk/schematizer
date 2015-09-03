# -*- coding: utf-8 -*-
from schematizer import models

from schematizer.models.database import session

import datetime

def get_note_by_reference_id_and_type(reference_id, reference_type):
    return session.query(
        models.Note
    ).filter(
        models.Note.reference_type == reference_type,
        models.Note.reference_id == reference_id
    ).first()


def get_note_by_id(id):
    return session.query(
        models.Note
    ).filter(
        models.Note.id == id
    ).first()


def update_note(id, note_text, last_updated_by):
    return session.query(
        models.Note
    ).filter(
        models.Note.id == id
    ).update(
        {
            models.Note.note: note_text,
            models.Note.last_updated_by: last_updated_by,
	    models.Note.updated_at: datetime.datetime.now()
        }
    )


def create_note(reference_type, reference_id, note_text, last_updated_by):
    note = models.Note(
        reference_type=reference_type,
        reference_id=reference_id,
        note=note_text,
        last_updated_by=last_updated_by
    )
    session.add(note)
    session.flush()
    return note


def get_distinct_categories():
    categories = session.query(models.SourceCategory.category).distinct().all()
    # categories is a list of single item lists. Return a single layered list.
    return [category for category, in categories]


def get_source_category_by_source_id(source_id):
    return session.query(
        models.SourceCategory
    ).filter(
        models.SourceCategory.source_id == source_id
    ).first()


def update_source_category(source_id, category):
    return session.query(
        models.SourceCategory
    ).filter(
        models.SourceCategory.source_id == source_id
    ).update(
        {
            models.SourceCategory.category: category
        }
    )


def create_source_category(source_id, category):
    source_category = models.SourceCategory(
        source_id=source_id,
        category=category
    )
    session.add(source_category)
    session.flush()
    return source_category


def delete_source_category_by_source_id(source_id):
    return session.query(
        models.SourceCategory
    ).filter(
        models.SourceCategory.source_id == source_id
    ).delete()
