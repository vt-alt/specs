Name: dnstracer
Version: 1.9
Release: alt1.qa1.M90P.1

Summary: A tool to trace DNS queries
License: BSD
Group: Networking/Other
Url: http://www.mavetju.org/unix/general.php

Packager: Evgenii Terechkov <evg@altlinux.ru>

Source: http://www.mavetju.org/download/dnstracer-%version.tar.gz

# Patch from Gentoo
Patch1: dnstracer-1.9-argv0.patch

%description
dnstracer determines where a given Domain Name Server (DNS) gets its
information from, and follows the chain of DNS servers back to the
servers which know the data.

%prep
%setup
%patch1 -p1

%build
%configure
%make

%install
%makeinstall

%files
%doc CHANGES CONTACT LICENSE README
%doc %_man8dir/*
%_bindir/*

%changelog
* Thu Dec 17 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9-alt1.qa1.M90P.1
- Applied security patch from Gentoo (Fixes: CVE-2017-9430).

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.9-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Sep  9 2008 Terechkov Evgenii <evg@altlinux.ru> 1.9-alt1
- 1.9

* Fri Dec 03 2004 Andrei Bulava <abulava@altlinux.ru> 1.8-alt1
- initial build for ALT Linux; based on specfile by Dag Wieers

