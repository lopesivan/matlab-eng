# -*- coding: utf-8 -*-

# para a correta compilação é necessario alterar o arquivo C:\Python27\Lib\site-packages\numpy\core\__init__.py comentando
# a linha que contem "del sys"

from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "matplotlib.backends.backend_tkagg", "scipy.optimize.linesearch", "scipy.optimize.minpack2", "scipy.optimize.minpack", "scipy.optimize._minpack", "scipy.optimize._lbfgsb", "scipy.optimize.lbfgsb"], "excludes": [""]}

executables = [
    Executable('aterramento.py')
]

setup(name='aterramento',
      version='1.0',
      description='Felipe Bandeira',
      executables=executables,
      options = {"build_exe": build_exe_options}
      )
