%define _unpackaged_files_terminate_build 1
#
#   - File::Touch -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       '--packager=Igor Vlasenko <viy@altlinux.ru>' ../SOURCES/perl-File-Touch/File-Touch-0.08.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module File-Touch
%define m_distro File-Touch
%define m_name File::Touch
%define m_author_id unknown
%define _enable_test 1

Name: perl-File-Touch
Version: 0.12
Release: alt1

Summary: update access and modification timestamps, creating nonexistent files where necessary

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Igor Vlasenko <viy@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/N/NE/NEILB/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Sat Jul 10 2010
BuildRequires: perl-devel

%description
Here's a list of arguments that can be used with the object-oriented contruction:

=over 4

=item atime_only => [0|1]

If nonzero, change only the access time of files. Default is zero.

=item mtime_only => [0|1]

If nonzero, change only the modification time of files. Default is zero.

=item no_create => [0|1]

If nonzero, do not create new files. Default is zero.

=item reference => $reference_file

If defined, use timestamps from this file instead of current time. Default is undefined.

=item atime => $time

If defined, use this time (in epoch seconds) instead of current time for access time.

=item mtime => $time

If defined, use this time (in epoch seconds) instead of current time for modification time.

=back

%prep
%setup -q -n %{module}-%{version}
%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%doc Changes LICENSE README
%perl_vendor_privlib/File/*

%changelog
* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0.12-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Sat Jul 10 2010 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- initial build for ALT Linux Sisyphus

