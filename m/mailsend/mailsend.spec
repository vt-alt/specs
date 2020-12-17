Name:		mailsend
Version:	1.20b2
Release:	alt0.p9.1
Summary:	Command line tool to send email via SMTP protocol
Url:		https://github.com/muquit/mailsend
Group:		Networking/Mail
License:	BSD
Source0:	%name-%version.tar.gz

BuildRequires: libssl-devel

%description
%name is a simple command line program to send mail via SMTP protocol

%prep
%setup

%build
%configure --with-openssl=/usr
%make_build

%install
%makeinstall

%files
%doc doc/*.mediawiki
%_bindir/*
%_man1dir/*

%changelog
* Fri Dec 11 2020 Motsyo Gennadi <drool@altlinux.ru> 1.20b2-alt0.p9.1
- build for p9

* Wed Dec 09 2020 Motsyo Gennadi <drool@altlinux.ru> 1.20b2-alt1
- initial build
