[Setup]
; Informations g�n�rales sur l'installeur
AppName=MyDiscordStatut
AppVersion=1.0
DefaultDirName={pf}\MyDiscordStatut
DefaultGroupName=MyDiscordStatut
OutputDir=C:\Users\slemaire\Downloads\Setup
OutputBaseFilename=MyDiscordStatutInstaller
Compression=lzma
SolidCompression=yes

[Files]
; Fichiers � inclure dans l'installeur
Source: "C:\Users\slemaire\Downloads\Max\MyDiscordStatut\MyDiscordStatut.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\slemaire\Downloads\Max\MyDiscordStatut\files\app.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Cr�er un raccourci dans le menu d�marrer
Name: "{group}\MyDiscordStatut"; Filename: "{app}\MyDiscordStatut.exe"
; Cr�er un raccourci sur le bureau
Name: "{commondesktop}\MyDiscordStatut"; Filename: "{app}\MyDiscordStatut.exe"

[Run]
; Optionnel : lancer l'application apr�s installation
Filename: "{app}\MyDiscordStatut.exe"; Description: "Lancer MyDiscordStatut"; Flags: nowait postinstall skipifsilent
