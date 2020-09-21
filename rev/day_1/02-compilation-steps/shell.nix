with import <nixpkgs> {};
mkShell {
  hardeningDisable = [
    "format"
  ];
  shellHook = ''
    export hardeningDisable=format
  '';
  nativeBuildInputs = with buildPackages; [
    glibc
    gnumake
  ];
}
