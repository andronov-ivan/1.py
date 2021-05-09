[app]

# (str) Title of your application
title = For1

# (str) Package name
package.name = For1

# (str) Package domain (needed for android/ios packaging)
package.domain = org.wiseplat

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
#source.include_exts = py,png,jpg,kv,atlas,po,mo

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (str) Application version (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.0.0

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = all

osx.python_version = 3.9.5

osx.kivy_version = 2.0.0

