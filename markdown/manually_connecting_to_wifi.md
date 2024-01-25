---
tags: [
  command prompt, cmd, shell, Wi-Fi, wifi
]
---

# Manually Connecting to WiFi Network via Command Prompt (CMD)

Used when encountering the error `windows cannot get the network settings from the router`

First open command prompt and use `netsh wlan show networks` to get a list of all available networks

```
C:\Users\...\folder>netsh wlan show networks

Interface name : Wi-Fi
There are 3 networks currently visible.

SSID 1 : WiFi-Name
    Network type            : Infrastructure
    Authentication          : WPA2-Personal
    Encryption              : CCMP

SSID 2 : WiFi-Name-5G
    Network type            : Infrastructure
    Authentication          : WPA2-Personal
    Encryption              : CCMP

SSID 3 : Optus_AC3BEB
    Network type            : Infrastructure
    Authentication          : WPA2-Personal
    Encryption              : CCMP
```

Then open a note editor and create an XML profile file eg. `C:\...\test.xml`, updating the {WiFi-Name} and {PASSWORD-OR-NUMBER} and then note the file path

```xml
<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{WiFi-Name}</name>
    <SSIDConfig>
        <SSID>
            <hex>576946692D3543393431315F455854</hex>
            <name>{WiFi-Name}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>manual</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{PASSWORD-OR-NUMBER}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>

```

Now go back to command prompt and use `netsh wlan add profile filename="C:\...\test.xml" interface="Wi-Fi" user=current`, using the filepath to the XML profile file you made

Then run `netsh wlan connect name="{WiFi-Name}"` with the correct WiFi-Name

After this you can delete the xml file as the connection data is now stored in the windows registry