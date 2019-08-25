%define unicodedir %_datadir/unicode
%define emojidir %unicodedir/emoji

Name: unicode-emoji
Version: 12.0
Release: alt1

Summary: Unicode Emoji Data Files
Group: Development/Other
License: MIT
Url: https://www.unicode.org/Public/emoji

Source: %url/%version/ReadMe.txt
Source1: %url/%version/emoji-data.txt
Source2: %url/%version/emoji-sequences.txt
Source3: %url/%version/emoji-test.txt
Source4: %url/%version/emoji-variation-sequences.txt
Source5: %url/%version/emoji-zwj-sequences.txt

# http://www.unicode.org/terms_of_use.html referenced in ReadMe.txt redirects to:
Source6: http://www.unicode.org/copyright.html

BuildArch: noarch

%description
Unicode Emoji Data Files are the machine-readable
emoji data files associated with
http://www.unicode.org/reports/tr51/index.html

%prep
%setup -cT

%install
mkdir -p %buildroot%emojidir
cp -a %_sourcedir/emoji-*.txt %buildroot%emojidir
cp -a %_sourcedir/{copyright.html,ReadMe.txt} .

%files
%emojidir/
%doc copyright.html ReadMe.txt

%changelog
* Thu Aug 22 2019 Yuri N. Sedunov <aris@altlinux.org> 12.0-alt1
- first build for sisyphus


