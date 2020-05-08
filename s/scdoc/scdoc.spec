Name: scdoc
Version: 1.10.1
Release: alt1
License: MIT
Summary: Tool for generating roff manual pages
URL: https://git.sr.ht/~sircmpwn/scdoc
Group: Development/Other

Source: %name-%version.tar

BuildRequires: gcc

%description
scdoc is a tool designed to make the process of writing man pages more
friendly. It reads scdoc syntax from stdin and writes roff to stdout, suitable
for reading with man.

%prep
%setup

# Disable static linking
sed -i '/-static/d' Makefile

# Use INSTALL provided by the make_install macro
sed -i 's/\tinstall/\t$(INSTALL)/g' Makefile

%build
%make_build PREFIX="%_prefix"

%install
%make_install install \
	PREFIX="%buildroot%_prefix" \
	PCDIR="%buildroot%_pkgconfigdir"

%check
%make check

%files
%_bindir/%name
%_man1dir/*
%_man5dir/*
# Not shipped in a -devel package since scdoc is a development tool not
# installed in a user runtime.
%_pkgconfigdir/%name.pc

%changelog
* Fri Mar 27 2020 Alexey Gladkov <legion@altlinux.ru> 1.10.1-alt1
- New version (1.10.1)

* Wed May 22 2019 Alexey Gladkov <legion@altlinux.ru> 1.9.4-alt1
- Initial build.
