let 
  pkgs = import <nixpkgs> {};
  dockerTools = pkgs.dockerTools;
  nodejs = pkgs.nodejs-8_x;
  app = pkgs.stdenv.mkDerivation {
    name = "application";
    src = ./. ;
    buildInputs = [ nodejs ];
    buildCommand = ''
      cp $src/package.json .
      HOME=$(pwd) npm --no-update-notifier install
      mkdir -p $out
      cp -rf node_modules $out/node_modules
      cp $src/index.js $out/index.js
      fixupPhase
    '';
  };
in

dockerTools.buildImage {
  name = "dockerhp/app";
  tag = "nix";
  contents = app;
  config = {
    Cmd = [ "${nodejs}/bin/node" "${app}/index.js" ];
  };
}

