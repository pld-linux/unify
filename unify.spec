Summary:	Patch file format translator
Summary(pl.UTF-8):   Narzędzie tłumaczące formaty łat
Name:		unify
Version:	1.2
Release:	4
License:	distributable
Group:		Development/Tools
Source0:	http://www.web.us.uu.net/sw/dist/%{name}-%{version}.tar.gz
# Source0-md5:	cbd2fb1920162314e304c98187049cbc
Patch0:		%{name}-warnings.patch
URL:		http://www.web.us.uu.net/sw/dist/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unify translates a context diff into a unified diff, or vice-versa. It
is a supplement to diffutils and patch.

Install unify if you find one patch format easier to read than the
other, for example if you want to read patch ".rej" files in unified
format.

%description -l pl.UTF-8
unify tłumaczy kontekstowy diff na unified lub odwrotnie. Jest
dodatkiem do pakietów diffutils i patch. Przydaje się np. gdy chcemy
przeczytać pliki .rej w formacie unified.

%prep
%setup -q
%patch0 -p0

%build
%{__cc} %{rpmcflags} %{rpmldflags} -Wall unify.c -o unify

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install unify $RPM_BUILD_ROOT%{_bindir}
install unify.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
