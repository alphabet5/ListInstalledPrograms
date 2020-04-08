# ListInstalledPrograms

 Quick scripts to list / parse installed programs in a domain.


## Prerequisites.

ListInstalledPrograms.ps1 should be modified to skip any domain-joined computers/servers that you do not want to list the programs of.

winrm must be enabled on the target computers in the domain to run Invoke-Command.


## Usage

Run ListInstalledPrograms.ps1.

One example of parsing the output is located in 'ParseJsonOutput.py'. This takes the output json file from ListInstalledPrograms.ps1 and outputs a CSV with 'PSComputerName', 'DisplayName', 'DisplayVersion', and 'Publisher'.

This output is then modified by 'ConsolidateByProgram.py' to list computers by the specific version of software installed.
