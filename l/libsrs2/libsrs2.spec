Summary: SRS email address rewriting engine
Name: libsrs2
Version: 1.0.18
Release: alt1
License: GPL-2.0-only-or-BSD-3-Clause

Group: System/Libraries

URL: http://www.libsrs2.org/
Source: http://www.libsrs2.org/srs/%{name}-%{version}.tar

BuildRequires: gcc-c++ chrpath

%description
libsrs2 is the next generation Sender Rewriting Scheme (SRS)
library. SPF verifies that the Sender address of a mail matches
(according to some policy) the client IP address which submits
the mail. When a mail is forwarded, the sender address must be
rewritten to comply with SPF policy. The SRS provides a standard
for this rewriting which is not vulnerable to attacks by spammers.

%package devel
Summary: Development files for %name
Group: System/Libraries

%description devel
This package contains the development files for %name.

%package -n srs2
Summary: Sender Rewriting Scheme - command/daemon interface
Group: Networking/Mail
Requires: %name = %version-%release
Conflicts: libsrs_alt

%description -n srs2
Sender Rewriting Scheme - command/daemon interface

%prep
%setup -q

%configure

%build
%make

%install
%makeinstall

rm -f $RPM_BUILD_ROOT%_libdir/libsrs2.a
chrpath -d $RPM_BUILD_ROOT%_bindir/srs

%files
%doc ChangeLog INSTALL README NEWS AUTHORS COPYING LICENSE.*
%_libdir/libsrs2.so.*

%files -n srs2
%_bindir/srs

%files devel
%_includedir/srs2.h
%_libdir/libsrs2.so

%changelog
* Sun Jun 28 2020 Sergey Y. Afonin <asy@altlinux.org> 1.0.18-alt1
- initial build for ALT Linux
