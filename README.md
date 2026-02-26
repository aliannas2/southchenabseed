# South Chenab Seed Corporation Website

![Status](https://img.shields.io/badge/status-active-brightgreen)
![AWS S3](https://img.shields.io/badge/Hosting-AWS_S3-orange)
![Tailwind](https://img.shields.io/badge/Styling-TailwindCSS-blue)

This is the public-facing static website for **South Chenab Seed Corporation (PVT) LTD.**, built using HTML5, Vanilla JavaScript, and TailwindCSS via CDN.

It serves as the company’s digital presence, offering information on their seed varieties, leadership team, research facilities, and contact information. The site is optimized for performance and mobile responsiveness.

## 🚀 Live Website
**URL:** [https://southchenabseed.com](https://southchenabseed.com)

---

## 🏗️ Technical Stack
- **Frontend Core**: HTML5, Vanilla Javascript.
- **Styling**: TailwindCSS, FontAwesome.
- **Hosting**: AWS S3 Static Website Hosting.
- **CDN/SSL**: AWS CloudFront & Amazon Certificate Manager (ACM).
- **DNS**: AWS Route53.

## 📂 Project Structure
```text
/
├── index.html              # Main Landing Page
├── gallery.html            # Photography and Facilities Gallery
├── s3_index.html           # CloudFront Entry Point
├── package assets          # Images, Favicons (.jpg, .png)
├── site.webmanifest        # PWA / Manifest file
├── robots.txt              # Search Engine Indexing
├── sitemap.xml             # XML Sitemap
├── generate_favicons.py    # Script used for building icons
└── .gitignore              # Secures AWS credentials and outputs
```

---

## ☁️ Setting Up Cloud Infrastructure & Deployment

The infrastructure utilizes AWS to host static files with high availability.

### 1. File Edits
If you are modifying the website (`index.html`, `gallery.html` or adding images), simply edit the source directly. Because this leverages the Tailwind CDN, there is no Node.js compilation step required.

### 2. AWS S3 Upload
To deploy changes manually:
1. Log into the AWS Console.
2. Navigate to S3 and open the dedicated bucket configured for static web hosting.
3. Upload the modified `.html` files, or new images directly into the bucket.
4. Set permissions correctly to ensure public read access (usually handled by the Bucket Policy).

### 3. CloudFront Cache Invalidation
Whenever you upload changes to S3, visitors might initially see the cached older version. 
1. Open CloudFront in the AWS Console.
2. Select the distribution for `southchenabseed.com`.
3. Go to `Invalidations` -> `Create Invalidation`.
4. Enter `/*` to clear the entire site cache, or specifically target updated paths (like `/index.html`).

---

## 🔒 Security Posture
- This repository purely contains the front-end source code and configuration examples.
- All actual AWS API Keys (`*.csv`), TLS cert payloads, or environment variations are safely ignored via the configured `.gitignore`.
