rule Comprehensive_Malware_Detection
{
    meta:
        author = "RSG"
        description = "Detects Trojans, Beacons, Exploits, and Malware while ignoring DFIR tools."
        version = "1.0"
        date = "2025-03-05"
        reference = "https://attack.mitre.org/"

    strings:
        // Trojan & Exploit Strings
        $trojan1 = "trojan.exe" nocase
        $trojan2 = "malware_payload" nocase
        $trojan3 = "backdoor_connection" nocase
        $exploit1 = "heap spray" nocase
        $exploit2 = "ROP chain" nocase
        $exploit3 = "shellcode execution" nocase

        // C2 Beacons (Cobalt Strike, Metasploit, Sliver, Empire)
        $c2_1 = "Malleable C2 Profile" nocase
        $c2_2 = "GET /ajax.php?m=beacon" nocase
        $c2_3 = "X-Forwarded-For: 127.0.0.1" nocase
        $c2_4 = "Meterpreter" nocase
        $c2_5 = "Sliver C2" nocase
        $c2_6 = "EmpireAgent" nocase

        // Known C2 Mutexes
        $mutex1 = "Global\\MZNUZ7NN1MTQAATLP2MRS1G" nocase
        $mutex2 = "Global\\COMSPEC" nocase

        // Ignored DFIR Tools (Axiom, Cellebrite, Autopsy, Passware)
        $dfir1 = "MagnetAxiom.exe" nocase
        $dfir2 = "cellebrite.ufed" nocase
        $dfir3 = "autopsy.exe" nocase
        $dfir4 = "passwarekit.exe" nocase

    condition:
        (4 of ($trojan*) or 3 of ($exploit*) or 3 of ($c2_*) or any of ($mutex*)) and not any of ($dfir*)
}
