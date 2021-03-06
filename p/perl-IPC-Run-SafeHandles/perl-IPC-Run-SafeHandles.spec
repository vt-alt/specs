#
#   - IPC::Run::SafeHandles -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       IPC::Run::SafeHandles
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module IPC-Run-SafeHandles
%define m_distro IPC-Run-SafeHandles
%define m_name IPC::Run::SafeHandles
%define m_author_id unknown
%define _enable_test 1

Name: perl-IPC-Run-SafeHandles
Version: 0.04
Release: alt1

Summary: IPC-Run-SafeHandles - Perl module

License: Artistic
Group: Development/Perl
Url: %CPAN %m_distro

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: http://www.cpan.org/authors/id/C/CL/CLKAO/IPC-Run-SafeHandles-%{version}.tar.gz

# Automatically added by buildreq on Sun Apr 13 2008
BuildRequires: perl-devel perl(List/MoreUtils.pm)

%description
IPC::Run and IPC::Run3 are both very upset when you try to use them under
environments where you have STDOUT and/or STDERR tied to something else,
such as under fastcgi.  The module adds safe-guarding code when you call
IPC::Run or IPC::Run3 under such environment to make sure it always works.
If you intend to release your code to work under normal envionrment as
well as under fastcgi, simply use this module after the IPC modules are
loaded in your code.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/IPC/Run/*

%changelog
* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Sun Dec 21 2008 Vitaly Lipatov <lav@altlinux.ru> 0.02-alt1
- new version 0.02 (with rpmrb script)
- fix directory ownership violation
- disable man packaging
- change packager

* Sun Apr 13 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.01-alt1
- first build for ALT Linux Sisyphus

