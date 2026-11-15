---
tags: [note, guia]
---

# A Guide to Implementing a Let’s Encrypt Certificate


> …
> 

```bash

# doign system wide isntalation is a mistake - high probabilty of latter being broken.
# sudo apt update
# sudo apt install certbot python3-certbot-nginx -y

sudo apt remove certbot python3-certbot-nginx -y
sudo snap install core
sudo snap refresh core
sudo snap install --classic certbot
sudo ln -sf /snap/bin/certbot /usr/bin/certbot

sudo nginx -t
sudo systemctl reload nginx

sudo certbot --nginx -d bremontix.xyz

# Verify
curl -I https://bremontix.xyz
```

## Certbot

Certbot will:

- Contact Let’s Encrypt
- Prove your domain via HTTP-01 challenge
- Get the certificate
- Automatically edit your Nginx config
- Ask if you want to **redirect HTTP → HTTPS**

## Renewal

> https://github.com/louislam/uptime-kuma
> 

> Let’s Encrypt certs last **90 days**. Certbot installs an automatic systemd timer or cron job. Test it manually:
> 

```bash
sudo certbot renew --dry-run
```

## Certification Agency

> A **Certificate Authority (CA)** is a trusted third-party organization that **issues digital certificates** to prove ownership of a domain or entity.
> 

> The CA’s root certificates are built into operating systems and browsers — that’s why your browser “trusts” an SSL/TLS certificate signed by them.
> 

Providers:

- Let’s Encrypt (free, automated)
- DigiCert
- Sectigo (formerly Comodo)
- GoDaddy
- GlobalSign

## 🏷️ Types of Certificates, a CA Issues

- **DV (Domain Validation)** – Confirms domain ownership (most common, used by Let’s Encrypt).
- **OV (Organization Validation)** – Confirms both domain and organization identity.
- **EV (Extended Validation)** – Strongest validation; used by banks and big institutions.

## 🛠️ How the CA Works?

1. **CSR Submission** – You generate a **Certificate Signing Request (CSR)** on your server (contains your domain and public key).
2. **Validation** – The CA validates you own the domain (via DNS, email, or HTTP challenge).
3. **Certificate Issuance** – The CA signs your certificate with its **private root or intermediate key**.
4. **Installation** – You install the certificate (and chain) on your server (e.g., Nginx).
5. **Trust Chain** – Browsers verify the certificate by checking the chain of trust:
    - Your Certificate → Intermediate CA → Root CA → Trusted by OS/browser.

## References

- https://letsencrypt.org/
- https://certbot.eff.org/
- https://en.wikipedia.org/wiki/Automatic_Certificate_Management_Environment
