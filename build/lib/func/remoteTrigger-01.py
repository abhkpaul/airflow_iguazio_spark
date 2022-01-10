import os

import mlrun

def main(**kwargs):
    mlrun.set_environment(project="sparksimulationrc")
    project=mlrun.get_or_create_project("sparksimulationrc", context="./")
    sj = project.get_function("igz_spark_submit_rc3")
    sj.spec.args=['-test', 'testmod']
    sj.run(params={"p_mods": "mymod", "mods": "pyspark_test_2"})

if __name__ == '__main__': main()

def add():
    print("do something")
