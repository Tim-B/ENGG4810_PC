from distutils.core import setup
import py2exe
import matplotlib
import os

includes = ['_pyo', 'pyo']

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
    if os.path.basename(pathname).lower() in ("libsndfile-1.dll", "fftpack_lite.pyd"):
        return 0
    return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL

setup(
    options={
        "py2exe": {
            'includes' : includes,
        }
    },
    data_files=matplotlib.get_py2exe_datafiles(),
    windows=['engg4810.py']
)