### Installation

1. Install nvm following the instructions from [nvm docs](https://github.com/nvm-sh/nvm)
2. Run `nvm install` in order to install correct version of nodejs. Afterwards, use `nvm use` to switch between node versions.
3. Run `npm i`
4. Run `make dev`
5. Open [local stand](https://firework:5173/) in browser

### Local setup with remote (sandbox) backend
CORS, CSRF and other stuff is properly configured on backend side.
Note: Sandbox has http basic auth and Chrome has several issues with that. Use Firefox for connecting to sandbox.
1. Add `127.0.0.1 firework` to `/etc/hosts`
2. Add `.env` file wit the following content:
```text
VITE_BACKEND_HOST=http://localhost:8080
```
3. `make dev`
4. Open https://firework:5173/ in Firefox and accept message about invalid SSL certificate
- Note: make sure url is `https` and port is `:5173`. Otherwise you might face CORS issues.
