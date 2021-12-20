import os
os.environ['MLRUN_DBPATH'] = ''
os.environ['MLRUN_ARTIFACT_PATH'] = '/User/artifacts/{{run.project}}'
os.environ['V3IO_USERNAME'] = ''
os.environ['V3IO_API'] = ''
os.environ['V3IO_ACCESS_KEY'] = ''
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

    sj.spec.deps['pyFiles'] = ['local:///v3io/projects/sparksimulation/igz_func-1.0-py3.8.egg']

    sj.spec.replicas = 1

    sj.deploy()
    # sj.run()
# .mlrun/func-sparksimulation-igz_test_job:latest
if __name__ == '__main__': main()