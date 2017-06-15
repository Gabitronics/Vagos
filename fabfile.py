from fabric.api import *
 
def vagrant():
    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    env.hosts = ['127.0.0.1:2222']
 
    # use vagrant ssh key
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]
 
def uname():
    run('uname -a')


def autopatch():
    sudo('/opt/patchmgr/scripts/auto_patch.sh -y -n ', shell=False)



class FabricException(Exception):
    pass

def autopatch2():
    with settings(abort_exception = FabricException):
        try:
            with cd('/opt/patchmgr/scripts/'):
                sudo('bash auto_patch.sh -y -n')
        except FabricException:
            print 'host did not patch'



def patchenv():
	upload = put("auto_patch.env", "/opt/patchmgr", mode=755)
        sudo(upload) 
