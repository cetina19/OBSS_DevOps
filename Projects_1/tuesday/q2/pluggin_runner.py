import pkgutil, fire, importlib

for finder,name,ispkg in pkgutil.iter_modules(path=None, prefix=''):
    if(name.startswith('plugin_sample')):
        func = importlib.import_module(name=name)
        func.run()