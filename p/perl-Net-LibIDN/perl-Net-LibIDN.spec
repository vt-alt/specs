%global pkgname Net-LibIDN

Summary:  Perl bindings for GNU LibIDN
Name:     perl-Net-LibIDN
Version:  0.12
Release:  alt11
Group:    Development/Perl
License:  GPL-1.0+ or Artistic-1.0
URL:      https://metacpan.org/release/%{pkgname}

Source:   https://cpan.metacpan.org/authors/id/T/TH/THOR/%{pkgname}-%{version}.tar.gz
# Use distribution CFLAGS for tests, bug #1242794, CPAN RT#105853
Patch0:   Net-LibIDN-0.12-Respect-Config-s-cc-ccflags-and-ldflags.patch

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
BuildRequires: libidn-devel >= 0.4.0
BuildRequires: perl-devel >= 5.8.0
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Getopt/Long.pm)
# Run-time:
BuildRequires: perl(AutoLoader.pm)
BuildRequires: perl(Carp.pm)
BuildRequires: perl(Exporter.pm)
# Tests:
BuildRequires: perl(Test.pm)

%description
Provides perl bindings for GNU Libidn, a C library for handling
Internationalized Domain Names according to IDNA (RFC 3490), in
a way very much inspired by Turbo Fredriksson's PHP-IDN.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1
# Change man page encoding into UTF-8
for F in _LibIDN.pm; do
    iconv -f latin1 -t utf-8 < "$F" > "${F}.utf"
    sed -i -e '/^=encoding\s/ s/latin1/utf-8/' "${F}.utf"
    touch -r "$F" "${F}.utf"
    mv "${F}.utf" "$F"
done;

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete

%check
make test

%files
%doc README
%perl_vendor_archlib/Net
%perl_vendor_archlib/auto/Net

%changelog
* Tue Aug 25 2020 Andrey Cherepanov <cas@altlinux.org> 0.12-alt11
- Inital build in Sisyphus (based on version from fcimport).
