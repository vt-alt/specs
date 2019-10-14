
Name: adobe-flash-player
%define bin_name mozilla-plugin-adobe-flash
%define ver_fake 32
%define ver_ix86 32.0.0.270
%define ver_x86_64 32.0.0.270
Release: alt16
Epoch: 3

%define ver_real %ver_fake
%ifarch x86_64
%define ver_real %ver_x86_64
%endif
%ifarch %ix86
%define ver_real %ver_ix86
%endif
Version: %ver_fake

Group: Networking/WWW
Summary: Adobe Flash Player NPAPI compatibility
URL: http://www.adobe.com/products/flashplayer/
License: GPL

ExclusiveArch: %ix86 x86_64
#BuildArch: noarch

BuildRequires(pre): rpm-build-ubt
BuildRequires: rpm-macros-browser-plugins

Source: versions

%description
Adobe Flash Player NPAPI compatibility collective package.

%package -n %bin_name
Version: %ver_real
Group: Networking/WWW
Summary: Adobe Flash Player NPAPI compatibility
Requires: freshplayerplugin ppapi-plugin-adobe-flash
Provides: flash-plugin = %version
Obsoletes: flash-plugin < %version
Provides: mozilla-plugin-macromedia-flash = %version-%release
Obsoletes: mozilla-plugin-macromedia-flash < %version-%release
%description -n %bin_name
Adobe Flash Player NPAPI compatibility collective package.

%package fake
Version: %ver_fake
Group: Networking/WWW
Summary: fake
%description fake
fake


%prep
%setup -Tqcn flash_player_%{version}_linux


%files -n %bin_name

%changelog
* Sat Oct 12 2019 Cronbuild Service <cronbuild@altlinux.org> 3:32-alt16
- repocop cronbuild 20191012. At your service.

* Tue Sep 10 2019 Cronbuild Service <cronbuild@altlinux.org> 3:32-alt15
- repocop cronbuild 20190910. At your service.

* Tue Aug 13 2019 Cronbuild Service <cronbuild@altlinux.org> 3:32-alt14
- repocop cronbuild 20190813. At your service.

* Fri Jul 12 2019 Cronbuild Service <cronbuild@altlinux.org> 3:32-alt13
- repocop cronbuild 20190712. At your service.

* Fri Jun 14 2019 Cronbuild Service <cronbuild@altlinux.org> 3:32-alt12
- repocop cronbuild 20190614. At your service.

* Fri Jun 14 2019 Sergey V Turchin <zerg@altlinux.org> 3:32-alt11
- fix cronbuild support

* Wed May 15 2019 Cronbuild Service <cronbuild@altlinux.org> 3:32-alt10
- repocop cronbuild 20190515. At your service.

* Tue Apr 09 2019 Cronbuild Service <cronbuild@altlinux.org> 3:32-alt9
- repocop cronbuild 20190409. At your service.

* Tue Mar 12 2019 Cronbuild Service <cronbuild@altlinux.org> 3:32-alt8
- repocop cronbuild 20190312. At your service.

* Thu Mar 07 2019 Cronbuild Service <cronbuild@altlinux.org> 3:32-alt7
- small fix in .gear/cronbuild-update-source

* Wed Mar 06 2019 Sergey V Turchin <zerg@altlinux.org> 3:32-alt6
- fix cronbuild support

* Thu Feb 28 2019 Sergey V Turchin <zerg@altlinux.org> 3:32-alt5
- fix cronbuild support

* Mon Feb 18 2019 Cronbuild Service <cronbuild@altlinux.org> 3:32-alt4
- repocop cronbuild 20190218. At your service.

* Thu Feb 14 2019 Cronbuild Service <cronbuild@altlinux.org> 3:32-alt3
- repocop cronbuild 20190214. At your service.

* Thu Feb 14 2019 Sergey V Turchin <zerg@altlinux.org> 3:32-alt2
- fix cronbuid support

* Tue Jan 15 2019 Sergey V Turchin <zerg@altlinux.org> 3:32-alt1
- bump version

* Tue Oct 02 2018 Sergey V Turchin <zerg@altlinux.org> 3:31-alt1%ubt
- bump version

* Tue Aug 14 2018 Sergey V Turchin <zerg@altlinux.org> 3:30-alt2%ubt
- bump version
- fix to obsolete only old adobe package (ALT#35244)

* Thu Aug 09 2018 Sergey V Turchin <zerg@altlinux.org> 3:30-alt1%ubt
- bump version

* Mon May 07 2018 Sergey V Turchin <zerg@altlinux.org> 3:29-alt1%ubt
- bump version

* Mon Dec 25 2017 Sergey V Turchin <zerg@altlinux.org> 3:28-alt1%ubt
- bump version

* Thu Sep 21 2017 Sergey V Turchin <zerg@altlinux.org> 3:27-alt1%ubt
- bump version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 3:26-alt1%ubt
- bump version

* Mon Mar 20 2017 Sergey V Turchin <zerg@altlinux.org> 3:25-alt1%ubt
- bump version

* Fri Dec 16 2016 Sergey V Turchin <zerg@altlinux.org> 3:24-alt2
- bump version

* Fri Nov 18 2016 Sergey V Turchin <zerg@altlinux.org> 3:13-alt3
- fix description (ALT#32764)

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 3:13-alt2
- clean requires

* Wed Nov 09 2016 Sergey V Turchin <zerg@altlinux.org> 3:13-alt1
- empty package
- require firefox-pepperflash

* Wed Nov 09 2016 Sergey V Turchin <zerg@altlinux.org> 3:11-alt68
- new version
- security fixes:
  CVE-2016-7857, CVE-2016-7858, CVE-2016-7859, CVE-2016-7860,
  CVE-2016-7861, CVE-2016-7862, CVE-2016-7863, CVE-2016-7864,
  CVE-2016-7865

* Thu Oct 27 2016 Sergey V Turchin <zerg@altlinux.org> 3:11-alt67
- new version
- security fixes: CVE-2016-7855

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 3:11-alt66
- new version
- security fixes:
  CVE-2016-4273, CVE-2016-4286, CVE-2016-6981, CVE-2016-6982,
  CVE-2016-6983, CVE-2016-6984, CVE-2016-6985, CVE-2016-6986,
  CVE-2016-6987, CVE-2016-6989, CVE-2016-6990, CVE-2016-6992

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 3:11-alt65
- new version
  CVE-2016-4271, CVE-2016-4272, CVE-2016-4274, CVE-2016-4275,
  CVE-2016-4276, CVE-2016-4277, CVE-2016-4278, CVE-2016-4279,
  CVE-2016-4280, CVE-2016-4281, CVE-2016-4282, CVE-2016-4283,
  CVE-2016-4284, CVE-2016-4285, CVE-2016-4287, CVE-2016-6921,
  CVE-2016-6922, CVE-2016-6923, CVE-2016-6924, CVE-2016-6925,
  CVE-2016-6926, CVE-2016-6927, CVE-2016-6929, CVE-2016-6930,
  CVE-2016-6931, CVE-2016-6932

* Wed Jul 20 2016 Sergey V Turchin <zerg@altlinux.org> 3:11-alt64
- new version
- security fixes:
  CVE-2016-4172, CVE-2016-4173, CVE-2016-4174, CVE-2016-4175,
  CVE-2016-4176, CVE-2016-4177, CVE-2016-4178, CVE-2016-4179,
  CVE-2016-4180, CVE-2016-4181, CVE-2016-4182, CVE-2016-4183,
  CVE-2016-4184, CVE-2016-4185, CVE-2016-4186, CVE-2016-4187,
  CVE-2016-4188, CVE-2016-4189, CVE-2016-4190, CVE-2016-4217,
  CVE-2016-4218, CVE-2016-4219, CVE-2016-4220, CVE-2016-4221,
  CVE-2016-4222, CVE-2016-4223, CVE-2016-4224, CVE-2016-4225,
  CVE-2016-4226, CVE-2016-4227, CVE-2016-4228, CVE-2016-4229,
  CVE-2016-4230, CVE-2016-4231, CVE-2016-4232, CVE-2016-4233,
  CVE-2016-4234, CVE-2016-4235, CVE-2016-4236, CVE-2016-4237,
  CVE-2016-4238, CVE-2016-4239, CVE-2016-4240, CVE-2016-4241,
  CVE-2016-4242, CVE-2016-4243, CVE-2016-4244, CVE-2016-4245,
  CVE-2016-4246, CVE-2016-4247, CVE-2016-4248, CVE-2016-4249

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 3:11-alt63
- new version
- security fixes:
  CVE-2016-4122, CVE-2016-4123, CVE-2016-4124, CVE-2016-4125,
  CVE-2016-4127, CVE-2016-4128, CVE-2016-4129, CVE-2016-4130,
  CVE-2016-4131, CVE-2016-4132, CVE-2016-4133, CVE-2016-4134,
  CVE-2016-4135, CVE-2016-4136, CVE-2016-4137, CVE-2016-4138,
  CVE-2016-4139, CVE-2016-4140, CVE-2016-4141, CVE-2016-4142,
  CVE-2016-4143, CVE-2016-4144, CVE-2016-4145, CVE-2016-4146,
  CVE-2016-4147, CVE-2016-4148, CVE-2016-4149, CVE-2016-4150,
  CVE-2016-4151, CVE-2016-4152, CVE-2016-4153, CVE-2016-4154,
  CVE-2016-4155, CVE-2016-4156, CVE-2016-4166, CVE-2016-4171

* Fri May 13 2016 Sergey V Turchin <zerg@altlinux.org> 3:11-alt62
- new version
- security fixes:
  CVE-2016-1096, CVE-2016-1097, CVE-2016-1098, CVE-2016-1099,
  CVE-2016-1100, CVE-2016-1101, CVE-2016-1102, CVE-2016-1103,
  CVE-2016-1104, CVE-2016-1105, CVE-2016-1106, CVE-2016-1107,
  CVE-2016-1108, CVE-2016-1109, CVE-2016-1110, CVE-2016-4108,
  CVE-2016-4109, CVE-2016-4110, CVE-2016-4111, CVE-2016-4112,
  CVE-2016-4113, CVE-2016-4114, CVE-2016-4115, CVE-2016-4116,
  CVE-2016-4117

* Fri Apr 08 2016 Sergey V Turchin <zerg@altlinux.org> 3:11-alt61
- new version
- security fixes:
  CVE-2016-1006, CVE-2016-1011, CVE-2016-1012, CVE-2016-1013,
  CVE-2016-1014, CVE-2016-1015, CVE-2016-1016, CVE-2016-1017,
  CVE-2016-1018, CVE-2016-1019, CVE-2016-1020, CVE-2016-1021,
  CVE-2016-1022, CVE-2016-1023, CVE-2016-1024, CVE-2016-1025,
  CVE-2016-1026, CVE-2016-1027, CVE-2016-1028, CVE-2016-1029,
  CVE-2016-1030, CVE-2016-1031, CVE-2016-1032, CVE-2016-1033

* Fri Mar 11 2016 Sergey V Turchin <zerg@altlinux.org> 3:11-alt60
- new version
- security fixes:
  CVE-2016-0960, CVE-2016-0961, CVE-2016-0962, CVE-2016-0963,
  CVE-2016-0986, CVE-2016-0987, CVE-2016-0988, CVE-2016-0989,
  CVE-2016-0990, CVE-2016-0991, CVE-2016-0992, CVE-2016-0993,
  CVE-2016-0994, CVE-2016-0995, CVE-2016-0996, CVE-2016-0997,
  CVE-2016-0998, CVE-2016-0999, CVE-2016-1000, CVE-2016-1001,
  CVE-2016-1002, CVE-2016-1005, CVE-2016-1010

* Wed Feb 10 2016 Sergey V Turchin <zerg@altlinux.org> 3:11-alt59
- new version
- security fixes:
  CVE-2016-0964, CVE-2016-0965, CVE-2016-0966, CVE-2016-0967,
  CVE-2016-0968, CVE-2016-0969, CVE-2016-0970, CVE-2016-0971,
  CVE-2016-0972, CVE-2016-0973, CVE-2016-0974, CVE-2016-0975,
  CVE-2016-0976, CVE-2016-0977, CVE-2016-0978, CVE-2016-0979,
  CVE-2016-0980, CVE-2016-0981, CVE-2016-0982, CVE-2016-0983,
  CVE-2016-0984, CVE-2016-0985

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt58
- new version
- security fixes:
  CVE-2015-8459, CVE-2015-8460, CVE-2015-8634, CVE-2015-8635,
  CVE-2015-8636, CVE-2015-8638, CVE-2015-8639, CVE-2015-8640,
  CVE-2015-8641, CVE-2015-8642, CVE-2015-8643, CVE-2015-8644,
  CVE-2015-8645, CVE-2015-8646, CVE-2015-8647, CVE-2015-8648,
  CVE-2015-8649, CVE-2015-8650, CVE-2015-8651

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt57
- new version
- security fixes:
  CVE-2015-8045, CVE-2015-8047, CVE-2015-8048, CVE-2015-8049,
  CVE-2015-8050, CVE-2015-8418, CVE-2015-8454, CVE-2015-8455,
  CVE-2015-8055, CVE-2015-8056, CVE-2015-8057, CVE-2015-8058,
  CVE-2015-8059, CVE-2015-8060, CVE-2015-8061, CVE-2015-8062,
  CVE-2015-8063, CVE-2015-8064, CVE-2015-8065, CVE-2015-8066,
  CVE-2015-8067, CVE-2015-8068, CVE-2015-8069, CVE-2015-8070,
  CVE-2015-8071, CVE-2015-8401, CVE-2015-8402, CVE-2015-8403,
  CVE-2015-8404, CVE-2015-8405, CVE-2015-8406, CVE-2015-8407,
  CVE-2015-8408, CVE-2015-8409, CVE-2015-8410, CVE-2015-8411,
  CVE-2015-8412, CVE-2015-8413, CVE-2015-8414, CVE-2015-8415,
  CVE-2015-8416, CVE-2015-8417, CVE-2015-8419, CVE-2015-8420,
  CVE-2015-8421, CVE-2015-8422, CVE-2015-8423, CVE-2015-8424,
  CVE-2015-8425, CVE-2015-8426, CVE-2015-8427, CVE-2015-8428,
  CVE-2015-8429, CVE-2015-8430, CVE-2015-8431, CVE-2015-8432,
  CVE-2015-8433, CVE-2015-8434, CVE-2015-8435, CVE-2015-8436,
  CVE-2015-8437, CVE-2015-8438, CVE-2015-8439, CVE-2015-8440,
  CVE-2015-8441, CVE-2015-8442, CVE-2015-8443, CVE-2015-8444,
  CVE-2015-8445, CVE-2015-8446, CVE-2015-8447, CVE-2015-8448,
  CVE-2015-8449, CVE-2015-8450, CVE-2015-8451, CVE-2015-8452,
  CVE-2015-8453

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt56
- new version
- security fixes:
  CVE-2015-7651, CVE-2015-7652, CVE-2015-7653, CVE-2015-7654,
  CVE-2015-7655, CVE-2015-7656, CVE-2015-7657, CVE-2015-7658,
  CVE-2015-7659, CVE-2015-7660, CVE-2015-7661, CVE-2015-7662,
  CVE-2015-7663, CVE-2015-8042, CVE-2015-8043, CVE-2015-8044,
  CVE-2015-8046

* Mon Oct 19 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt55
- new version
- security fixes: CVE-2015-7645, CVE-2015-7647, CVE-2015-7648

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt54
- new version
- security fixes:
  CVE-2015-5569, CVE-2015-7625, CVE-2015-7626, CVE-2015-7627,
  CVE-2015-7628, CVE-2015-7629, CVE-2015-7630, CVE-2015-7631,
  CVE-2015-7632, CVE-2015-7633, CVE-2015-7634, CVE-2015-7643,
  CVE-2015-7644

* Fri Sep 25 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt53
- new version
- security fixes:
  CVE-2015-5567, CVE-2015-5568, CVE-2015-5570, CVE-2015-5571,
  CVE-2015-5572, CVE-2015-5573, CVE-2015-5574, CVE-2015-5575,
  CVE-2015-5576, CVE-2015-5577, CVE-2015-5578, CVE-2015-5579,
  CVE-2015-5580, CVE-2015-5581, CVE-2015-5582, CVE-2015-5584,
  CVE-2015-5587, CVE-2015-5588, CVE-2015-6676, CVE-2015-6677,
  CVE-2015-6678, CVE-2015-6679, CVE-2015-6682

* Wed Aug 12 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt52
- new version
- security fixes:
  CVE-2015-3107, CVE-2015-5124, CVE-2015-5125, CVE-2015-5127,
  CVE-2015-5128, CVE-2015-5129, CVE-2015-5130, CVE-2015-5131,
  CVE-2015-5132, CVE-2015-5133, CVE-2015-5134, CVE-2015-5539,
  CVE-2015-5540, CVE-2015-5541, CVE-2015-5544, CVE-2015-5545,
  CVE-2015-5546, CVE-2015-5547, CVE-2015-5548, CVE-2015-5549,
  CVE-2015-5550, CVE-2015-5551, CVE-2015-5552, CVE-2015-5553,
  CVE-2015-5554, CVE-2015-5555, CVE-2015-5556, CVE-2015-5557,
  CVE-2015-5558, CVE-2015-5559, CVE-2015-5560, CVE-2015-5561,
  CVE-2015-5562, CVE-2015-5563, CVE-2015-5564

* Sat Jul 18 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt51
- new version
- security fixes: CVE-2015-5122, CVE-2015-5123

* Tue Jul 14 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt50
- fix changelog
- security NOT fixed: CVE-2015-5122, CVE-2015-5123

* Mon Jul 13 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt49
- update changelog

* Wed Jul 08 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt48
- update changelog

* Wed Jul 08 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt47
- new version
- security fixes:
  CVE-2014-0578, CVE-2015-3097, CVE-2015-3114, CVE-2015-3115,
  CVE-2015-3116, CVE-2015-3117, CVE-2015-3118, CVE-2015-3119,
  CVE-2015-3120, CVE-2015-3121, CVE-2015-3122, CVE-2015-3123,
  CVE-2015-3124, CVE-2015-3125, CVE-2015-3126, CVE-2015-3127,
  CVE-2015-3128, CVE-2015-3129, CVE-2015-3130, CVE-2015-3131,
  CVE-2015-3132, CVE-2015-3133, CVE-2015-3134, CVE-2015-3135,
  CVE-2015-3136, CVE-2015-3137, CVE-2015-4428, CVE-2015-4429,
  CVE-2015-4430, CVE-2015-4431, CVE-2015-4432, CVE-2015-4433,
  CVE-2015-5116, CVE-2015-5117, CVE-2015-5118, CVE-2015-5119

* Wed Jun 24 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt46
- new version
- security fixes: CVE-2015-3113

* Wed Jun 10 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt45
- new version
- security fixes:
  CVE-2015-3096, CVE-2015-3097, CVE-2015-3098, CVE-2015-3099,
  CVE-2015-3100, CVE-2015-3101, CVE-2015-3102, CVE-2015-3103,
  CVE-2015-3104, CVE-2015-3105, CVE-2015-3106, CVE-2015-3107,
  CVE-2015-3108

* Thu May 14 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt44
- new version
- security fixes:
  CVE-2015-3044, CVE-2015-3077, CVE-2015-3078, CVE-2015-3079,
  CVE-2015-3080, CVE-2015-3081, CVE-2015-3082, CVE-2015-3083,
  CVE-2015-3084, CVE-2015-3085, CVE-2015-3086, CVE-2015-3087,
  CVE-2015-3088, CVE-2015-3089, CVE-2015-3090, CVE-2015-3091,
  CVE-2015-3092, CVE-2015-3093

* Wed Apr 15 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt43
- new version
- security fixes:
  CVE-2015-0346, CVE-2015-0347, CVE-2015-0348, CVE-2015-0349,
  CVE-2015-0350, CVE-2015-0351, CVE-2015-0352, CVE-2015-0353,
  CVE-2015-0354, CVE-2015-0355, CVE-2015-0356, CVE-2015-0357,
  CVE-2015-0358, CVE-2015-0359, CVE-2015-0360, CVE-2015-3038,
  CVE-2015-3039, CVE-2015-3040, CVE-2015-3041, CVE-2015-3042,
  CVE-2015-3043, CVE-2015-3044

* Fri Mar 13 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt42
- new version
- security fixes:
  CVE-2015-0332, CVE-2015-0333, CVE-2015-0334, CVE-2015-0335,
  CVE-2015-0336, CVE-2015-0337, CVE-2015-0338, CVE-2015-0339,
  CVE-2015-0340, CVE-2015-0341, CVE-2015-0342

* Fri Feb 06 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt41
- new version
- security fixes:
  CVE-2015-0313, CVE-2015-0314, CVE-2015-0315, CVE-2015-0316,
  CVE-2015-0317, CVE-2015-0318, CVE-2015-0319, CVE-2015-0320,
  CVE-2015-0321, CVE-2015-0322, CVE-2015-0323, CVE-2015-0324,
  CVE-2015-0325, CVE-2015-0326, CVE-2015-0327, CVE-2015-0328,
  CVE-2015-0329, CVE-2015-0330

* Wed Jan 28 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt40
- new version
- security fixes: CVE-2015-0311, CVE-2015-0312

* Fri Jan 23 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt39
- new version
- security fixes: CVE-2015-0310, CVE-2015-0311

* Wed Jan 14 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt38
- new version
- security fixes:
  CVE-2015-0301, CVE-2015-0302, CVE-2015-0303, CVE-2015-0304,
  CVE-2015-0305, CVE-2015-0306, CVE-2015-0307, CVE-2015-0308,
  CVE-2015-0309

* Wed Dec 10 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt37
- new version
- security fixes:
  CVE-2014-0580, CVE-2014-0587, CVE-2014-8443, CVE-2014-9162,
  CVE-2014-9163, CVE-2014-9164

* Wed Nov 26 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt36
- new version
- security fixes: CVE-2014-8439

* Wed Nov 12 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt35
- new version
- security fixes:
  CVE-2014-0573, CVE-2014-0574, CVE-2014-0576, CVE-2014-0577,
  CVE-2014-0581, CVE-2014-0582, CVE-2014-0583, CVE-2014-0584,
  CVE-2014-0585, CVE-2014-0586, CVE-2014-0588, CVE-2014-0589,
  CVE-2014-0590, CVE-2014-8437, CVE-2014-8438, CVE-2014-8440,
  CVE-2014-8441, CVE-2014-8442

* Wed Oct 15 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt34
- new version
- security fixes: CVE-2014-0570, CVE-2014-0571, CVE-2014-0572

* Wed Sep 10 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt33
- new version
- security fixes:
  CVE-2014-0547, CVE-2014-0548, CVE-2014-0549, CVE-2014-0550,
  CVE-2014-0551, CVE-2014-0552, CVE-2014-0553, CVE-2014-0554,
  CVE-2014-0555, CVE-2014-0556, CVE-2014-0557, CVE-2014-0559

* Mon Aug 18 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt32
- new version
- security fixes:
  CVE-2014-0538, CVE-2014-0540, CVE-2014-0541, CVE-2014-0542,
  CVE-2014-0543, CVE-2014-0544, CVE-2014-0545

* Wed Jul 16 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt31
- new version (ALT#30190)
- security fixes: CVE-2014-0537, CVE-2014-0539, CVE-2014-4671

* Mon Jun 16 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt30
- new version
- security fixes:
  CVE-2014-0531, CVE-2014-0532, CVE-2014-0533, CVE-2014-0534,
  CVE-2014-0535, CVE-2014-0536

* Tue Apr 29 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt29
- new version
- security fixes: CVE-2014-0515

* Tue Apr 15 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt28
- new version
- security fixes:
  CVE-2014-0506, CVE-2014-0507, CVE-2014-0508, CVE-2014-0509

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt27
- new version
- security fixes: CVE-2014-0503, CVE-2014-0504

* Fri Feb 21 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt26
- new version
- security fixes: CVE-2014-0498, CVE-2014-0499, CVE-2014-0502

* Wed Feb 05 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt25
- new version
- security fixes: CVE-2014-0497

* Fri Jan 24 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt24
- 11.2.202.335 (x86,x86-64)
- security fixes:
  CVE-2014-0491, CVE-2014-0492

* Thu Jan 09 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt23
- 11.2.202.332 (x86,x86-64)
- security fixes:
  CVE-2013-5331, CVE-2013-5332

* Wed Nov 20 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt22
- 11.2.202.327 (x86,x86-64)
- security fixes:
  CVE-2013-5329, CVE-2013-5330

* Wed Sep 11 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt21
- 11.2.202.310 (x86,x86-64)
- security fixes:
  CVE-2013-3361, CVE-2013-3362, CVE-2013-3363, CVE-2013-5324

* Tue Jul 16 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt20
- 11.2.202.297 (x86,x86-64)
- security fixes: CVE-2013-3344, CVE-2013-3345, CVE-2013-3347

* Mon Jun 17 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt19
- 11.2.202.291 (x86,x86-64)
- security fixes: CVE-2013-3343

* Mon Jun 03 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt18
- 11.2.202.285 (x86,x86-64)
- security fixes:
  CVE-2013-2728, CVE-2013-3324, CVE-2013-3325, CVE-2013-3326,
  CVE-2013-3327, CVE-2013-3328, CVE-2013-3329, CVE-2013-3330,
  CVE-2013-3331, CVE-2013-3332, CVE-2013-3333, CVE-2013-3334,
  CVE-2013-3335

* Thu Apr 11 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt17
- 11.2.202.280 (x86,x86-64)
- security fixes:
  CVE-2013-1378, CVE-2013-1379, CVE-2013-1380, CVE-2013-2555

* Thu Feb 28 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt16
- 11.2.202.273 (x86,x86-64)
- security fixes:
  CVE-2013-0504, CVE-2013-0643, CVE-2013-0648

* Mon Feb 11 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt15
- 11.2.202.262 (x86,x86-64)
- security fixes:
  CVE-2013-0633, CVE-2013-0634

* Fri Jan 11 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt14
- 11.2.202.261 (x86,x86-64)
- security fixes:
  CVE-2013-0630

* Wed Dec 12 2012 Sergey V Turchin <zerg@altlinux.org> 3:11-alt13
- 11.2.202.258 (x86,x86-64)

* Thu Oct 11 2012 Sergey V Turchin <zerg@altlinux.org> 3:11-alt12
- 11.2.202.243 (x86,x86-64)
- security fixes:
  CVE-2012-5248, CVE-2012-5249, CVE-2012-5250, CVE-2012-5251,
  CVE-2012-5252, CVE-2012-5253, CVE-2012-5254, CVE-2012-5255,
  CVE-2012-5256, CVE-2012-5257, CVE-2012-5258, CVE-2012-5259,
  CVE-2012-5260, CVE-2012-5261, CVE-2012-5262, CVE-2012-5263,
  CVE-2012-5264, CVE-2012-5265, CVE-2012-5266, CVE-2012-5267,
  CVE-2012-5268, CVE-2012-5269, CVE-2012-5270, CVE-2012-5271,
  CVE-2012-5272

* Wed Aug 15 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt11
- security fixes:
  CVE-2012-1535

* Wed Jun 13 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt10
- security fixes:
  CVE-2012-2034, CVE-2012-2035, CVE-2012-2036, CVE-2012-2037,
  CVE-2012-2038, CVE-2012-2039, CVE-2012-2040

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt9
- 11.2.202.235 (x86,x86-64)
  CVE-2012-0779

* Mon Apr 02 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt8
- 11.2.202.228 (x86,x86-64)

* Sun Mar 11 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt7
- CVE-2012-0768, CVE-2012-0769

* Thu Feb 16 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt5.M60P.1
- built for M60P

* Thu Feb 16 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt6
- 11.1.102.62 (x86,x86-64)
- security fixes:
  CVE-2012-0751, CVE-2012-0752, CVE-2012-0753, CVE-2012-0754,
  CVE-2012-0755, CVE-2012-0756, CVE-2012-0767

* Thu Dec 01 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt4.M60P.1
- built for M60P

* Thu Dec 01 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt5
- update license text

* Fri Nov 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt3.M60P.1
- built for M60P

* Fri Nov 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt4
- 11.1.102.55 (x86,x86-64)
- security fixes:
  CVE-2011-2445, CVE-2011-2450, CVE-2011-2451, CVE-2011-2452,
  CVE-2011-2453, CVE-2011-2454, CVE-2011-2455, CVE-2011-2456,
  CVE-2011-2457, CVE-2011-2458, CVE-2011-2459, CVE-2011-2460

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt2.M60P.1
- built for M60P

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt3
- 11.0.1.152 (x86,x86-64)

* Thu Oct 06 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt2
- use brp_strip_none instead of set_strip_method

* Mon Sep 26 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt1
- 11.0.1.129 (x86,x86-64)

* Fri Aug 26 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt13
- new version 11.0.1.98(x86)

* Fri Aug 12 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt11.M51.1
- built for M51

* Thu Aug 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt12
- new version 10.3.183.5(x86), 11.0.1.98(x86-64)
- security fixes:
  CVE-2011-2130, CVE-2011-2134, CVE-2011-2135, CVE-2011-2136,
  CVE-2011-2137, CVE-2011-2138, CVE-2011-2139, CVE-2011-2140,
  CVE-2011-2414, CVE-2011-2415, CVE-2011-2416, CVE-2011-2417,
  CVE-2011-2425

* Thu Jul 14 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt11
- new beta 11.0.1.60 (64-bit only)

* Tue Jun 07 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt9.M51.1
- built for M51

* Mon Jun 06 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt10
- new version 10.3.181.22 (32-bit only)

* Sun May 29 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt9
- fix path to LICENSE.txt

* Fri May 20 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt8
- fix desktop-file premissions

* Mon May 16 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt6.M51.1
- build for M51

* Mon May 16 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt7
- package flash-player-properties

* Mon May 16 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt6
- new version 10.3.181.14(x86-32)
- only 32-bit security fixes:
  CVE-2011-0579, CVE-2011-0618, CVE-2011-0619, CVE-2011-0620,
  CVE-2011-0621, CVE-2011-0622, CVE-2011-0623, CVE-2011-0624,
  CVE-2011-0625, CVE-2011-0626, CVE-2011-0627

* Mon Apr 18 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt4.M51.1
- build for M51

* Mon Apr 18 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt5
- new version 10.2.159.1(x86-32)

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt3.M51.1
- build for M51

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt4
- fix build requires

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt2.M51.1
- build for M51

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt3
- new version 10.2.153.1(x86-32)

* Tue Feb 15 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt1.M51.1
- build for M51

* Mon Feb 14 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt2
- new version 10.2.152.27(x86-32)

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 1:10-alt0.M51.1
- built for M51

* Fri Dec 03 2010 Sergey V Turchin <zerg@altlinux.org> 1:10-alt1
- new version
- package different versions for ix86(10.1.102.65) and x86_64(10.3.162.29)

* Thu Sep 30 2010 Sergey V Turchin <zerg@altlinux.org> 10.2.161.23-alt0.M51.1
- built for M51

* Thu Sep 30 2010 Sergey V Turchin <zerg@altlinux.org> 10.2.161.23-alt1
- CVE-2010-2884

* Thu Sep 16 2010 Sergey V Turchin <zerg@altlinux.org> 10.2.161.22-alt0.M51.1
- built for M51

* Thu Sep 16 2010 Sergey V Turchin <zerg@altlinux.org> 10.2.161.22-alt1
- 10.2.161.22 beta
- package 64-bit version too

* Mon Aug 30 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.82.76-alt3
- fix conflicts with i586-%name

* Wed Aug 18 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.82.76-alt2
- don't package 64-bit version

* Wed Aug 11 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.82.76-alt0.M51.1
- built for M51

* Wed Aug 11 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.82.76-alt1
- only 32-bit new version
- CVE-2010-0209 CVE-2010-2188 CVE-2010-2213 CVE-2010-2214 CVE-2010-2215
  CVE-2010-2216

* Mon Jun 14 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.53.64-alt0.M51.1
- built for M51

* Mon Jun 14 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.53.64-alt1
- only 32-bit new version (ALT#17168)
- only 32-bit fixes CVE-2008-4546 CVE-2009-3793 CVE-2010-1297 CVE-2010-2160
  CVE-2010-2161 CVE-2010-2162 CVE-2010-2163 CVE-2010-2164 CVE-2010-2165
  CVE-2010-2166 CVE-2010-2167 CVE-2010-2169 CVE-2010-2170 CVE-2010-2171
  CVE-2010-2172 CVE-2010-2173 CVE-2010-2174 CVE-2010-2175 CVE-2010-2176
  CVE-2010-2177 CVE-2010-2178 CVE-2010-2179 CVE-2010-2180 CVE-2010-2181
  CVE-2010-2182 CVE-2010-2183 CVE-2010-2184 CVE-2010-2185 CVE-2010-2186
  CVE-2010-2187 CVE-2010-2188 CVE-2010-2189

* Wed Feb 17 2010 Sergey V Turchin <zerg@altlinux.org> 10.0.45.2-alt0.M51.1
- built for M51

* Wed Feb 17 2010 Sergey V Turchin <zerg@altlinux.org> 10.0.45.2-alt1
- new version
- fix requires

* Wed Dec 09 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.42.34-alt0.M51.1
- built for M51

* Wed Dec 09 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.42.34-alt1
- new version

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.32.18-alt4
- fix requires

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.32.18-alt3
- don't use old netscape plugins placement

* Mon Sep 28 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.32.18-alt2
- move to more accessible place

* Tue Aug 11 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.32.18-alt1
- new version

* Thu Jun 25 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.22.87-alt2
- add x86_64 version

* Fri Feb 27 2009 Sergey V Turchin <zerg at altlinux dot org> 10.0.22.87-alt0.M41.1
- built for M41

* Fri Feb 27 2009 Sergey V Turchin <zerg at altlinux dot org> 10.0.22.87-alt1
- security update (SA34012)

* Fri Dec 19 2008 Sergey V Turchin <zerg at altlinux dot org> 10.0.15.3-alt1
- new version
- remove deprecated macroses from specfile

* Fri Oct 31 2008 Sergey V Turchin <zerg at altlinux dot org> 10.0.12.36-alt2
- add libcurl to requires

* Wed Oct 15 2008 Sergey V Turchin <zerg at altlinux dot org> 10.0.12.36-alt1
- new version

* Thu Apr 10 2008 Sergey V Turchin <zerg at altlinux dot org> 9.0.124.0-alt2
- fix src tarball file permissions

* Wed Dec 05 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.115.0-alt1
- new version

* Fri Aug 17 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.48.0-alt3
- fix path to license in desktop-file

* Thu Jul 12 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.48.0-alt2
- add Categories parameter to desktop-file

* Thu Jul 12 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.48.0-alt1
- new version

* Mon Jan 22 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.31.0-alt2
- fix license && package description

* Fri Jan 19 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.31.0-alt1
- release 9.0.31.0

* Thu Oct 26 2006 Sergey V Turchin <zerg at altlinux dot org> 9.0.21.55-alt0.1.beta
- new beta version

* Mon Jun 19 2006 Sergey V Turchin <zerg at altlinux dot org> 7.0.63-alt1
- new version

* Wed Dec 28 2005 Sergey V Turchin <zerg at altlinux dot org> 7.0.61-alt1
- new version

* Thu Jan 06 2005 Alexey Gladkov <legion@altlinux.ru> 7.0.25-alt1.1
- browser-plugins-npapi support added;

* Fri May 28 2004 Sergey V Turchin <zerg at altlinux dot org> 7.0.25-alt1
- new version

* Thu May 27 2004 Sergey V Turchin <zerg at altlinux dot org> 6.0.81-alt2
- fix menu section

* Tue May 25 2004 Sergey V Turchin <zerg at altlinux dot org> 6.0.81-alt1
- new version
- add menufile to show license

* Fri Aug 01 2003 Sergey V Turchin <zerg at altlinux dot org> 6.0.79-alt1
- new version

* Tue Feb 11 2003 Sergey V Turchin <zerg@altlinux.ru> 6.0.69-alt1
- initial spec
