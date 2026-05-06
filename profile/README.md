# Swift Foundations

Composed Swift building blocks for production systems — HTTP servers and clients, markup and serialization, crypto and authentication, database connectivity, observability, rendering, language tooling, and platform integration. 137 packages.

## Part of Swift Institute

swift-foundations is the Layer 3 organization within the [Swift Institute](https://github.com/swift-institute) ecosystem — composed building blocks that depend on swift-primitives (Layer 1, atomic) and swift-standards (Layer 2, specifications). The packages here build on the lower layers without forming an internal tier ordering of their own. See the [ecosystem overview](https://github.com/swift-institute) and [layered architecture](https://swift-institute.org) for context.

## Packages

137 packages organized by capability domain. Each repo links directly:

### HTTP and web

[swift-http](https://github.com/swift-foundations/swift-http) · [swift-http2](https://github.com/swift-foundations/swift-http2) · [swift-http3](https://github.com/swift-foundations/swift-http3) · [swift-http-body](https://github.com/swift-foundations/swift-http-body) · [swift-http-compression](https://github.com/swift-foundations/swift-http-compression) · [swift-http-content-negotiation](https://github.com/swift-foundations/swift-http-content-negotiation) · [swift-http-cookies](https://github.com/swift-foundations/swift-http-cookies) · [swift-http-cors](https://github.com/swift-foundations/swift-http-cors) · [swift-http-etag](https://github.com/swift-foundations/swift-http-etag) · [swift-http-headers](https://github.com/swift-foundations/swift-http-headers) · [swift-http-range](https://github.com/swift-foundations/swift-http-range) · [swift-http-redirect](https://github.com/swift-foundations/swift-http-redirect) · [swift-http-routing](https://github.com/swift-foundations/swift-http-routing) · [swift-websocket](https://github.com/swift-foundations/swift-websocket)

### Networking

[swift-domain-name-system](https://github.com/swift-foundations/swift-domain-name-system) · [swift-dns-cache](https://github.com/swift-foundations/swift-dns-cache) · [swift-ip-address](https://github.com/swift-foundations/swift-ip-address) · [swift-sockets](https://github.com/swift-foundations/swift-sockets) · [swift-transport-layer-security](https://github.com/swift-foundations/swift-transport-layer-security) · [swift-uri](https://github.com/swift-foundations/swift-uri)

### Markup and serialization

[swift-html](https://github.com/swift-foundations/swift-html) · [swift-css](https://github.com/swift-foundations/swift-css) · [swift-svg](https://github.com/swift-foundations/swift-svg) · [swift-pdf](https://github.com/swift-foundations/swift-pdf) · [swift-xml](https://github.com/swift-foundations/swift-xml) · [swift-json](https://github.com/swift-foundations/swift-json) · [swift-yaml](https://github.com/swift-foundations/swift-yaml) · [swift-toml](https://github.com/swift-foundations/swift-toml) · [swift-plist](https://github.com/swift-foundations/swift-plist) · [swift-msgpack](https://github.com/swift-foundations/swift-msgpack) · [swift-protobuf](https://github.com/swift-foundations/swift-protobuf) · [swift-concise-binary-object-representation](https://github.com/swift-foundations/swift-concise-binary-object-representation) · [swift-rss](https://github.com/swift-foundations/swift-rss) · [swift-json-feed](https://github.com/swift-foundations/swift-json-feed) · [swift-epub](https://github.com/swift-foundations/swift-epub) · [swift-email](https://github.com/swift-foundations/swift-email) · [swift-emailaddress](https://github.com/swift-foundations/swift-emailaddress)

### Crypto and authentication

[swift-crypto](https://github.com/swift-foundations/swift-crypto) · [swift-certificates](https://github.com/swift-foundations/swift-certificates) · [swift-json-web-encryption](https://github.com/swift-foundations/swift-json-web-encryption) · [swift-json-web-key](https://github.com/swift-foundations/swift-json-web-key) · [swift-json-web-signature](https://github.com/swift-foundations/swift-json-web-signature) · [swift-json-web-token](https://github.com/swift-foundations/swift-json-web-token) · [swift-oauth](https://github.com/swift-foundations/swift-oauth) · [swift-oauth-pkce](https://github.com/swift-foundations/swift-oauth-pkce) · [swift-basic-auth](https://github.com/swift-foundations/swift-basic-auth) · [swift-digest-auth](https://github.com/swift-foundations/swift-digest-auth) · [swift-password](https://github.com/swift-foundations/swift-password) · [swift-time-based-one-time-password](https://github.com/swift-foundations/swift-time-based-one-time-password) · [swift-cross-site-request-forgery](https://github.com/swift-foundations/swift-cross-site-request-forgery) · [swift-secrets](https://github.com/swift-foundations/swift-secrets)

### Database and persistence

[swift-sql](https://github.com/swift-foundations/swift-sql) · [swift-sql-postgres](https://github.com/swift-foundations/swift-sql-postgres) · [swift-sql-mysql](https://github.com/swift-foundations/swift-sql-mysql) · [swift-sql-sqlite](https://github.com/swift-foundations/swift-sql-sqlite) · [swift-redis](https://github.com/swift-foundations/swift-redis) · [swift-keyvalue](https://github.com/swift-foundations/swift-keyvalue) · [swift-pool-connections](https://github.com/swift-foundations/swift-pool-connections)

### Concurrency

[swift-async](https://github.com/swift-foundations/swift-async) · [swift-clocks](https://github.com/swift-foundations/swift-clocks) · [swift-time](https://github.com/swift-foundations/swift-time) · [swift-threads](https://github.com/swift-foundations/swift-threads) · [swift-executors](https://github.com/swift-foundations/swift-executors) · [swift-scheduler](https://github.com/swift-foundations/swift-scheduler) · [swift-effects](https://github.com/swift-foundations/swift-effects) · [swift-graceful-shutdown](https://github.com/swift-foundations/swift-graceful-shutdown) · [swift-pubsub](https://github.com/swift-foundations/swift-pubsub) · [swift-signal](https://github.com/swift-foundations/swift-signal)

### I/O and filesystem

[swift-io](https://github.com/swift-foundations/swift-io) · [swift-file-system](https://github.com/swift-foundations/swift-file-system)

### Compilation and language tooling

[swift-compiler](https://github.com/swift-foundations/swift-compiler) · [swift-driver](https://github.com/swift-foundations/swift-driver) · [swift-runtime](https://github.com/swift-foundations/swift-runtime) · [swift-syntax](https://github.com/swift-foundations/swift-syntax) · [swift-source](https://github.com/swift-foundations/swift-source) · [swift-symbol](https://github.com/swift-foundations/swift-symbol) · [swift-lexer](https://github.com/swift-foundations/swift-lexer) · [swift-parsers](https://github.com/swift-foundations/swift-parsers) · [swift-diagnostic](https://github.com/swift-foundations/swift-diagnostic) · [swift-diagnostics](https://github.com/swift-foundations/swift-diagnostics) · [swift-intermediate-representation](https://github.com/swift-foundations/swift-intermediate-representation) · [swift-loader](https://github.com/swift-foundations/swift-loader) · [swift-abstract-syntax-tree](https://github.com/swift-foundations/swift-abstract-syntax-tree)

### Platform integration

[swift-darwin](https://github.com/swift-foundations/swift-darwin) · [swift-linux](https://github.com/swift-foundations/swift-linux) · [swift-windows](https://github.com/swift-foundations/swift-windows) · [swift-posix](https://github.com/swift-foundations/swift-posix)

### Rendering

[swift-html-render](https://github.com/swift-foundations/swift-html-render) · [swift-css-html-render](https://github.com/swift-foundations/swift-css-html-render) · [swift-pdf-render](https://github.com/swift-foundations/swift-pdf-render) · [swift-pdf-html-render](https://github.com/swift-foundations/swift-pdf-html-render) · [swift-svg-render](https://github.com/swift-foundations/swift-svg-render) · [swift-markdown-html-render](https://github.com/swift-foundations/swift-markdown-html-render) · [swift-user-interface-render](https://github.com/swift-foundations/swift-user-interface-render) · [swift-user-interface](https://github.com/swift-foundations/swift-user-interface)

### Application infrastructure

[swift-backend](https://github.com/swift-foundations/swift-backend) · [swift-config](https://github.com/swift-foundations/swift-config) · [swift-config-toml](https://github.com/swift-foundations/swift-config-toml) · [swift-config-yaml](https://github.com/swift-foundations/swift-config-yaml) · [swift-environment](https://github.com/swift-foundations/swift-environment) · [swift-feature-flags](https://github.com/swift-foundations/swift-feature-flags) · [swift-migrations](https://github.com/swift-foundations/swift-migrations) · [swift-identities](https://github.com/swift-foundations/swift-identities) · [swift-translating](https://github.com/swift-foundations/swift-translating) · [swift-locale](https://github.com/swift-foundations/swift-locale)

### Observability

[swift-log](https://github.com/swift-foundations/swift-log) · [swift-log-json](https://github.com/swift-foundations/swift-log-json) · [swift-metrics](https://github.com/swift-foundations/swift-metrics) · [swift-tracing](https://github.com/swift-foundations/swift-tracing) · [swift-health](https://github.com/swift-foundations/swift-health) · [swift-observations](https://github.com/swift-foundations/swift-observations)

### Utility

[swift-strings](https://github.com/swift-foundations/swift-strings) · [swift-paths](https://github.com/swift-foundations/swift-paths) · [swift-numerics](https://github.com/swift-foundations/swift-numerics) · [swift-decimals](https://github.com/swift-foundations/swift-decimals) · [swift-systems](https://github.com/swift-foundations/swift-systems) · [swift-witnesses](https://github.com/swift-foundations/swift-witnesses) · [swift-defunctionalize](https://github.com/swift-foundations/swift-defunctionalize) · [swift-dual](https://github.com/swift-foundations/swift-dual) · [swift-copy-on-write](https://github.com/swift-foundations/swift-copy-on-write) · [swift-least-recently-used](https://github.com/swift-foundations/swift-least-recently-used) · [swift-time-to-live](https://github.com/swift-foundations/swift-time-to-live) · [swift-process](https://github.com/swift-foundations/swift-process) · [swift-console](https://github.com/swift-foundations/swift-console) · [swift-command-line](https://github.com/swift-foundations/swift-command-line) · [swift-color](https://github.com/swift-foundations/swift-color) · [swift-ascii](https://github.com/swift-foundations/swift-ascii) · [swift-dependencies](https://github.com/swift-foundations/swift-dependencies) · [swift-dependency-analysis](https://github.com/swift-foundations/swift-dependency-analysis) · [swift-tests](https://github.com/swift-foundations/swift-tests) · [swift-testing](https://github.com/swift-foundations/swift-testing) · [swift-application-binary-interface](https://github.com/swift-foundations/swift-application-binary-interface) · [swift-type](https://github.com/swift-foundations/swift-type) · [swift-module](https://github.com/swift-foundations/swift-module) · [swift-kernel](https://github.com/swift-foundations/swift-kernel) · [swift-memory](https://github.com/swift-foundations/swift-memory) · [swift-random](https://github.com/swift-foundations/swift-random)

All 137 packages are public.

## How to use a package

Each package is a separate Swift Package Manager package with its own GitHub repo — there is no umbrella swift-foundations package. To depend on a package, use its individual repository URL:

```swift
dependencies: [
    .package(url: "https://github.com/swift-foundations/swift-http.git", from: "0.1.0")
]
```

See each package's README for current version, target configuration, and (for multi-product packages) umbrella-vs-variant product choices.

## Status

Initial public alpha. The ecosystem is being released repository by repository over the coming weeks. Most packages are at status `active--development`.

Maintained by [Coen ten Thije Boonkkamp](https://github.com/coenttb) — contributions welcome via pull request to individual package repositories.

## License

All packages use the Apache License 2.0.
