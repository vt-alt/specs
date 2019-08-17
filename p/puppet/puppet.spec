%define        pkgname        puppet
%define        confdir        ext/redhat
%define        core_version   6.8.0
%define        dm_version     1.0.1

Name:          %pkgname
Version:       %core_version
Release:       alt1
Summary:       A network tool for managing many disparate systems
Group:         System/Servers
License:       ASL 2.0
URL:           https://puppet.com/
# VCS:         https://github.com/puppetlabs/puppet.git
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       client.init
Source2:       puppet.service
Source3:       puppet-nm-dispatcher

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(yard)

%gem_replace_version CFPropertyList ~> 3.0
%gem_replace_version fast_gettext ~> 1.7
%add_findreq_skiplist %ruby_gemslibdir/*

Requires: shadow-change


%description
Puppet lets you centrally manage every important aspect of your
system using a cross-platform specification language that manages
all the separate elements normally aggregated in different files,
like users, cron jobs, and hosts, along with obviously discrete
elements like packages, services, and files.


%package       -n gem-deep-merge
Version:       %dm_version
Summary:       Deep merge hash
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-deep-merge
%summary.


%package       -n gem-deep-merge-doc
Version:       %dm_version
Summary:       Documentation for gem-deep-merge gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-deep-merge-doc
%summary.


%package       -n gem-%pkgname
Version:       %core_version
Summary:       Core library code for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname
%summary.


%package       -n gem-%pkgname-doc
Version:       %core_version
Summary:       Documentation for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
%summary.


%prep
%setup -n %name-%version

%build
%gem_build

%install
%gem_install

# SysVInit files
install -Dp -m0644 %confdir/client.sysconfig %buildroot%_sysconfdir/sysconfig/puppet
install -Dp -m0755 %SOURCE1 %buildroot%_initrddir/puppet
# Systemd files
install -Dp -m0644 %SOURCE2 %buildroot%_unitdir/puppet.service
ln -s %_unitdir/puppet.service %buildroot%_unitdir/puppetagent.service

install -Dp -m0644 %confdir/logrotate %buildroot%_sysconfdir/logrotate.d/puppet
install -Dp -m0644 conf/fileserver.conf %buildroot%_sysconfdir/puppet/fileserver.conf

# Create other configuration directories
mkdir -p %buildroot%_sysconfdir/puppet/ssl/{public_keys,certificate_requests,certs,ca/requests,ca/private,ca/signed,private,private_keys}
mkdir -p %buildroot%_sysconfdir/puppet/{code,modules,environments/production/manifests}

# Setup tmpfiles.d config
mkdir -p %buildroot%_tmpfilesdir
echo "D /run/%name 0755 _%name %name -" > \
    %buildroot%_tmpfilesdir/%name.conf

# Create puppet modules directory for puppet module tool
mkdir -p %buildroot%_sysconfdir/%name/modules

# Create service directory
mkdir -p %buildroot{%_localstatedir,%_logdir,%_var/run}/puppet

# Install NetworkManager dispatcher
install -Dpv %SOURCE3 \
    %buildroot%_sysconfdir/NetworkManager/dispatcher.d/98-%{name}

# Add puppetdb example configuration to puppet.conf
cat >> %buildroot%_sysconfdir/puppet/puppet.conf << END.
# Example of puppetdb integration
#[master]
#storeconfigs = true
#storeconfigs_backend = puppetdb
#report = true
#reports = puppetdb
END.

%pre
%_sbindir/groupadd -r -f puppet
%_sbindir/useradd -r -n -g puppet -d %_localstatedir/puppet -s /dev/null -c Puppet _puppet >/dev/null 2>&1 ||:

%post
%post_service puppet

%preun
%preun_service puppet

%files
%_bindir/puppet
%_initdir/puppet
%_unitdir/puppet.service
%_unitdir/puppetagent.service
%config(noreplace) %_tmpfilesdir/%name.conf
%dir %_sysconfdir/puppet
%attr(0771,_puppet,puppet) %dir %_sysconfdir/puppet/ssl
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/public_keys
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/certificate_requests
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/certs
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/ca
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/ca/requests
%attr(0750,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/ca/private
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/ca/signed
%attr(0750,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/private
%attr(0750,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/private_keys
%dir %_sysconfdir/puppet/environments
%dir %_sysconfdir/puppet/environments/production
%dir %_sysconfdir/puppet/environments/production/manifests
%dir %_sysconfdir/puppet/code
%dir %_sysconfdir/puppet/modules
%config(noreplace) %_sysconfdir/puppet/puppet.conf
%config(noreplace) %_sysconfdir/sysconfig/puppet
%config(noreplace) %_sysconfdir/logrotate.d/puppet
%config(noreplace) %_sysconfdir/puppet/fileserver.conf
%_sysconfdir/NetworkManager/dispatcher.d/98-%{name}
%attr(1770,_puppet,puppet) %dir %_localstatedir/puppet
%_localstatedir/puppet/
%attr(1770,_puppet,puppet) %dir %_logdir/puppet
%attr(1770,_puppet,puppet) %dir %_var/run/puppet
%doc %_man8dir/*
%doc %_man5dir/puppet.conf.5*


%files         -n gem-%pkgname
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-deep-merge
%ruby_gemspecdir/deep_merge-%dm_version.gemspec
%ruby_gemslibdir/deep_merge-%dm_version

%files         -n gem-deep-merge-doc
%ruby_gemsdocdir/deep_merge-%dm_version


%changelog
* Fri Aug 16 2019 Andrey Cherepanov <cas@altlinux.org> 6.8.0-alt1
- New version.

* Sat Jul 27 2019 Andrey Cherepanov <cas@altlinux.org> 6.7.2-alt1
- New version.

* Mon Jul 22 2019 Andrey Cherepanov <cas@altlinux.org> 6.7.0-alt1
- New version.

* Thu Jun 27 2019 Andrey Cherepanov <cas@altlinux.org> 6.6.0-alt1
- New version.

* Wed Jun 19 2019 Andrey Cherepanov <cas@altlinux.org> 6.5.0-alt1
- New version.

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 6.4.2-alt1
- New version.

* Thu Apr 11 2019 Andrey Cherepanov <cas@altlinux.org> 6.4.1-alt1
- New version.

* Mon Apr 01 2019 Andrey Cherepanov <cas@altlinux.org> 6.4.0-alt1
- New version.

* Sat Mar 09 2019 Pavel Skrylev <majioa@altlinux.org> 6.3.0-alt1
- Bump to 6.3.0;
- Use Ruby Policy 2.0.

* Mon Mar 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 6.1.0-alt2
- Requires fixed.

* Tue Dec 18 2018 Andrey Cherepanov <cas@altlinux.org> 6.1.0-alt1
- New version.

* Mon Dec 03 2018 Pavel Skrylev <majioa@altlinux.org> 6.0.4-alt2
- Repack to avoid unnecessary deps.

* Thu Nov 01 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.4-alt1
- New version.

* Mon Oct 29 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.3-alt1
- New version.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.2-alt1.qa1
- NMU: applied repocop patch

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.2-alt1
- New version.

* Tue Oct 02 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt1
- New version.

* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt2
- Updated deps of fast-gettext to 1.7.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- New version.
- Package ad gem.
- Use /run instead of /var/run in tmpfiles rules.
- puppet-server is deprecated. To run puppet as a server you must use puppetserver.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.6-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.2-alt1
- New version.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt3
- Fix "Cannot determine basic system flavour" (https://tickets.puppetlabs.com/browse/SERVER-14).

* Wed Apr 25 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt2
- Create and package all configuration directories.
- Add puppetdb example configuration to puppet.conf.

* Thu Apr 19 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt1
- New version.

* Wed Apr 04 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.0-alt1
- New version.

* Thu Oct 05 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.2-alt1
- New version

* Sat Sep 30 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt1
- New version

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- New version

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Aug 17 2017 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- New version

* Wed Jul 19 2017 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt1
- New version

* Wed Jun 28 2017 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version

* Mon Jun 19 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.4-alt1
- New version

* Fri Jun 16 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.3-alt1
- New version

* Tue Jun 13 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.2-alt1
- New version

* Sun May 21 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.1-alt1
- New version

* Mon Apr 10 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt1
- New version

* Wed Feb 01 2017 Andrey Cherepanov <cas@altlinux.org> 4.9.0-alt1
- new version 4.9.0

* Fri Jan 27 2017 Andrey Cherepanov <cas@altlinux.org> 4.8.2-alt1
- new version 4.8.2

* Wed Jan 18 2017 Andrey Cherepanov <cas@altlinux.org> 4.8.1-alt1
- new version 4.8.1
- aptrpm package provider is default for ALT operating system

* Fri Oct 21 2016 Andrey Cherepanov <cas@altlinux.org> 4.7.0-alt2
- Fix build without bundled libraries
- Rebuild with fixed ruby autoreq (ALT #32601)

* Thu Oct 06 2016 Andrey Cherepanov <cas@altlinux.org> 4.7.0-alt1
- new version 4.7.0

* Mon Dec 28 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version
- Package missing directories (ALT #30148)

* Sat Apr 25 2015 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version

* Tue Jan 13 2015 Andrey Cherepanov <cas@altlinux.org> 3.7.3-alt1
- New version

* Thu May 15 2014 Andrey Cherepanov <cas@altlinux.org> 3.5.1-alt1
- New version
- Rename services to puppet, puppetmaster
- Add NetworkManager dispatcher script to pickup changes to
  /etc/resolv.conf and such

* Fri Jul 26 2013 Andrey Cherepanov <cas@altlinux.org> 2.7.21-alt2
- Set correct pid file name for services (ALT #29114)
- Set correct user name _puppet in configuration of puppetmasterd


* Fri Jun 07 2013 Andrey Cherepanov <cas@altlinux.org> 2.7.21-alt1
- New version 2.7.21 (ALT #28695)
- Use system group `puppet` instead `_puppet` (ALT #28273)
- New format of puppet.conf (ALT #28517)

* Fri Nov 30 2012 Led <led@altlinux.ru> 2.7.5-alt1.2
- Rebuilt with ruby-1.9.3-alt1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.7.5-alt1.1
- Rebuild with Python-2.7

* Thu Oct 06 2011 Sergey Alembekov <rt@altlinux.ru> 2.7.5-alt1
- [2.7.5]

* Tue Sep 27 2011 Sergey Alembekov <rt@altlinux.ru> 2.7.3-alt1
- [2.7.3]

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.24.8-alt1
- [0.24.8]

* Sat Dec 20 2008 Sir Raorn <raorn@altlinux.ru> 0.24.6-alt3
- Fixed interpackage dependencies

* Sat Dec 20 2008 Sir Raorn <raorn@altlinux.ru> 0.24.6-alt2
- Cleaned up build deps

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 0.24.6-alt1
- [0.24.6]

* Tue Aug 26 2008 Sir Raorn <raorn@altlinux.ru> 0.24.5-alt1
- Built for Sisyphus

