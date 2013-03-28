Summary:	GNOME Tali
Summary(pl.UTF-8):	Tali dla GNOME
Name:		tali
Version:	3.8.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/tali/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	e9f1389df409247074aa24b329888482
URL:		https://live.gnome.org/Tali
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	pkgconfig
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Provides:	gnome-games-gtali = 1:%{version}-%{release}
Obsoletes:	gnome-games-gtali < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _gamesdir       %{_localstatedir}/games

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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT%{_gamesdir}/gtali.scores

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

if [ ! -f %{_gamesdir}/gtali.scores ]; then
	touch %{_gamesdir}/gtali.scores
	chown root:games %{_gamesdir}/gtali.scores
	chmod 664 %{_gamesdir}/gtali.scores
fi

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(2755,root,root) %{_bindir}/tali
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%attr(664,root,games) %ghost %{_gamesdir}/gtali.*
%{_datadir}/glib-2.0/schemas/org.gnome.tali.gschema.xml
%{_datadir}/tali
%{_desktopdir}/gtali.desktop
%{_mandir}/man6/tali.6*
