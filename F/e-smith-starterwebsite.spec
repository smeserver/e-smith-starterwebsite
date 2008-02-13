Summary: e-smith server and gateway - starterwebsite module
%define name e-smith-starterwebsite
Name: %{name}
%define version 1.0.0
%define release 3
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-starterwebsite-1.0.0.tags2general.patch2
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base
Requires: e-smith-formmagick >= 1.4.0-9
BuildRequires: e-smith-devtools >= 1.13.1-03
AutoReqProv: no

%description
e-smith server and gateway software - starterwebsite module.

%changelog
* Wed Feb 13 2008 Stephen Noble <support@dungog.net> 1.0.0-3
- Remove <base> tags now in general [SME: 3922]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Thu Mar 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-01
- Roll stable stream version. [SME: 1016]

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
