%define        pkgname po-to-json
%define        gemname po_to_json

Name:          gem-%pkgname
Version:       1.0.1
Release:       alt1
Summary:       Convert gettext PO files to JSON objects so that you can use it in your application
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/webhippie/po_to_json
%vcs           https://github.com/webhippie/po_to_json.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Convert gettext PO files to JSON to use in your javascript app, based on
po2json.pl by DuckDuckGo, Inc.. Ideally you'll use this on a Rake task that
creates JSON versions of your PO files, which can later be used from javascript
with Jed.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
