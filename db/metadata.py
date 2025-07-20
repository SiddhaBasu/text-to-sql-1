import psycopg2

def get_sor_metadata(target_sors, pg_config):
    """
    Query sor_data_catalog for all rows where sor_nm in target_sors.
    Returns a list of dicts.
    """
    conn = psycopg2.connect(**pg_config)
    cur = conn.cursor()
    format_strings = ','.join(['%s'] * len(target_sors))
    query = f"""
        SELECT sor_nm, table_nm, attr_nm, is_sde_field, source_channel, attr_format,
               record_identifier, joiningPredicate, filterPredicate, isActive, specificDateFilterFlag
        FROM sor_data_catalogue
        WHERE sor_nm IN ({format_strings})
    """
    cur.execute(query, tuple(target_sors))
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    metadata = [dict(zip(columns, row)) for row in rows]
    cur.close()
    conn.close()
    return metadata 