#
# spec file for PCL reference assemblies
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Xamarin, Inc.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           referenceassemblies-pcl
Version:        2014.04.14
Release:	alt5
Url:            http://go-mono.org/
# https://github.com/mono/linux-packaging-referenceassemblies-pcl/
Source0:	%name-%version.tar
Source1:	EULA.rtf
Summary:        PCL reference assemblies for .NET
License:        EULA
Group:          Development/Other
BuildArch:      noarch

BuildRequires(Pre): rpm-build-mono >= 2.0.0
BuildRequires: mono-devel >= 5.0.0.0
BuildRequires: /proc

# ALT Bug 39254
AutoReq: no
AutoProv: no

%description
PCL Reference Assemblies are used for compiling code which
works on multiple .NET framework targets

%prep
%setup

%build
cp %SOURCE1 .

%install
mkdir -p %buildroot%_monodir/xbuild-frameworks/.NETPortable/
cp -a v4.0  %buildroot%_monodir/xbuild-frameworks/.NETPortable/
cp -a v4.5  %buildroot%_monodir/xbuild-frameworks/.NETPortable/
cp -a v4.6  %buildroot%_monodir/xbuild-frameworks/.NETPortable/

%files
%_monodir/xbuild-frameworks/.NETPortable
%doc EULA.rtf

%changelog
* Wed Nov 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2014.04.14-alt5
- Disabled AutoReq and AutoProv (ALT #39254).

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2014.04.14-alt4
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 2014.04.14-alt3
- NMU: remove %ubt from release

* Fri Sep 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2014.04.14-alt2%ubt
- Rebuilt with support of %%ubt macro.

* Wed Jul 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2014.04.14-alt1
- Initial build for ALT
