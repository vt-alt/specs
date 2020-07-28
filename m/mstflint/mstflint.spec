%global commit      45e11fb8aded640515312c3124e21608876fb0ab
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%def_enable dc
%def_disable fw_mgr
%def_enable xml2
%def_enable cs
%def_enable inband
%def_enable openssl

Name: mstflint
Version: 4.14.0
Release: alt1

Summary: Mellanox firmware burning application
License: GPL/BSD
Url: http://openib.org/

Group: System/Base
# VCS-git: https://github.com/Mellanox/mstflint.git
Source: %name-%version.tar
Patch: %name-%version.patch
BuildRequires(pre): rpm-build-python3
BuildRequires: autoconf-archive
BuildRequires: gcc-c++
%{?_enable_dc:BuildRequires: zlib-devel}
%{?_enable_fw_mgr:BuildRequires: libcurl-devel liblzma-devel zlib-devel boost-devel}
%{?_enable_xml2:BuildRequires: libxml2-devel}
%{?_enable_inband:BuildRequires: rdma-core-devel}
%{?_enable_cs:BuildRequires: libssl-devel}
%{?_enable_openssl:BuildRequires: libssl-devel}
BuildRequires: libmuparser-devel libsqlite3-devel
AutoReq: yes, nopython
%add_python_compile_exclude %_libdir/%name/python_tools
%add_python3_compile_exclude %_libdir/%name/python_tools
%add_python3_path %_libdir/%name/python_tools


%description
This package contains a tool for burning updated firmware on to
Mellanox manufactured InfiniBand adapters.

%prep
%setup -q
%patch -p1

%build
mkdir config
echo "#define TOOLS_GIT_SHA \"%shortcommit\"" > common/gitversion.h

%autoreconf
%configure \
    %{subst_enable dc} \
    %{?_enable_fw_mgr:--enable-fw-mgr} \
    %{subst_enable xml2} \
    %{subst_enable inband} \
    %{subst_enable cs} \
    %{subst_enable openssl} \
    MSTFLINT_VERSION_STR="%name %version-%release"

%make_build

%install
%makeinstall_std
rm -rf %buildroot%_includedir

%files
%_bindir/*
%_datadir/%name
%dir %_libdir/%name
%_libdir/%name/python_tools
%_man1dir/*

%changelog
* Sun Apr 12 2020 Alexey Shabalin <shaba@altlinux.org> 4.14.0-alt1
- 4.14.0-1

* Fri Oct 18 2019 Alexey Shabalin <shaba@altlinux.org> 4.13.1-alt1
- v4.13.1-1

* Mon Feb 11 2019 Alexey Shabalin <shaba@altlinux.org> 4.11.0-alt1
- 4.11.0-2

* Wed Oct 31 2018 Alexey Shabalin <shaba@altlinux.org> 4.10.0-alt1
- v4.10.0-3

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.4-alt2.qa1
- NMU: rebuilt for debuginfo.

* Tue Aug 17 2010 Andriy Stepanov <stanv@altlinux.ru> 1.4-alt2
- New version (OFED 1.5.1)

* Tue Dec 08 2009 Stanislav Ievlev <inger@altlinux.org> 1.4-alt1
- Initial build

