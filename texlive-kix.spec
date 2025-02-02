Name:		texlive-kix
Version:	21606
Release:	2
Summary:	Typeset KIX codes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/kix
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kix.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kix.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Implements KIX codes as used by the Dutch PTT for bulk mail
addressing. (Royal Mail 4 State Code.) KIX is a registered
trade mark of PTT Post Holdings B. V.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/kix
%doc %{_texmfdistdir}/doc/latex/kix

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
