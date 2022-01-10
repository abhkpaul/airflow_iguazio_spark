from mlrun import get_or_create_ctx
from modules import jobB

if __name__ == '__main__':
    context = get_or_create_ctx("iguazio")
    sparkPackage = context.get_param("spark_package")
    sparkModule = context.get_param("spark_module")
    sparkFunction = context.get_param("spark_function")
    sparkFunctionParam = context.get_param("spark_function_param")
    print('IMPORTING {} FROM {}'.format(sparkModule,sparkPackage))
    exec('from {} import {}'.format(sparkPackage,sparkModule))
    print('EXECUTING FUNCTION : {}'.format(sparkFunction))
    eval('{}.{}()'.format(sparkModule,sparkFunction,sparkFunctionParam))


# def igz_func_jobb():
#     jobB.main()

import sys
# sys.path.insert(0, '/v3io/projects/sparksimulation/spark_igz-1.0-py3.8.egg')

# exec('from {} import {}'.format(module[0], module[2]))
# exec('{}(**kwargs)'.format(module[2]))
# import jobA

# if __name__ == '__main__':
#     print("This runs before the spark context!")
#
#     jobA.main()
#
#     print("This runs after the job call")


# igz_func_jobb()
# globals()[sys.argv[1]](sys.argv[2])