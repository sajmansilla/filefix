from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('./src/main/python/__init__.py', base=base, targetName = 'init')
]

setup(name='filefix',
      version = '1.0',
      description = 'file',
      options = dict(build_exe = buildOptions),
      executables = executables, requires=['easygui'])
