from os.path import exists, dirname, join

import environ 

env = environ.Env()

# Build paths inside the project like this: join(BASE_DIR, "directory")
BASE_DIR = dirname(dirname(__file__))
# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = join(BASE_DIR, "config.env")
if exists(env_file):
    environ.Env.read_env(str(env_file))