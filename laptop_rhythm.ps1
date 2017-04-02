# Windows Powershell Script
# > ...laptop_rhythm.ps1

# event file Winlogon latest 100 to CSV
Get-EventLog -logname system -newest 100 -instanceid 7001, 7002 | `
Export-CSV -encoding UTF8 -path $PSScriptRoot\static\rhythm.csv

# virtualenv activate
. $PSScriptRoot\_rhythm\Scripts\activate.ps1

# module running
python $PSScriptRoot\laptop_rhythm.py