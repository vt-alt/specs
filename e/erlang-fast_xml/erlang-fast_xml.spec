%define _unpackaged_files_terminate_build 1

%global realname fast_xml

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.1.41
Release: alt1
Summary: Fast Expat based Erlang XML parsing library
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/fast_xml

# https://github.com/processone/fast_xml.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-p1_utils
BuildRequires: libexpat-devel

%description
Fast Expat based Erlang XML parsing and manipulation library,
with a strong focus on XML stream parsing from network.

It supports:
    Full XML structure parsing: Suitable for small but complete XML chunks.
    XML stream parsing: Suitable for large XML document,
    or infinite network XML stream like XMPP.

This module can parse files much faster than built-in module xmerl.
Depending on file complexity and size fxml_stream:parse_element/1
can be 8-18 times faster than calling xmerl_scan:string/2.

This application was previously called p1_xml and was renamed
after major optimisations to put emphasis on the fact it is damn fast.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE.*
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Wed Jul 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.41-alt1
- Updated to upstream version 1.1.41.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.39-alt1
- Updated to upstream version 1.1.39.

* Wed Jun 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.36-alt1
- Updated to upstream version 1.1.36.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.35-alt1
- Updated to upstream version 1.1.35.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.34-alt1
- Updated to upstream version 1.1.34.

* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.29-alt1
- Initial build for ALT.
