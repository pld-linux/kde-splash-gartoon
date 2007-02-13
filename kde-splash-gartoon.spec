%define		_splash		gartoon
Summary:	KDE splash screen
Summary(pl.UTF-8):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	0.1
Release:	0.2
License:	GPL
Group:		X11/Amusements
Source0:	http://www.kde-look.org/content/files/20031-gartoonss.tar.gz
# Source0-md5:	58fe2ceb5c75b327e1e7a3a2f4f3fdf1
URL:		http://www.kde-look.org/content/show.php?content=20031
Requires:	kdebase-desktop
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gartoon splash screen.

%description -l pl.UTF-8
Ekran startowy gartoon.

%prep
%setup -q -n gartoonss

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

install *.png $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install Theme.rc $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}
