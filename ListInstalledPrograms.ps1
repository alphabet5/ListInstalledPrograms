 # Check if RSAT-AD-Powershell is installed
$ad_powershell = Get-WindowsFeature -Name RSAT-AD-Powershell
If (-NOT $ad_powershell.Installed) {
    Add-WindowsFeature RSAT-AD-PowerShell
    }
# Fetch the installed programs and features for all computers in the domain
$installed_features = ForEach ($computer in (Get-ADComputer -Filter * | Where-Object {$_.name -ne "SERVER-TO-SKIP"})) {
    Invoke-Command -ComputerName $computer.name -ScriptBlock {
        [PSCustomObject][Ordered]@{
            computer_name = $Using:computer
            installed_features = Get-ChildItem -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall | Get-ItemProperty
            installed_features2 = Get-ChildItem -Path HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall | Get-ItemProperty
            }
        }
    }
$installed_features | ConvertTo-Json -Compress -Depth 4 | Out-File "installed_features.json"
