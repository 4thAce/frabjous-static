#!/usr/bin/perl
# goopoetry.cgi
# Generates a mean word salad.
# goopoetry.cgi is called as a CGI with form input
# Your google API developer's key
my $google_key = '1gv1N/5QFHL3tjcUm6ufMm0FBuG9mW24';

# Location of the GoogleSearch WSDL file
my $google_wdsl = ".GoogleSearch.wsdl";

# Number of lines per poem
my $numlines = 10;

# Number of words per line
my $numwords = 6;

use strict;

use SOAP::Lite;
use CGI qw/:standard/;

my $flavors = {
  'Hippie' => ['wow', 'groovy man!', 'far out!', 'Right on!',
    'funky', 'outta sight', 'Like,', 'peace out!',
    'munchies'],
  'Beatnik' => ['daddy-o', 'long gone', 'hepcat', ',jazzy',
    'cool', 'hip', 'cool', 'jazzman', 'zoot'],
  'Shakespeare' => ['thee', 'hark!', 'forsooth,', 'alas!', 'sirrah',
    'hither', 'hence'],
  'Swedish Chef' => ['bork bork bork!', 'hmdordeborkbork', 'BORK!',
    'hrm de hr', 'bork?', 'hur chikee chikee'],
  'Default' => ['...', '!', '(?)', '---']
};

print
  header(),
  start_html("GooPoetry"),
  h1("GooPoetry"),
  start_form(-method=>'Get'),
  'Query: ', textfield(-name=>'query'),
  br(),
  'Flavor: ', popup_menu(
    -name=>'flavor', -values=>[keys %$flavors], -default=>'Default'
  ),
  br(),
  submit(-name=>'submit', -value=>'Toss that Word Salad'),
  end_form(), p();

if (param('flavor')){
  my $google_search = SOAP::Lite->service("file:$google_wdsl");

  #Create an array for the random words
  my @words;
  # Mix in the flavored words
  push @words, @{$flavors->{param('flavor')}};

  # Query Google
  my $results = $google_search ->
    doGoogleSEarch(
      $google_key, param('query'), 0, 10, "false", "", "false",
      "", "latin1", "latin1"
    );

  # Glean and clean title words from results
  foreach my $result (@{$results->{'resultElements'}}) {
    $result->{title} =~ s!\n!!g;  # drop spurious newlines
    $result->{title} =~ s!!!g; # Drop all HTML tags
    push @words, split /\s+/, $result->{title};
  }

  for (my $l = 0; $l <=$numlines; $l++) {
    # Randomly decide the number of words in the setntence
    for (my $w = 0; $w <= int(rand($numwords))+3; $w++) {
      print lc $words[rand(scalar @words)] . ' ';
    }
    print "";
  }
}

print end_html();
