(English|[한글](./README_KO.md))
# RJConverter
![GitHub](https://img.shields.io/github/license/hankail05/RJConverter)
[![Build Status](https://travis-ci.com/hankail05/RJConverter.svg?branch=master)](https://travis-ci.com/hankail05/RJConverter)
[![codecov](https://codecov.io/gh/hankail05/RJConverter/branch/master/graph/badge.svg)](https://codecov.io/gh/hankail05/RJConverter)

RJConverter is a script converts name of directories with RJ code (ex. RJ171695) to its name.

## Requirements
RJConverter requires [mir.dlsite](https://github.com/darkfeline/mir.dlsite).
After cloning source code, type
```
pip install mir.dlsite
```
Binary file includes the requirement.

## Download
Binary files will be provieded soon™.

## Usage
```
python src/converter.py path/to/convert
```
For recursive conversion,
```
python src/converter.py -r path/to/convert
```

## License
This script is under MIT License.

## Special Thanks
[darkfeline](https://github.com/darkfeline/) for [great dlsite API](https://github.com/darkfeline/mir.dlsite/)
