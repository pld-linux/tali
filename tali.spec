Summary:	GNOME Tali
Summary(pl.UTF-8):	Tali dla GNOME
Name:		tali
Version:	3.16.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/tali/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	af4296b252752e96f9f4014ebbe4b75a
URL:		https://wiki.gnome.org/Apps/Tali
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.15.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	pkgconfig
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	gtk+3 >= 3.15.0
Requires:	hicolor-icon-theme
Requires:	librsvg >= 2.32.0
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
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_datadir}/appdata/tali.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.tali.gschema.xml
%{_datadir}/tali
%{_iconsdir}/hicolor/*x*/apps/tali.png
%{_iconsdir}/hicolor/scalable/apps/tali.svg
%{_iconsdir}/hicolor/symbolic/apps/tali-symbolic.svg
%{_desktopdir}/tali.desktop
%{_mandir}/man6/tali.6*
