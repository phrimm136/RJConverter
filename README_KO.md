([English](./README.md)|한글)
# RJConverter

RJConverter 는 폴더 내의 RJ코드를 찾아 그 폴더의 이름을 해당하는 이름으로 변환하는 스크립트입니다.

## Requirements

RJConverter 는 실행을 위해 [mir.dlsite](https://github.com/darkfeline/mir.dlsite)가 필요합니다.
코드를 클론 한 뒤,
```
pip install mir.dlsite
```
를 입력하십시오.
실행파일을 다운로드 했을 시 이 과정이 필요하지 않습니다.

## Download

실행파일은 곧™ 추가될 것입니다.

## Usage

cmd 또는 powershell을 실행 한 뒤, 클론 한 폴더로 이동하여 다음을 입력하십시오.
```
python src/converter.py path/to/convert
```
하위 폴더도 변환하려면 다름을 입력하십시오.
```
python src/converter.py -r path/to/convert
```
`path/to/convert` 는 변환 대상 경로입니다.
dlsite는 https 차단 대상이므로, 우회를 한 뒤 사용하십시오.
