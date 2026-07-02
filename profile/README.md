# Swift Foundations

Composed Swift building blocks for production systems — Layer 3 of the [Swift Institute](https://github.com/swift-institute) ecosystem.

## What this is

Packages that compose the lower layers into working systems: HTTP and networking, markup and serialization, cryptography and authentication, database connectivity, I/O and filesystem, rendering, observability, and platform integration. Every package builds on [swift-primitives](https://github.com/swift-primitives) (atomic building blocks) and [swift-standards](https://github.com/swift-standards) (specification implementations), and carries the same discipline throughout: typed throws end-to-end, strict memory safety, one repo per package.

## Start here

| Package | What it gives you |
|---|---|
| [swift-pdf](https://github.com/swift-foundations/swift-pdf) | PDF document generation from HTML views and Markdown, authored with a result-builder DSL |
| [swift-html](https://github.com/swift-foundations/swift-html) | Type-safe HTML, CSS, and SVG generation, grounded in the WHATWG and W3C specifications |
| [swift-file-system](https://github.com/swift-foundations/swift-file-system) | Typed filesystem operations — scoped handles, atomic writes, zero-copy reads |
| [swift-io](https://github.com/swift-foundations/swift-io) | High-performance async I/O executor that isolates blocking syscalls from Swift's cooperative pool |
| [swift-linter](https://github.com/swift-foundations/swift-linter) | SwiftSyntax-based AST linting with a CLI, SARIF output, and a reusable CI workflow |

## Browse everything

The [repositories tab](https://github.com/orgs/swift-foundations/repositories) lists every package with its description. Narrow it down:

[http](https://github.com/orgs/swift-foundations/repositories?q=http) · [html](https://github.com/orgs/swift-foundations/repositories?q=html) · [css](https://github.com/orgs/swift-foundations/repositories?q=css) · [svg](https://github.com/orgs/swift-foundations/repositories?q=svg) · [pdf](https://github.com/orgs/swift-foundations/repositories?q=pdf) · [json](https://github.com/orgs/swift-foundations/repositories?q=json) · [sql](https://github.com/orgs/swift-foundations/repositories?q=sql) · [render](https://github.com/orgs/swift-foundations/repositories?q=render) · [log](https://github.com/orgs/swift-foundations/repositories?q=log) · [config](https://github.com/orgs/swift-foundations/repositories?q=config)

## How to use a package

Each package is a separate Swift Package Manager package with its own repository — there is no umbrella swift-foundations package:

```swift
dependencies: [
    .package(url: "https://github.com/swift-foundations/swift-html.git", from: "0.1.0")
]
```

See each package's README for current products, traits, and platform support.

## Status

Public alpha. Packages are released repository by repository; most are at status `active--development`.

Maintained by [Coen ten Thije Boonkkamp](https://github.com/coenttb) — contributions welcome via pull request.

## License

All packages use the Apache License 2.0.
