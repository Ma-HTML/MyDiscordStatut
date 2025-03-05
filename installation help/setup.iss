[Setup]
; Informations générales sur l'installeur
AppName=MyDiscordStatut
AppVersion=1.0
DefaultDirName={pf}\MyDiscordStatut
DefaultGroupName=MyDiscordStatut
OutputDir=C:\Users\slemaire\Downloads\Setup
OutputBaseFilename=MyDiscordStatutInstaller
Compression=lzma
SolidCompression=yes

[Files]
; Fichiers à inclure dans l'installeur
Source: "C:\Users\slemaire\Downloads\Max\MyDiscordStatut\MyDiscordStatut.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\slemaire\Downloads\Max\MyDiscordStatut\files\app.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Créer un raccourci dans le menu démarrer
Name: "{group}\MyDiscordStatut"; Filename: "{app}\MyDiscordStatut.exe"
; Créer un raccourci sur le bureau
Name: "{commondesktop}\MyDiscordStatut"; Filename: "{app}\MyDiscordStatut.exe"

[Run]
; Optionnel : lancer l'application après installation
Filename: "{app}\MyDiscordStatut.exe"; Description: "Lancer MyDiscordStatut"; Flags: nowait postinstall skipifsilent
