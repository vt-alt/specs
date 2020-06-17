%define        pkgname rqrcode

Name:          ruby-%pkgname
Version:       1.1.2
Release:       alt1
Summary:       A library to encode QR Codes
Group:         Development/Ruby
License:       MIT
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/whomwah/rqrcode
Source:        %name-%version.tar
BuildArch:     noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec)
BuildRequires: gem(rake)
BuildRequires: gem(rqrcode_core) >= 0.1
BuildRequires: gem(chunky_png) >= 1.0

%description
rqrcode is a library for encoding QR Codes. The simple
interface allows you to create QR Code data structures
and then render them in the way you choose.

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
* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 1.1.2-alt1
- Initial build.
