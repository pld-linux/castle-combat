Summary:	castle-combat - enclose land and destroy your opponent's castle
Summary(pl):	castle-combat - zdob±d¼ ziemiê i zniszcz zamki przeciwnika
Name:		castle-combat
Version:	0.7.4
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://user.cs.tu-berlin.de/~karlb/castle-combat/%{name}-%{version}.tar.gz
# Source0-md5:	1cf225fbcfbee2b9a00757609fd054bb
URL:		http://user.cs.tu-berlin.de/~karlb/castle-combat/
Patch0:		%{name}-SDL_net.patch
BuildRequires:	SDL-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
castle-combat is a game where up to four players build castle walls,
place cannons inside these walls, and shoot at the walls of their
enemy(s). If a player can't build a complete wall around one of his
castles, he loses. The last surviving player wins.

%description -l pl
castle-combat to gra, w której do czterech graczy buduje zamkowe mury,
ustawia nich armaty i strzela w mury swoich wrogów. Je¿eli gracz nie
mo¿e otoczyæ ani jednego ze swoich zamków murami przegrywa. Wygrywa
ostatni, który przetrwa.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/castle-combat
%{_mandir}/man6/*
