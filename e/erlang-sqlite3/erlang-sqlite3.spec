%define _unpackaged_files_terminate_build 1

%define realname sqlite3

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.1.11
Release: alt1
Summary: Sqlite gen_server port for Erlang. Creates, reads and writes to sqlite database.
Group: Development/Erlang
License: ErlPL-1.1
Url: https://github.com/processone/erlang-sqlite3

# https://github.com/processone/erlang-sqlite3.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: libsqlite3-devel

%description
This library allows you to work with SQLite3 databases from Erlang.

%prep
%setup
rm -rf sqlite3_amalgamation

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit

%files
%doc LICENSE
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Wed Feb 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.11-alt1
- Updated to upstream version 1.1.11.

* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.9-alt1
- Updated to upstream version 1.1.9.

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.8-alt1
- Updated to upstream version 1.1.8.

* Tue Mar 31 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.6-alt4
- Fixed build with rebar2.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt2
- NMU: remove %%ubt from release

* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.6-alt1
- Initial build for ALT.
