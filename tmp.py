import pkgutil
import entities


mod=pkgutil.iter_modules(entities.__path__)
walk = pkgutil.walk_packages('entities')
print(dir(mod))
modules = []
for (_,m,_) in mod:
    modules.append(m)
print(modules)