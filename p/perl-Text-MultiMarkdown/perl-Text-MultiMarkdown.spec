#
#   - Text-MultiMarkdown -
#   This spec file was automatically generated by cpan2rpm [ver: 2.028]
#   (ALT Linux revision)
#   The following arguments were used:
#       Text::MultiMarkdown . --spec-only
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Text-MultiMarkdown
%define m_distro Text-MultiMarkdown
%define m_name Text-MultiMarkdown
%define m_author_id unknown
%define _enable_test 1

Name: perl-Text-MultiMarkdown
Version: 1.000035
Release: alt1

Summary: Convert MultiMarkdown syntax to (X)HTML

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: %m_distro-%version.tar

BuildRequires: perl-devel perl-Encode perl-Text-Markdown perl-Test-Exception perl-List-MoreUtils
BuildRequires: perl-Text-Diff perl-Test-Pod perl-Test-Pod-Coverage perl-Test-Spelling
BuildRequires: perl-HTML-Tidy perl(HTML/Entities.pm)

%description
Markdown is a text-to-HTML filter; it translates an easy-to-read /
easy-to-write structured text format into HTML. Markdown's text format
is most similar to that of plain text email, and supports features such
as headers, *emphasis*, code blocks, blockquotes, and links.

Markdown's syntax is designed not as a generic markup language, but
specifically to serve as a front-end to (X)HTML. You can use span-level
HTML tags anywhere in a Markdown document, and you can use block level
HTML tags (`<div>', `<table>' etc.). Note that by default
Markdown isn't interpreted in HTML block-level elements, unless you add
a `markdown=1"' attribute to the element. See the Text::Markdown manpage for
details.

This module implements the MultiMarkdown markdown syntax extensions from:

    http://fletcherpenney.net/multimarkdown/

%prep
%setup -n %m_distro-%version

%build
export TEST_POD=1
#export TEST_SPELLING=1 # it will not pass
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/MultiMarkdown.pl
%_man1dir/*
%perl_vendor_privlib/Text/*

%changelog
* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.000035-alt1
- automated CPAN update

* Thu Dec 15 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1.000034-alt1
- Initial build for ALT Linux Sisyphus.

