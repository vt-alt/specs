%define        pkgname artifactory-client
%define        gemname artifactory

Name:          ruby-%pkgname
Version:       3.0.1
Release:       alt1
Summary:       A simple, lightweight Ruby client for interacting with the Artifactory API.
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/artifactory-client
# VCS          https://github.com/chef/artifactory-client.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby


%description
A Ruby client and interface to the Artifactory API. The majority of API
endpoints are only exposed for Artifactory Pro customers! As such, many of
the resources and actions exposed by this gem also require Artifactory Pro.

The Artifactory gem offers a convienent interface for managing various parts of
the Artifactory API.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Thu Jun 13 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- Bump to 3.0.1
- Use Ruby Policy 2.0
- Fix lost provides (closes #36888)

* Mon Jan 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.0.0-alt1
- version fixed 3.0.0

* Tue Dec 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.8.6-alt1
- Initial build for Sisyphus
