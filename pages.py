import re, os, subprocess
subprocess.run(['python3','build.py'],check=True,capture_output=True)
h = open('bloom-and-rise-home.html').read()

def cut(a, b):
    i = h.index(a); j = h.index(b, i)
    return h[i:j]

HEAD  = h[:h.index('<main id="main">')]
GREEN = h[h.index('<div class="greenhouse">'):h.index('<script>')]
SCRIPT= h[h.index('<script>'):]

SEC = {
 'hero'    : cut('<header class="hero" id="top">', '<section class="intro">'),
 'intro'   : cut('<section class="intro">', '<section class="meta" id="becoming">'),
 'becoming': cut('<section class="meta" id="becoming">', '<section class="sky" id="sky">'),
 'sky'     : cut('<section class="sky" id="sky">', '<section class="work" id="work">'),
 'work'    : cut('<section class="work" id="work">', '<section class="about" id="about">'),
 'about'   : cut('<section class="about" id="about">', '<section class="shops" id="shops">'),
 'shops'   : cut('<section class="shops" id="shops">', '<section class="contact" id="contact">'),
 'contact' : cut('<section class="contact" id="contact">', '</main>'),
}

from sub import set_social
DESCS = {
 'index.html': 'Therapy for anxiety, identity, body image, depression, and OCD with Roshunda M. Hartison, MEd, LPC. Virtual in TX, VA, and CO, in person in Katy, TX.',
 'feels.html': 'What working with Roshunda feels like: how sessions go, the long middle of change, and the free 15 minute consult. Virtual in TX, VA, and CO, in person in Katy.',
 'about.html': 'Meet Roshunda M. Hartison, MEd, LPC. Sixteen years in mental health, licensed in Texas, Virginia, and Colorado, with in person sessions in Katy, Texas.',
 'workshops.html': 'Chew & Chat and other creative community workshops from Bloom & Rise. Educational, not clinical, and open to participants in any state. Join the interest list.'.replace('&','&amp;'),
 'contact.html': 'Book a free 15 minute consult with Roshunda M. Hartison, MEd, LPC. Virtual therapy in Texas, Virginia, and Colorado, and in person in Katy, Texas.',
}
H1 = {
 'feels.html': 'What therapy with Roshunda feels like',
 'about.html': 'About Roshunda M. Hartison, MEd, LPC',
 'workshops.html': 'Workshops and groups',
 'contact.html': 'Book a free consult',
}
PAGES = {
 'index.html'    : (['hero','intro','becoming','sky'],'Bloom &amp; Rise Therapy | Roshunda M. Hartison, MEd, LPC'),
 'feels.html'    : (['work','contact'],               'What it feels like | Bloom &amp; Rise Therapy'),
 'about.html'    : (['about','contact'],              'About Roshunda | Bloom &amp; Rise Therapy'),
 'workshops.html': (['shops'],                        'Workshops &amp; groups | Bloom &amp; Rise Therapy'),
 'contact.html'  : (['contact'],                      'Book a consult | Bloom &amp; Rise Therapy'),
}

NAVLINKS = [('index.html','Home'),('services.html','Services'),('feels.html','What it feels like'),
            ('about.html','Roshunda'),('workshops.html','Workshops')]

def build_nav(current):
    rows = ''.join('      <a href="%s"%s>%s</a>\n' %
                   (h, ' aria-current="page"' if h == current else '', t)
                   for h, t in NAVLINKS)
    return ('    <div class="nav-r" id="navr">\n' + rows +
            '      <a class="cta" href="contact.html"><span class="dot"></span>Book a consult</a>\n'
            '    </div>')

FOOT_LINKS = '''        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="feels.html">What it feels like</a></li>
          <li><a href="about.html">About Roshunda</a></li>
          <li><a href="workshops.html">Workshops and groups</a></li>
          <li><a href="faq.html">Questions people ask</a></li>
          <li><a href="contact.html">Book a consult</a></li>
        </ul>'''

FOOT_FINE = ('<p class="full">&copy; <span id="yr">2026</span> Bloom &amp; Rise. '
             '<a href="privacy.html">Privacy</a> &middot; '
             '<a href="terms.html">Terms of use</a> &middot; '
             '<a href="good-faith-estimate.html">Good Faith Estimate</a> &middot; '
             '<a href="accessibility.html">Accessibility</a></p>')

def build_foot(green):
    fs = green.index('        <ul>'); fe = green.index('</ul>', fs) + len('</ul>')
    out = green[:fs] + FOOT_LINKS + green[fe:]
    ls = out.index('<p class="full">'); le = out.index('</p>', ls) + 4
    return out[:ls] + FOOT_FINE + out[le:]

PAGECSS = '''
/* inner pages clear the fixed nav */
.page-top{padding-top:clamp(6.5rem,10vw,9rem)}
.nav-r a[aria-current]{color:var(--orange-deep)}
.nav-r a[aria-current]::after{transform:scaleX(1)}
'''

def swap_nav(head, current):
    # the wordmark always returns home, on every page
    head = head.replace('<a class="wordmark" href="#top">',
                        '<a class="wordmark" href="index.html">')
    a = head.index('    <div class="nav-r" id="navr">')
    b = head.index('</div>', head.index('</a>\n    </div>', a)) + len('</div>')
    return head[:a] + build_nav(current) + head[b:]

for fname,(parts,title) in PAGES.items():
    head = HEAD
    head = head.replace('<title>Bloom &amp; Rise — Roshunda M. Hartison, MEd, LPC</title>',
                        '<title>%s</title>' % title)
    head = head.replace('@media (prefers-reduced-motion:reduce){', PAGECSS + '@media (prefers-reduced-motion:reduce){',1)
    # real nav
    head = swap_nav(head, fname)
    head = head.replace('__CANON__', '' if fname == 'index.html' else fname)
    head = set_social(head, title, DESCS[fname])

    body = ''.join(SEC[p] for p in parts)
    if 'hero' not in parts:
        body = '<div class="page-top"><h1 class="sr-only">' + H1[fname] + '</h1>' + body + '</div>'

    out = head + '<main id="main">\n' + body + '</main>\n\n' + build_foot(GREEN) + SCRIPT
    open(fname,'w').write(out)
    print(fname, round(len(out)/1024), 'KB')

import sub
sub.build(HEAD, GREEN, SCRIPT, swap_nav, build_foot)

# ---- 404 page (Cloudflare Pages serves 404.html with a real 404 status)
import re as _re
_s = open('faq.html').read()
_i = _s.index('<main id="main">'); _j = _s.index('</main>')
_body = '''<main id="main">
<header class="pagehead"><div class="shell">
  <p class="kicker">Page not found</p>
  <h1>This page has <i style="color:var(--orange-deep)">moved on.</i></h1>
  <p class="lede">The link may be old or mistyped. Everything is still here.</p>
  <p style="margin-top:2rem"><a class="cta" href="index.html"><span class="dot"></span>Back to the homepage</a></p>
</div></header>
'''
_s = _s[:_i] + _body + _s[_j:]
_s = _re.sub(r'<title>.*?</title>', '<title>Page not found | Bloom &amp; Rise Therapy</title>', _s, count=1)
_s = _re.sub(r'<link rel="canonical"[^>]*>', '<meta name="robots" content="noindex">', _s, count=1)
_s = _s.replace('href="index.html"', 'href="/"').replace('href="', 'href="/').replace('href="//', 'href="/').replace('href="/https', 'href="https').replace('href="/mailto', 'href="mailto').replace('href="/tel', 'href="tel').replace('href="/#', 'href="#').replace('href="/data:', 'href="data:')
open('404.html', 'w').write(_s)
print('404.html', round(len(_s)/1024), 'KB')
