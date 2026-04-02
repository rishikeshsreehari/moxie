# FormBeep landing page repo copy/UX audit (repo-grounded)

Scope: /root/moxie/formbeep/landing (partials + index). Focused on exact, paste-ready replacements with file + section pointers. 

Key accuracy check:
- **“Free Forever” is inaccurate** given pricing shows a capped free plan (15 notifications/month). Replace “Free Forever” and “Free forever plan” claims with precise free-plan language.

---

## 10 exact improvements (file + location + replacement blocks)

### 1) Hero trust line: replace “Free Forever” with accurate free-tier cap
**File:** `landing/layouts/partials/hero.html` — `.hero-trust`

**Current:**
```html
<span class="trust-item-v1">Free Forever</span>
```

**Replace with:**
```html
<span class="trust-item-v1">Free plan: 15 alerts/mo</span>
```

---

### 2) Hero CTA: make free tier explicit (reduces ambiguity)
**File:** `landing/layouts/partials/hero.html` — `.hero-actions` CTA

**Current:**
```html
Get FREE Alerts
```

**Replace with:**
```html
Start free — 15 alerts/mo
```

---

### 3) Hero subheadline: tighten benefit + add “any form” clarity
**File:** `landing/layouts/partials/hero.html` — `.hero-sub`

**Current:**
```html
Get a WhatsApp notification <span class="hero-highlight">the moment</span> someone submits — before they move on to a competitor.
```

**Replace with:**
```html
Get a WhatsApp alert <span class="hero-highlight">the moment</span> someone submits any form — before they move on.
```

---

### 4) “FormBeep IS” list: remove vague “plug-and-forget,” add concrete outcome
**File:** `landing/layouts/partials/what-it-is.html` — `.is-items`

**Current:**
```html
<li>A notification layer for your existing forms</li>
<li>One line of code</li>
<li>Instant WhatsApp alerts</li>
<li>A plug-and-forget tool</li>
```

**Replace with:**
```html
<li>A notification layer for your existing forms</li>
<li>One line of code (no form changes)</li>
<li>Instant WhatsApp alerts</li>
<li>Set it once, get alerts forever</li>
```

---

### 5) How-it-works Step 1: clarify no Business API needed
**File:** `landing/layouts/partials/how-it-works.html` — Step 1 description

**Current:**
```html
<p class="simple-step-desc">Scan a QR code and send one message. That's the entire verification.</p>
```

**Replace with:**
```html
<p class="simple-step-desc">Scan a QR code and send one message. No WhatsApp Business API or extra setup.</p>
```

---

### 6) How-it-works Step 2: sharpen compatibility + remove “anything” fluff
**File:** `landing/layouts/partials/how-it-works.html` — Step 2 description

**Current:**
```html
<p class="simple-step-desc">Paste this code to your website. Works with any platform — WordPress, Wix, Webflow, Carrd, static HTML, anything.</p>
```

**Replace with:**
```html
<p class="simple-step-desc">Paste this code to your website. Works with WordPress, Wix, Webflow, Carrd, and any HTML form.</p>
```

---

### 7) FAQ support email: fix to canonical address
**File:** `landing/layouts/partials/faq.html` — “I'm not able to configure FormBeep.”

**Current:**
```html
<p>Shoot us an email at support@formbeep.com or message rishikeshs on Discord. We'll help you get set up.</p>
```

**Replace with:**
```html
<p>Shoot us an email at hello@formbeep.com or message rishikeshs on Discord. We'll help you get set up.</p>
```

---

### 8) FAQ reliability answer: remove unrealistic “99.99% chance” phrasing
**File:** `landing/layouts/partials/faq.html` — “If FormBeep fails, will it affect my leads?”

**Current:**
```html
<p>99.99% chance it won't fail. FormBeep is built on Cloudflare's edge network and scales automatically. But even in that one-in-a-million scenario, your form works as usual. FormBeep never touches your form's original submit action. It just acts as a middle layer that reads the data and sends it to WhatsApp.</p>
```

**Replace with:**
```html
<p>Even if FormBeep is down, your form still works as usual. FormBeep never changes your form’s submit action — it only reads the submission and forwards it to WhatsApp.</p>
```

---

### 9) Comparison section: make proof + outcome more specific (reduce hand-wavy line)
**File:** `landing/layouts/partials/email-vs-whatsapp.html` — comparison footer

**Current:**
```html
<p class="comparison-tagline">FormBeep makes sure you know instantly.</p>
```

**Replace with:**
```html
<p class="comparison-tagline">FormBeep puts new leads in your pocket within seconds.</p>
```

---

### 10) Final CTA subtext: fix “Free forever” + reinforce free plan cap
**File:** `landing/layouts/index.html` — FINAL CTA `.cta-subtext`

**Current:**
```html
<p class="cta-subtext">Free forever plan. No credit card. 2-minute setup.</p>
```

**Replace with:**
```html
<p class="cta-subtext">Free plan includes 15 alerts/month. No credit card. 2-minute setup.</p>
```

---

## Notes
- **Accuracy fix is mandatory**: “Free Forever” copy conflicts with pricing limits (15 notifications/month). Adjusted in hero trust line + final CTA to avoid misrepresentation.
- All replacements are repo-grounded and can be applied without design changes.
