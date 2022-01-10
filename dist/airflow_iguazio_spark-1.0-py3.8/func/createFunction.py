import os
os.environ['MLRUN_DBPATH'] = 'https://mlrun-api.default-tenant.app.cvs-rx.iguazio-c0.com'
os.environ['MLRUN_ARTIFACT_PATH'] = '/User/artifacts/{{run.project}}'
os.environ['V3IO_USERNAME'] = 'abishek'
os.environ['V3IO_API'] = 'https://webapi.default-tenant.app.cvs-rx.iguazio-c0.com:8444/'
os.environ['V3IO_ACCESS_KEY'] = '99f8f20c-d4ca-4b0c-9e23-fef56997f369'
import mlrun

def main(**kwargs):

    mlrun.set_environment(project="sparksimulationab")
    project = mlrun.get_or_create_project("sparksimulationab", context="./")
    sj = mlrun.new_function(kind="spark",
                            project="sparksimulationab",
                            command="/v3io/projects/sparksimulation/runner.py",
                            name="igz_func_joba",
                            image=".mlrun/func-sparksimulation-igz_func_joba:latest")

    sj.with_driver_limits(cpu="1300m")
    sj.with_driver_requests(cpu=1, mem="512m")

    sj.with_executor_limits(cpu="1400m")
    sj.with_executor_requests(cpu=1, mem="512m")

    sj.with_igz_spark()

    sj.spec.deps['pyFiles'] = ['local:///v3io/projects/sparksimulationab/airflow_iguazio_spark-1.0-py3.8.egg']

    sj.spec.replicas = 1

    sj.deploy()
    # sj.run()
# .mlrun/func-sparksimulation-igz_test_job:latest
if __name__ == '__main__': main()