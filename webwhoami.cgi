#!/usr/bin/perl
# webwhoami - show web users id
print "Content-Type: text/plain\n\n";
print "Running as ", scalar getpwuid($>),"\n";
