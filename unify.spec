Summary:	Patch file format translator
Name:		unify
Version:	1.2
Release:	2
Copyright:	freely distributable
Group:		Applications/Text
URL:		http://www.web.us.uu.net/sw/dist/
Source0:	http://www.web.us.uu.net/sw/dist/%{name}-%{version}.tar.gz
Patch0:		unify-warnings.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unify translates a context diff into a unified diff, or vice-versa. It is a
supplement to diffutils and patch.

Install unify if you find one patch format easier to read than the other,
for example if you want to read patch ".rej" files in unified format.

%prep
%setup 	-q
%patch0 -p0

%build
gcc -Wall unify.c -o unify $RPM_OPT_FLAGS

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -m755 unify 	$RPM_BUILD_ROOT%{_bindir}/unify
install unify.1 	$RPM_BUILD_ROOT%{_mandir}/man1/unify.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/unify
%{_mandir}/man1/unify.1*
