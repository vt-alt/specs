Name: bootstrap-p9-freeipa-ppc64le-fake-python3-ipalib
Version: 0
Release: alt1

Summary: Fake python3 provides to bootstrap freeipa for ppc64le in p9
License: N/A
Group: Other

ExclusiveArch: ppc64le

Provides: python3(ipalib)
Provides: python3(ipalib.constants)
Provides: python3(ipalib.errors)
Provides: python3(ipalib.krb_utils)

%description
%summary.

The following packages have unmet dependencies:
  python3-module-custodia: Depends: python3(ipalib) (< 0) but it is not installable
                           Depends: python3(ipalib.constants) (< 0) but it is not installable
                           Depends: python3(ipalib.errors) (< 0) but it is not installable
                           Depends: python3(ipalib.krb_utils) (< 0) but it is not installable

%files

%changelog
* Sat Jul 06 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0-alt1
- Initial build (this hack should be dropped right after build of freeipa).
