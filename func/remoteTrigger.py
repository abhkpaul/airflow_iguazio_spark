def trigger_igz_spark(project, function):
    import os
    os.environ['MLRUN_DBPATH'] = ''
    os.environ['MLRUN_ARTIFACT_PATH'] = '/User/artifacts/{{run.project}}'
    os.environ['V3IO_USERNAME'] = ''
    os.environ['V3IO_API'] = ''
    os.environ['V3IO_ACCESS_KEY'] = ''
    import mlrun
    mlrun.set_environment(project=project)
    project = mlrun.get_or_create_project(project, context="./")
    trig_func = project.get_function(function)
    trig_func.run(params="")