%define        pkgname ansi

Name:          gem-%pkgname
Version:       1.5.0
Release:       alt1
Summary:       Set of ANSI Code based classes and modules for Ruby
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           http://rubyworks.github.io/ansi/
%vcs           https://github.com/rubyworks/ansi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
The ANSI project is a collection of ANSI escape code related libraries enabling
ANSI code based colorization and stylization of output. It is very nice
for beautifying shell output.

This collection is based on a set of scripts spun-off from Ruby Facets. Included
are Code (used to be ANSICode), Logger, ProgressBar and String. In addition
the library includes Terminal which provides information about the current
output device.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

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

%files         doc
%ruby_gemdocdir

%changelog
* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
