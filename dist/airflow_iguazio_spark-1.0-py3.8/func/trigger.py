from func import remoteTrigger as f

def func(project='',function='',switch=''):
    if(switch=="True"):
        f.trigger_igz_spark(project,function,switch)