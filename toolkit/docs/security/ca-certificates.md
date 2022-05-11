# SSL CA certificates management

- [SSL CA certificates management](#ssl-ca-certificates-management)
  - [The `ca-certificates` package](#the-ca-certificates-package)
  - [Certificate locations](#certificate-locations)
  - [Legacy certificates support](#legacy-certificates-support)
  - [Tips and tricks](#tips-and-tricks)

## The `ca-certificates` package

This package contains the basic SSL CA certificates available to use on all images. The certificates are split into two sub packages:

- `ca-certificates-base` - package containing the minimal set of certificates required by the package management tools to authenticate the package repositories.
- `ca-certificates` - package containing a collection of CAs trusted through the [Microsoft Trusted Root Program](https://docs.microsoft.com/en-us/security/trusted-root/release-notes). For exact version information please consult the [`ca-certificates.spec`](../../../SPECS/ca-certificates/ca-certificates.spec). Installing this package will automatically pull in `ca-certificates-base`.

In addition to the certificates, the `ca-certificates-tools` package provides tooling for [installation of custom certificates](#custom-configuration-of-the-ca-certificates).

## Certificate locations

The directory /etc/pki/ca-trust/source/ contains CA certificates and
trust settings in the PEM file format. The trust settings found here will be
interpreted with a high priority - higher than the ones found in
/usr/share/pki/ca-trust-source/.

**QUICK HELP 1**: to add a certificate in the simple PEM or DER file format to the list of CAs trusted on the system:

1. Copy the certificate into `/etc/pki/ca-trust/source/anchors/`.
2. Run `update-ca-trust`.

**QUICK HELP 2**: if your certificate is in the extended BEGIN TRUSTED file format (which may contain distrust/blacklist trust flags, or trust flags for usages other than TLS) then:

1. Copy the certificate into `/etc/pki/ca-trust/source/`.
2. Run `update-ca-trust`.

Please refer to the [update-ca-trust manual](../../../SPECS/ca-certificates/update-ca-trust.8.txt) for more details.

## Legacy certificates support

Some application may not be able to use the certificates in the bundled format under `/etc/pki/tls/certs/ca-bundle.crt` and require the bundle to be extracted to a single-cert-per-file format in the same directory. In those cases the `ca-certificates-legacy` subpackage will take care of automatically extracting and updating the single certificates whenever any of the other `ca-certificates` subpackages modifying the bundle (e.g. `ca-certificates` or `ca-certificates-base`) get installed, removed, or updated.

**WARNING**: after manually installing a trust anchor **and** running `update-ca-trust`, the user must also run `sudo bundle2pem.sh /etc/pki/tls/certs/ca-bundle.crt` in order for the new certificates to be available in the legacy format. The `bundle2pem.sh` script is installed with the `ca-certificates-legacy` subpackage.

## Tips and tricks

To get additional debug output when using p11-kit's `trust` or `p11-kit` commands set the `P11_KIT_DEBUG` environment variable and to not specify the `-v` parameter.

``` bash
export P11_KIT_DEBUG=all
export DEST=/etc/pki/ca-trust/extracted
sudo -E /usr/bin/p11-kit extract --format=pem-bundle --filter=ca-anchors --overwrite --comment --purpose server-auth $DEST/pem/tls-ca-bundle.pem
```
