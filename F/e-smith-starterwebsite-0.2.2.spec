Summary: e-smith server and gateway - starterwebsite module
%define name e-smith-starterwebsite
Name: %{name}
%define version 0.2.2
%define release 02
Version: %{version}
Release: %{release}
License: GPL
Vendor: Mitel Networks Corporation
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-starterwebsite-0.2.2-GPL.patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base
AutoReqProv: no

%description
e-smith server and gateway software - starterwebsite module.

%changelog
* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 0.2.2-02
- Add COPYING file

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [0.2.2-01]
- Remove L10Ns from base packages [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [0.2.1-01]
- New dev stream before relocating L10Ns

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [0.2.0-04]
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [0.2.0-03]
- And add the correct file to the correct package [SF: 1293325]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [0.2.0-02]
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [0.2.0-01]
- Changing version to stable stream number - 0.2.0

* Wed May  7 2003 Lijie Deng <lijied@e-smith.com>
- [0.1.0-04]
- Add fr and es lexicon for starterwebsite [lijied 3793]

* Mon Apr  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.0-03]
- Removed emacs leftovers [gordonr 8073]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [0.1.0-02]
- Modified the starterwebsite panel order [lijied 7356]
- Split en-us lexicon from panel [lijied 4030]

* Mon Jan 06 2003 Mark Knox <m_knox@mitel.com>
- [0.1.0-01]
- Initial import from e-smith-base [markk 5509]

%prep
%setup
%patch0 -p1

%pre

%post

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > e-smith-%{version}-filelist
echo "%doc COPYING"          >> e-smith-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)
