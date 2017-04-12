# Windows Powershell Script
# > ...laptop_rhythm.ps1

# event file Winlogon latest 100 to CSV
Get-EventLog -logname system -newest 100 -instanceid 7001, 7002, 506, 507 | `
Export-CSV -encoding UTF8 -path "$PSScriptRoot\static\logon_rhythm.csv"

# Battery dump to CSV
powercfg /batteryreport /output "$PSScriptRoot\static\battery_rhythm.xml" /xml

# virtualenv activate
. $PSScriptRoot\_rhythm\Scripts\activate.ps1

# module running
python $PSScriptRoot\laptop_rhythm.py