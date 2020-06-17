Name:          foreman
Version:       1.24.2
Release:       alt6
Summary:       An application that automates the lifecycle of servers
License:       GPLv3
Group:         System/Servers
Url:           https://theforeman.org
Vcs:           https://github.com/theforeman/foreman.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Source1:       database.yml
Source2:       %name.sysconfig
Source3:       %name.logrotate
Source4:       %name.cron.d
Source5:       %name.tmpfiles
# Source6:       dynflowd.sysconfig
# Source7:       dynflowd.service
Source8:       %name.service
Source9:       %name-production-%version.tar
Patch:         patch.patch
Patch1:        sass.patch
Patch2:        1.22.2.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-macros-webserver-common
BuildRequires: ruby-gem(asciidoctor)
# npmjs
BuildRequires: elfutils
BuildRequires: glibc-core
BuildRequires: libX11-devel
#BuildRequires: libnss-devel
BuildRequires: libnspr-devel
BuildRequires: fontconfig
BuildRequires: libfreetype-devel
BuildRequires: node-sass

Requires:      wget
Requires:      vixie-cron
Requires:      postgresql-server
# npmjs
Requires:      libX11
Requires:      libnss
Requires:      libnspr
Requires:      fontconfig
Requires:      libfreetype

Requires:      node-sass
# explicit TODO then remove
Requires:      gem-sshkey
Requires:      gem-ldap-fluff
Requires:      gem-little-plugger
Requires:      gem-http-cookie
Requires:      gem-apipie-params
Requires:      gem-arel
Requires:      gem-secure-headers >= 6.3.0
Requires:      gem-ovirt-engine-sdk
Requires:      gem-rails-dom-testing
Requires:      gem-spice-html5-rails >= 0.1.5-alt1
Requires:      gem-gridster-rails >= 0.5.6.1-alt1

%gem_replace_version rails ~> 5.2
%gem_replace_version graphql ~> 1.9
%gem_replace_version jquery-ui-rails ~> 6.0
%gem_replace_version patternfly-sass ~> 3.38
%gem_replace_version fog-core ~> 2.1
%gem_replace_version prometheus-client ~> 2.0
%add_findreq_skiplist *.pyc
%add_findreq_skiplist *.pyo
%add_findreq_skiplist *.erb
%add_findreq_skiplist %_libexecdir/%name/**/*

# npmjs
%add_verify_elf_skiplist %_libexecdir/%name/**/*
# used binaries in node_modules
ExclusiveArch: x86_64

%description
Foreman is a free open source project that gives you the power to easily
automate repetitive tasks, quickly deploy applications, and proactively
manage your servers lifecyle, on-premises or in the cloud.
From provisioning and configuration to orchestration and monitoring,
Foreman integrates with your existing infrastructure to make operations
easier.
Using Puppet, Ansible, Chef, Salt and Foreman's smart proxy
architecture, you can easily automate repetitive tasks, quickly deploy
applications, and proactively manage change, both on-premise with VMs
and bare-metal or in the cloud.
Foreman provides comprehensive, interaction facilities including a web
frontend, CLI and RESTful API which enables you to build higher level
business logic on top of a solid foundation.


%package       doc
Summary:       Foreman code documentation
Group:         Development/Documentation

%description   doc
Foreman code documentation.


%prep
%setup -a 9
%patch -p1
# TODO remove when patternfly-sass gem will be upgraded to new font-awesome-sass v5
%patch1 -p1
%patch2
sed -e "s/a2x/asciidoctor/" -e "s/-f/-b/" -i Rakefile.dist # NOTE patching a2x to asciidoctor
sed "s,gem 'turbolinks'.*,gem 'gitlab-turbolinks-classic'," -i Gemfile
rm -rf ./node_modules/node-sass/ ./node_modules/.bin/node-sass

%build
%ruby_build --ignore=font-awesome-sass --use=foreman --join=lib:bin --srcexedirs= --srcconfdirs= --srclibdirs=
# Build man pages
# rake -f Rakefile.dist build PREFIX=%_prefix SBINDIR=%_sbindir SYSCONFDIR=%_sysconfdir
# Build locale files
make -C locale all-mo

%install
%ruby_install
rm -rf %buildroot%_libexecdir/%name/extras/{jumpstart,spec}

# Create VERSION file
install -pm0644 VERSION %buildroot%_libexecdir/%name/VERSION
cp -r node_modules/.bin %buildroot%_libexecdir/%name/node_modules/

install -Dm0755 %SOURCE1 %buildroot%_libexecdir/%name/config/database.yml
install -Dm0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -Dm0644 %SOURCE3 %buildroot%_logrotatedir/%name
install -Dm0644 %SOURCE4 %buildroot%_sysconfdir/cron.d/%name
install -Dm0644 %SOURCE5 %buildroot%_tmpfilesdir/%name.conf
# install -Dm0644 %%SOURCE6 %buildroot%_sysconfdir/sysconfig/dynflowd
# install -Dm0644 %%SOURCE7 %buildroot%_unitdir/dynflowd.service
install -Dm0755 %SOURCE8 %buildroot%_unitdir/%name.service

# public www TODO
mkdir -p %buildroot%webserver_datadir
mv %buildroot%_libexecdir/%name/public %buildroot%webserver_datadir/%name
ln -svr %webserver_datadir/%name %buildroot%_libexecdir/%name/public

install -d %buildroot%_logdir/%name

%pre
# Add the "foreman" user and group
getent group foreman >/dev/null || groupadd -r foreman
getent passwd _foreman >/dev/null || \
useradd -r -g foreman -d %_libexecdir/%name -s /bin/bash -c "Foreman" _foreman
exit 0

%post
#railsctl setup %name
# %post_service foreman
# %post_service dynflowd

%preun
railsctl cleanup %name
# %preun_service foreman
# %preun_service dynflowd


%files
%doc README* CONTRIBUTING.md LICENSE
# %_sbindir/dynflowd
# %config(noreplace) %_sysconfdir/%name/logging.yaml
# %config(noreplace) %_sysconfdir/%name/settings.yaml
# %dir %_sysconfdir/%name/plugins
%_libexecdir/%name
# %exclude %_datadir/%name/bundler.d/*
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_logrotatedir/%name
%_sysconfdir/cron.d/%name
%_tmpfilesdir/%name.conf
# %config(noreplace) %_sysconfdir/sysconfig/dynflowd
# %_unitdir/dynflowd.service
%_unitdir/*
%webserver_datadir/%name
%attr(750,_foreman,foreman) %_logdir/%name
# %attr(750,_foreman,foreman) %_localstatedir/%name
# %_man8dir/*.8*

%files         doc
%ruby_ridir/*

%changelog
* Fri May 19 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt6
- * tmpfiles.d file

* Fri May 15 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt5
- ! patches and requires

* Fri May 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt4
- + explicit require deps to gem-secure-headers
- - post call to railsctl on install
- ! service name call to railsctl in .service

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt3
- - post exec in spec
- * with service run using 'railsctl'
- ! gem rails deps to ~> 5.2

* Mon Mar 30 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt2
- * moving code from %%_libdir -> %%_libexecdir

* Mon Mar 02 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt1
- updated (^) 1.22.2 -> 1.24.2
- updated (^) node modules
- fixed (!) systemd service file, and spec deps

* Wed Feb 26 2020 Pavel Skrylev <majioa@altlinux.org> 1.22.2-alt1
- updated (^) 1.22.0 -> 1.22.2
- added (+) post script condition to initialize the foreman after the db is
  initialized and started
- fixed (!) rails db/migration
- fixed (!) post-install code

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1.22.0-alt3
- drop libnss-devel buildreq
- update node_modules with node.js >= 13

* Mon Nov 25 2019 Pavel Skrylev <majioa@altlinux.org> 1.22.0-alt2
- changed (*) license
- fixed (!) requires and required service
- added (+) vcs tag to spec
- fixed (!) post install procedure, running the postgres server to setup users
  and db

* Thu Sep 26 2019 Pavel Skrylev <majioa@altlinux.org> 1.22.0-alt1
- updated (^) 1.20.1 -> 1.22.0
- fixed (!) run and primarily work, js is bundled in

* Mon Jan 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.20.1-alt1
- Bump to 1.20.1.

* Thu Sep 27 2018 Pavel Skrylev <majioa@altlinux.org> 1.19.0-alt5
- Patch to support 5.2 rails from master.
- Rake tasks moved to named subfolder.
- Avoid aarch64

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.19.0-alt2
- Bumped to 1.19 with Gemfile fix.
- Enable auto req detection.

* Fri Sep 21 2018 Andrey Cherepanov <cas@altlinux.org> 1.19.0-alt1
- New version.

* Sun Jul 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.18.0-alt1
- New version.

* Fri May 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.17.1-alt1
- New version.

* Thu Apr 12 2018 Andrey Cherepanov <cas@altlinux.org> 1.17.0-alt1
- Initial build in Sisyphus
