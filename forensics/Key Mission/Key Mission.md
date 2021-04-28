```bash
tshark -r ./usb.pcap -Y 'usb.capdata && usb.data_len == 8' -T fields -e usb.capdata > usbPcapData
```

https://github.com/TeamRocketIst/ctf-usb-keyboard-parser/blob/master/usbkeyboard.py

Remove the `int(data.split(':')[3], 16) > 0` limitation

```bash
python3 usbkeyboard.py usbPcapData
```

CHTB{a_plac3_fAr_fAr_awway_ffr0m_eearth}
