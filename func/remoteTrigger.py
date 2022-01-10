def trigger_igz_spark(igz_project, igz_function, spark_package, spark_module, spark_function, spark_function_param):
    import os
    os.environ['MLRUN_DBPATH'] = ''
    os.environ['MLRUN_ARTIFACT_PATH'] = '/User/artifacts/{{run.project}}'
    os.environ['V3IO_USERNAME'] = ''
    os.environ['V3IO_API'] = ''
    os.environ['V3IO_ACCESS_KEY'] = ''
    import mlrun
    mlrun.set_environment(project=igz_project)
    project = mlrun.get_or_create_project(igz_project, context="./")
    trig_func = project.get_function(igz_function)
    trig_func.run(params={"spark_package": spark_package,
                          "spark_module": spark_module,
                          "spark_function": spark_function,
                          "spark_function_param": spark_function_param})