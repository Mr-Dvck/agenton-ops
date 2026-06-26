$WshShell = New-Object -ComObject WScript.Shell
$DesktopPath = [System.IO.Path]::Combine($env:USERPROFILE, "Desktop")
$ShortcutFile = Join-Path $DesktopPath "Money Machine.lnk"

Write-Host "Creating shortcut at: $ShortcutFile"
$Shortcut = $WshShell.CreateShortcut($ShortcutFile)
$Shortcut.TargetPath = "C:\BC RESEARCH\AI_FACTORY\AgentOn\launch_dashboard.bat"
$Shortcut.WorkingDirectory = "C:\BC RESEARCH\AI_FACTORY\AgentOn"
$Shortcut.IconLocation = "C:\BC RESEARCH\AI_FACTORY\AgentOn\dashboard\money_bag.ico, 0"
$Shortcut.Save()
Write-Host "Successfully created shortcut!"
