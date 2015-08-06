# -*- coding: utf-8 -*-
import logging


log = logging.getLogger('schematizer.config')


def routes(config):
    """Add routes to the configuration."""
    config.add_route(
        'api.v1.list_namespaces',
        '/v1/namespaces'
    )
    config.add_route(
        'api.v1.list_sources_by_namespace',
        '/v1/namespaces/{namespace}/sources'
    )
    config.add_route(
        'api.v1.list_sources',
        '/v1/sources'
    )
    config.add_route(
        'api.v1.get_source_by_id',
        '/v1/sources/{source_id}'
    )
    config.add_route(
        'api.v1.update_category',
        '/v1/sources/{source_id}/category',
        request_method="POST"
    )
    config.add_route(
        'api.v1.delete_category',
        '/v1/sources/{source_id}/category',
        request_method="DELETE"
    )
    config.add_route(
        'api.v1.list_topics_by_source_id',
        '/v1/sources/{source_id}/topics'
    )
    config.add_route(
        'api.v1.get_latest_topic_by_source_id',
        '/v1/sources/{source_id}/topics/latest'
    )
    config.add_route(
        'api.v1.get_topic_by_topic_name',
        '/v1/topics/{topic_name}'
    )
    config.add_route(
        'api.v1.list_schemas_by_topic_name',
        '/v1/topics/{topic_name}/schemas'
    )
    config.add_route(
        'api.v1.get_latest_schema_by_topic_name',
        '/v1/topics/{topic_name}/schemas/latest'
    )
    # The REST URI matches in order, so please consider the
    # potential conflicts when you make changes.
    config.add_route(
        'api.v1.register_schema_from_mysql_stmts',
        '/v1/schemas/mysql'
    )
    config.add_route(
        'api.v1.register_schema',
        '/v1/schemas/avro'
    )
    config.add_route(
        'api.v1.get_schema_by_id',
        '/v1/schemas/{schema_id}'
    )
    config.add_route(
        'api.v1.get_schema_elements_by_schema_id',
        '/v1/schemas/{schema_id}/elements'
    )
    config.add_route(
        'api.v1.is_avro_schema_compatible',
        '/v1/compatibility/schemas/avro'
    )
    config.add_route(
        'api.v1.is_mysql_schema_compatible',
        '/v1/compatibility/schemas/mysql'
    )
    config.add_route(
        'api.v1.create_note',
        '/v1/notes'
    )
    config.add_route(
        'api.v1.update_note',
        '/v1/notes/{note_id}'
    )
    config.add_route(
        'api.v1.list_categories',
        '/v1/categories'
    )
    # Serve the documentation tool from /web/
    config.add_static_view(name='web', path='static/html/')
    config.add_static_view(name='static', path='static/')
