Name: alt-issue
Version: 1.1
Release: alt1

Summary: Create issue.d banners for ALT distros
License: GPLv2
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/
Source: %name-%version.tar
BuildArch: noarch

Obsoletes: %name-server-v < %EVR

%description
%summary.

%package server
Summary: Create informational banner for ALT Server installation
License: GPLv2
Group: System/Configuration/Other
Requires: %name = %EVR

%description server
Create informational banner for ALT Server installation.

%package server-pve
Summary: Create informational banner for PVE installation
License: GPLv2
Group: System/Configuration/Other
Requires: %name-server = %EVR

%description server-pve
Create informational banner for PVE installation.

%prep

%install
mkdir -p %buildroot%_sysconfdir/issue.d

# Welcome:
cat > %buildroot%_sysconfdir/issue.d/00alt.issue <<EOF
Welcome to \R!

EOF

# Server:
cat > %buildroot%_sysconfdir/issue.d/00server.issue <<EOF
Hostname: \n
IP: \4
EOF

# PVE:
cat > %buildroot%_sysconfdir/issue.d/pve.issue <<EOF

Use https://\4:8006/ to manage your PVE server.

EOF

%post
touch %_sysconfdir/issue

%files
%_sysconfdir/issue.d/00alt.issue

%files server
%_sysconfdir/issue.d/00server.issue

%files server-pve
%_sysconfdir/issue.d/pve.issue

%changelog
* Thu May 27 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.1-alt1
- change package structure, use \R macros

* Mon May 24 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt1
- initial build for ALT

