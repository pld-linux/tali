Summary:	GNOME Tali
Summary(pl.UTF-8):	Tali dla GNOME
Name:		tali
Version:	40.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/tali/40/%{name}-%{version}.tar.xz
# Source0-md5:	4df75a5177aba2b721add569f472c4fb
URL:		https://wiki.gnome.org/Apps/Tali
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools
BuildRequires:	gtk+3-devel >= 3.16.0
BuildRequires:	libgnome-games-support-devel >= 1
BuildRequires:	meson >= 0.37.1
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	yelp-tools
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	gtk+3 >= 3.16.0
Requires:	hicolor-icon-theme
Provides:	gnome-games-gtali = 1:%{version}-%{release}
Obsoletes:	gnome-games-gtali < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Poker-style dice game.

%description -l pl.UTF-8
Gra w kości w pokerowym stylu.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/tali
%{_datadir}/glib-2.0/schemas/org.gnome.Tali.gschema.xml
%{_datadir}/metainfo/org.gnome.Tali.appdata.xml
%{_datadir}/tali
%{_desktopdir}/org.gnome.Tali.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Tali.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Tali-symbolic.svg
%{_mandir}/man6/tali.6*
