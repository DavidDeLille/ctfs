<!DOCTYPE html
	PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US">
<head>
<title>Next Generation Avatar Creation</title>
<link rel="stylesheet" type="text/css" href="/css.css" />
<script src="/js.js" type="text/javascript"></script>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
</head>
<body>
<div><h1>Avatar Generator</h1> <p>Are you sick and tired of stupid avatars on websites? Are you ready for the next generation of customizable, yet HAND MADE avatars? Then you have come to the right place!</p> 
<video><source src='https://zippy.gfycat.com/DesertedEasygoingArabianwildcat.webm'></source></video>
<canvas></canvas> 
<form method="poop" action="#" enctype="multipart/form-data" onchange="loadImage()" id="frm"> <br /> 
<table><tr><td><b>Head</b></td> 
<td><input name="Head" max="4" type="range" min="1" /></td></tr> <tr>
<td><b>Hair</b></td> <td><input name="Hair" max="2" type="range" min="0" /></td></tr> <tr>
<td><b>Nose</b></td> <td><input name="Nose" max="3" type="range" min="1" /></td></tr> <tr>
<td><b>Mouth</b></td> <td><input type="range" min="1" max="3" name="Mouth" /></td></tr> <tr>
<td><b>Eyes</b></td> <td><input type="range" min="1" max="3" name="Eyes" /></td></tr>
</table> </form></div>
<!-- DEBUG SOURCE
#!/usr/bin/perl

use CGI;

$q = new CGI;
if (defined($q->param('Head'))) {
  print $q->header(-type=>'image/bmp');
  open(HEAD,"head".$q->param('Head'));
  open(HAIR,"hair".$q->param('Hair'));
  open(NOSE,"nose".$q->param('Nose'));
  open(MOUTH,"mouth".$q->param('Mouth'));
  open(EYES,"eyes".$q->param('Eyes'));

  while (read(HEAD,$headb,1)) {
    read(HAIR,$hairb,1);
    read(NOSE,$noseb,1);
    read(MOUTH,$mouthb,1);
    read(EYES,$eyesb,1);
    print (chr (ord($headb)&ord($hairb)&ord($noseb)&ord($mouthb)&ord($eyesb)));
  }
}
else {
  print $q->header;

  print $q->start_html(-title=>"Next Generation Avatar Creation",-script=>{'src'=>'/js.js'},-style=>{'src'=>'/css.css'});
  print $q->div(
   $q->h1("Avatar Generator"),
   $q->p("Are you sick and tired of stupid avatars on websites? Are you ready for the next generation of customizable, yet HAND MADE avatars? Then you have come to the right place!"),
   "<video><source src='https://zippy.gfycat.com/DesertedEasygoingArabianwildcat.webm'></source></video><canvas></canvas>",
   $q->start_form(-id=>"frm",-method=>"POOP",-action=>"#",-onchange=>"loadImage()"),
   $q->br(),
   $q->table(
    $q->Tr($q->td([$q->b("Head"),$q->input({-name=>"Head",-type=>'range',-min=>1,-max=>4})])),
    $q->Tr($q->td([$q->b("Hair"),$q->input({-name=>"Hair",-type=>'range',-min=>0,-max=>2})])),
    $q->Tr($q->td([$q->b("Nose"),$q->input({-name=>"Nose",-type=>'range',-min=>1,-max=>3})])),
    $q->Tr($q->td([$q->b("Mouth"),$q->input({-name=>"Mouth",-type=>'range',-min=>1,-max=>3})])),
    $q->Tr($q->td([$q->b("Eyes"),$q->input({-name=>"Eyes",-type=>'range',-min=>1,-max=>3})]))
   ),
   $q->end_form
  );
  open SELF, "index.cgi";
  print $q->comment("DEBUG SOURCE\n".do { local $/; <SELF> });
  print $q->end_html();
}
 -->
</body>
</html>