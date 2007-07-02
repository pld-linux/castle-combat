Summary:	castle-combat - enclose land and destroy your opponent's castle
Summary(pl.UTF-8):	castle-combat - zdobądź ziemię i zniszcz zamki przeciwnika
Name:		castle-combat
Version:	0.8.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/castle-combat/%{name}-%{version}.tar.gz
# Source0-md5:	63380e9fc3d4d9de780b3cc52c822ea6
URL:		http://user.cs.tu-berlin.de/~karlb/castle-combat/
BuildRequires:	python-Numeric
BuildRequires:	python-TwistedCore
BuildRequires:	python-pygame-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
castle-combat is a game where up to four players build castle walls,
place cannons inside these walls, and shoot at the walls of their
enemy(s). If a player can't build a complete wall around one of his
castles, he loses. The last surviving player wins.

%description -l pl.UTF-8
castle-combat to gra, w której do czterech graczy buduje zamkowe mury,
ustawia na nich armaty i strzela w mury swoich wrogów. Jeżeli gracz
nie może otoczyć ani jednego ze swoich zamków murami przegrywa.
Wygrywa ostatni, który przetrwa.

%prep
%setup -q
%{__sed} -i 's@src@%{py_sitescriptdir}/%{name}/src@' castle-combat.py
%{__sed} -i 's@"data"@"%{py_sitescriptdir}/%{name}/data"@' src/common.py

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

cp -r data $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}
cp -r src $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
