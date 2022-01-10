def trigger_igz_spark(igz_project, igz_function, spark_package, spark_module, spark_function, spark_function_param):
    import os
    os.environ['MLRUN_DBPATH'] = 'https://mlrun-api.default-tenant.app.cvs-rx.iguazio-c0.com'
    os.environ['MLRUN_ARTIFACT_PATH'] = '/User/artifacts/{{run.project}}'
    os.environ['V3IO_USERNAME'] = 'abishek'
    os.environ['V3IO_API'] = 'https://webapi.default-tenant.app.cvs-rx.iguazio-c0.com:8444/'
    os.environ['V3IO_ACCESS_KEY'] = '99f8f20c-d4ca-4b0c-9e23-fef56997f369'
    import mlrun
    mlrun.set_environment(project=igz_project)
    project = mlrun.get_or_create_project(igz_project, context="./")
    trig_func = project.get_function(igz_function)
    trig_func.run(params={"spark_package": spark_package,
                          "spark_module": spark_module,
                          "spark_function": spark_function,
                          "spark_function_param": spark_function_param})