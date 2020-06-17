%define        pkgname rotp

Name:          ruby-%pkgname
Version:       5.1.0
Release:       alt1
Summary:       A Ruby library for generating and verifying one time passwords
Group:         Development/Ruby
License:       BSD
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/chuckremes/ffi-rzmq-core.git
Source:        %name-%version.tar
BuildArch:     noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec)
BuildRequires: gem(rake)
BuildRequires: gem(simplecov)
BuildRequires: gem(timecop)

%description
A Ruby library for generating and verifying one time passwords.
Works for both HOTP and TOTP, and includes QR Code provisioning.

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation

%description   doc
Documentation files for %gemname gem.

%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemsdocdir/*

%changelog
* Fri Jan 31 2020 Alexey Shabalin <shaba@altlinux.org> 5.1.0-alt1
- Initial build.
