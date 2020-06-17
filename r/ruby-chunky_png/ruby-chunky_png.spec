%define        pkgname chunky_png

Name:          ruby-%pkgname
Version:       1.3.11
Release:       alt1
Summary:       Pure ruby library for read/write, chunk-level access to PNG files
Group:         Development/Ruby
License:       MIT
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/wvanbergen/chunky_png
Source:        %name-%version.tar
BuildArch:     noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec)
BuildRequires: gem(rake)

%description
This pure Ruby library can read and write PNG images without depending on an external
image library, like RMagick. It tries to be memory efficient and reasonably fast.

It supports reading and writing all PNG variants that are defined in the specification,
with one limitation: only 8-bit color depth is supported. It supports all transparency,
interlacing and filtering options the PNG specifications allows. It can also read and
write textual metadata from PNG files. Low-level read/write access to PNG chunks is
also possible.

This library supports simple drawing on the image canvas and simple operations like
alpha composition and cropping. Finally, it can import from and export to RMagick for
interoperability.

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
* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 1.3.11-alt1
- Initial build.
