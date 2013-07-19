#!/usr/bin/perl
print "Content-Type: text/html\n\n"; 
use CGI qw(:standard); 
my $defaultmail = "rmagahiz\@compuserve.com";
my %recmail = (
	       "Main" => "rich\@www.magahiz.com",
               "Aux1" => "rmagahiz\@compuserve.com",
	       "Aux2" => "rmagahiz\@yahoo.com",
	       );
$session = param("session");
$Name = param("Name"); 
$Email = param("Email");
$TheBody = param("TheBody");

#$Recipient =param("Officer");
$Recipient =param("Account");
#print "Name was $Name, Email was $Email.\n" if ($DEBUG);
print "Body was $TheBody<br>\n" if ($DEBUG);
#$Salutation = (($Recipient eq "WEB") ? 'Dear ' : 'Worthy ') . $title{$Recipient} . ',';
$Salutation = '';
$Emailrec = $defaultmail;
if (exists $recmail{$Recipient}) {
    $Emailrec = $recmail{$Recipient}
};

open (SENDMAIL, "|/usr/sbin/sendmail -oi -t -odq") or die "Can't fork for sendmail: $!\n";
print SENDMAIL<<"EOF";
From: Email form <rich\@www.magahiz.com>
To: $title{$Recipient} <$Emailrec>, Email form <rich\@www.magahiz.com>
Reply-To: $Name <$Email>
Subject: Email from $Name <$Email>

$Salutation

$TheBody

End of comment
EOF
close(SENDMAIL);

print "<html><head><title>Thank you</title></head>\n<body><br>";
print "Thank you for sending your email\n<br>\n";
print "Click <a href=\"http://www.magahiz.com:8080/frabjous/\">here</a> to return to my  homepage.\n";
print "<hr>\n </body> \n </html>\n";


1;
