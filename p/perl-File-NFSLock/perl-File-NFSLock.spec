%define _unpackaged_files_terminate_build 1
#
#   - File::NFSLock -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       -U File::NFSLock
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module File-NFSLock
%define m_distro File-NFSLock
%define m_name File::NFSLock
%define m_author_id unknown
%define _disable_test 1

Name: perl-File-NFSLock
Version: 1.29
Release: alt1

Summary: File-NFSLock - perl module to do NFS (or not) locking

Group: Development/Perl
License: Artistic
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/B/BB/BBB/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Mon Jun 06 2005
BuildRequires: perl-devel

%description
Program based of concept of hard linking of files being atomic across
NFS.  This concept was mentioned in Mail::Box::Locker (which was
originally presented in Mail::Folder::Maildir).  Some routine flow is
taken from there -- particularly the idea of creating a random local
file, hard linking a common file to the local file, and then checking
the nlink status.  Some ideologies were not complete (uncache
mechanism, shared locking) and some coding was even incorrect (wrong
stat index).  File::NFSLock was written to be light, generic,
and fast.

%prep
%setup -q -n %{module}-%{version}
chmod -R u+w %_builddir/%module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/File/

%changelog
* Fri Nov 09 2018 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- automated CPAN update

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.20-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.20-alt2
- fix directory ownership violation

* Mon Jun 06 2005 Vitaly Lipatov <lav@altlinux.ru> 1.20-alt1
- first build for ALT Linux Sisyphus
