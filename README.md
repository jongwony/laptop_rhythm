# Laptop rhythm

Trace Laptop Logon, Logoff, Hibernation, Sleep time.

Draw rhythm chart & Battery report.

## Windows only

### How Works:

Filtering event log file(`.evt`)

### Package

```
virtualenv
flask
pandas
d3.js
```

## Usage

You must ensure [Get-ExecutionPolicy](//technet.microsoft.com/ko-KR/library/hh847748.aspx) is not Restricted. We suggest using `Bypass` to bypass the policy to get things installed or AllSigned for quite a bit more security.

### Set policy

```powershell
Set-ExecutionPolicy -ExecutionPolicy BYPASS
```

### Virtualenv

Python 3.6, pip 9.0.1

virtualenv name: `_rhythm`

```
pip install virtualenv

virtualenv _rhythm
```

Install `flask`, `pandas` package.

```
pip install pandas, flask
```

### Run script

```
.\laptop_rhythm.ps1
```

## Reference

- [D3.js 배우는 방법](//mobicon.tistory.com/275)  
- [D3 Gallery](//github.com/d3/d3/wiki/Gallery)  
- [Flask templates](//flask.pocoo.org/docs/0.12/templating/)  
- [Pandas dataframe](//pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html)  
- [Pandas dataframe binary operation](//pandas.pydata.org/pandas-docs/stable/api.html#id4)  
- [Pandas dataframe query](//pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.query.html)

## TODO List

- `static/battery_rhythm.xml` file analyze  
- Specify history time(today yet)