
Name: http-parser
Version: 2.9.2
Release: alt1
Summary: HTTP request/response parser for C

Group: System/Libraries
License: MIT
Url: http://github.com/joyent/http-parser
Source: %name-%version.tar

%description
This is a parser for HTTP messages written in C. It parses both requests and
responses. The parser is designed to be used in performance HTTP applications.
It does not make any syscalls nor allocations, it does not buffer data, it can
be interrupted at anytime. Depending on your architecture, it only requires
about 40 bytes of data per message stream (in a web server that is per
connection).

%package -n lib%name
Summary: HTTP request/response parser for C
Group: System/Libraries

%description -n lib%name
This is a parser for HTTP messages written in C. It parses both requests and
responses. The parser is designed to be used in performance HTTP applications.
It does not make any syscalls nor allocations, it does not buffer data, it can
be interrupted at anytime. Depending on your architecture, it only requires
about 40 bytes of data per message stream (in a web server that is per
connection).

%package -n lib%name-devel
Summary: HTTP request/response parser for C
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development headers and libraries for http-parser.

%prep
%setup -q

%build
%make library

%install
%makeinstall_std PREFIX=%_prefix LIBDIR=%_libdir 

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS README.md LICENSE-MIT

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Mon Aug 19 2019 Alexey Shabalin <shaba@altlinux.org> 2.9.2-alt1
- new version 2.9.2

* Wed Jan 16 2019 Alexey Shabalin <shaba@altlinux.org> 2.9.0-alt1
- 2.9.0

* Thu Apr 12 2018 Alexey Shabalin <shaba@altlinux.ru> 2.8.1-alt1%ubt
- 2.8.1

* Tue Feb 27 2018 Alexey Shabalin <shaba@altlinux.ru> 2.8.0-alt1%ubt
- 2.8.0

* Fri Apr 07 2017 Evgeny Sinelnikov <sin@altlinux.ru> 2.7.0-alt1%ubt
- Enable unified build tag aka ubt macros

* Fri Jul 08 2016 Alexey Shabalin <shaba@altlinux.ru> 2.7.0-alt1
- Initial packaging

