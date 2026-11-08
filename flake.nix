{
  description = "SMS and iMessage companion for the Bark agent";

  nixConfig = {
    extra-substituters = [ "https://scottylabs.cachix.org" ];
    extra-trusted-public-keys = [
      "scottylabs.cachix.org-1:hajjEX5SLi/Y7yYloiXTt2IOr3towcTGRhMh1vu6Tjg="
    ];
  };

  inputs = {
    scottylabs.url = "git+https://git.cmu.dev/ScottyLabs/kennel";
    nixpkgs.follows = "scottylabs/nixpkgs";
    flake-parts.follows = "scottylabs/flake-parts";
  };

  outputs =
    inputs:
    inputs.flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [ inputs.scottylabs.flakeModules.default ];
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "aarch64-darwin"
      ];

      perSystem =
        {
          pkgs,
          lib,
          helpers,
          ...
        }:
        {
          scottylabs = {
            project.name = "cmugpt-sms-surface";

            python = {
              enable = true;
              package = pkgs.python312;
            };

            processes.sms-surface = {
              run = "PORT=8000 exec secretspec run -P dev -- uv run sms-surface";
              ready = "${lib.getExe pkgs.curl} -sf http://localhost:8000/api/health";
            };
          };

          services.sms-surface = {
            package = lib.addMetaAttrs { mainProgram = "sms-surface"; } (
              helpers.buildPythonService {
                src = ./.;
                python = pkgs.python312;
              }
            );
          };
        };
    };
}
