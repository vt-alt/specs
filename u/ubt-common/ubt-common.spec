
%define branch_prefix .
%define branch_id M90P
%define branch_suffix .1

Name: ubt-common
Version: 0.3
Release: alt0.1

Group: Development/Other
Summary: Common Universal Branch Tag
Url: http://www.altlinux.org
License: GPL

BuildArch: noarch

Source1: macros

%description
Base set of RPM macroses for building one tag for all binary branches.

%package -n rpm-macros-ubt
Summary: Base set of RPM macros for packaging Universal Branch Tag
Group: Development/Other
%description -n rpm-macros-ubt
Base set of RPM macroses for building one tag for all binary branches.

%prep
%setup -cT

%install
install -D -m 0644 %SOURCE1 %buildroot/%_rpmmacrosdir/ubt
cat <<__EOF__ >%buildroot/%_rpmmacrosdir/ubt
%%__ubt_branch_prefix %branch_prefix
%%__ubt_branch_id %branch_id
%%__ubt_branch_suffix %branch_suffix
__EOF__

%files -n rpm-macros-ubt
%_rpmmacrosdir/ubt

%changelog
* Mon Jun 03 2019 Sergey V Turchin <zerg@altlinux.org> 0.3-alt0.1
- update for M90P

* Mon Jun 03 2019 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- update branch_id

* Mon Feb 27 2017 Sergey V Turchin <zerg@altlinux.org> 0.2-alt2
- bump release

* Fri Dec 02 2016 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- extend internal macros

* Thu Dec 01 2016 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
