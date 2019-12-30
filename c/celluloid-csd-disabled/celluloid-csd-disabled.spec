Name: celluloid-csd-disabled
Version: 0.1
Release: alt1
Summary: Disable client-side decorations and dark-theme for celluloid
License: GPL
Group: Graphical desktop/Other

BuildArch: noarch

Requires(post): dconf
Requires(postun): dconf

%description
%summary

%install
mkdir -p %buildroot%_sysconfdir/dconf/profile

cat > %buildroot%_sysconfdir/dconf/profile/user <<EOF
user-db:user
system-db:local
EOF

mkdir -p %buildroot%_sysconfdir/dconf/db/local.d

cat > %buildroot%_sysconfdir/dconf/db/local.d/01-celluloid-csd-disabled <<EOF
[io/github/celluloid-player/celluloid]
csd-enable=false
dark-theme-enable=false
EOF

%post
dconf update

%postun
dconf update

%files
%_sysconfdir/dconf/profile/user
%_sysconfdir/dconf/db/local.d/01-celluloid-csd-disabled

%changelog
* Mon Dec 23 2019 Dmitry Terekhin <jqt4@altlinux.org> 0.1-alt1
- Initial build for ALT
