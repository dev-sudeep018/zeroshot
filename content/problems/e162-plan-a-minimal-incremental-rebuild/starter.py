def incremental_rebuild(dependencies, previous, current):
    """Propagate changed input fingerprints through a DAG and return affected tasks in dependency order."""
    # Visit prerequisites before dependents so dirty status is already known when
    # processing a task.
    raise NotImplementedError("Implement the transformation")
