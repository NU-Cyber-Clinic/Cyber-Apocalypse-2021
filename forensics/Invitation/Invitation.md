Extract the vba macro from the docm file using oletools olevbs
which we get invite.vb from
running that through visual studio gets us invite.ps1.b64
and then base64 decode using `cat invite.ps1.b64 | base64 -d > invite.ps1` and then running that in powershell gets us invite.ps1.txt

pull out lines 1 and 7
```powershell
. ( $PshomE[4]+$pshoMe[30]+'x') ( [strinG]::join('' , ([REGeX]::MaTCHES( ")'x'+]31[DIlLeHs$+]1[DiLLehs$ (&| )43]RAhc[]GnIRTs[,'tXj'(eCALPER.)'$','wqi'(eCALPER.)';tX'+'jera_scodlam'+'{B'+'T'+'HCtXj '+'= p'+'gerwqi'(" ,'.' ,'R'+'iGHTtOl'+'eft' ) | FoREaCH-OBJecT {$_.VALUE} ))  )
```
```powershell
SEt ("G8"+"h")  (  " ) )63]Rahc[,'raZ'EcalPeR-  43]Rahc[,)05]Rahc[+87]Rahc[+94]Rahc[(  eCAlpERc-  )';2'+'N'+'1'+'}atem_we'+'n_eht'+'_2N1 = n'+'gerr'+'aZ'(( ( )''niOj-'x'+]3,1[)(GNirTSot.EcNereFeRpEsOBREv$ ( . "  ) ;-jOIn ( lS ("VAR"+"IaB"+"LE:g"+"8H")  ).VALue[ - 1.. - ( ( lS ("VAR"+"IaB"+"LE:g"+"8H")  ).VALue.LengtH)] | IeX 
```
then replace the iex with echos to get the raw output
```powershell
echo ( [strinG]::join('' , ([REGeX]::MaTCHES( ")'x'+]31[DIlLeHs$+]1[DiLLehs$ (&| )43]RAhc[]GnIRTs[,'tXj'(eCALPER.)'$','wqi'(eCALPER.)';tX'+'jera_scodlam'+'{B'+'T'+'HCtXj '+'= p'+'gerwqi'(" ,'.' ,'R'+'iGHTtOl'+'eft' ) | FoREaCH-OBJecT {$_.VALUE} ))  )

('iqwreg'+'p ='+' jXtCH'+'T'+'B{'+'maldocs_arej'+'Xt;').REPLACe('iqw','$').REPLACe('jXt',[sTRInG][chAR]34) |&( $sheLLiD[1]+$sHeLlID[13]+'x')

$regp = "CHTB{maldocs_are";
```
```powershell
SEt ("G8"+"h")  (  " ) )63]Rahc[,'raZ'EcalPeR-  43]Rahc[,)05]Rahc[+87]Rahc[+94]Rahc[(  eCAlpERc-  )';2'+'N'+'1'+'}atem_we'+'n_eht'+'_2N1 = n'+'gerr'+'aZ'(( ( )''niOj-'x'+]3,1[)(GNirTSot.EcNereFeRpEsOBREv$ ( . "  ) ;-jOIn ( lS ("VAR"+"IaB"+"LE:g"+"8H")  ).VALue[ - 1.. - ( ( lS ("VAR"+"IaB"+"LE:g"+"8H")  ).VALue.LengtH)] | echo 

( $vERBOsEpReFereNcE.toSTriNG()[1,3]+'x'-jOin'') ( (('Za'+'rreg'+'n = 1N2_'+'the_n'+'ew_meta}'+'1'+'N'+'2;')  -cREplACe  ([chaR]49+[chaR]78+[chaR]50),[chaR]34  -RePlacE'Zar',[chaR]36) )

$regn = "_the_new_meta}";
```

CHTB{maldocs_are_the_new_meta}
