import base64, os

def b64(p, mime='image/webp'):
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(p,'rb').read()).decode())

PORTRAIT = b64('rosh-plate.webp')

# Watercolour plates supplied by the client
HERO_ART   = b64('art-hero.webp')
STAGE_1    = b64('art-stage-1.webp')
STAGE_2    = b64('art-stage-2.webp')
STAGE_3    = b64('art-stage-3.webp')
GREENHOUSE = b64('art-greenhouse.webp')
SUN        = b64('art-sun.webp')

# Continuous line drawing, carried as a CSS mask so it takes the ink colour
HAND       = b64('hand.webp')
# Scattered line butterflies, used as a faint paper texture
FLIT       = b64('flit.webp')
BOTANICAL  = b64('bot.webp')
# Time of day triptych: dawn, midday, dusk
SKY_1      = b64('tod-1.webp')
SKY_2      = b64('tod-2.webp')
SKY_3      = b64('tod-3.webp')

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bloom &amp; Rise — Roshunda M. Hartison, MEd, LPC</title>
<meta name="description" content="Creative therapy for anxiety, identity and self trust, body image, and depression. Online in Texas, Virginia, and Colorado, with in-person coming soon in Texas.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://images.unsplash.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,300..900,0..100,0..1;1,9..144,300..900,0..100,0..1&family=Inter+Tight:ital,wght@0,300;0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<style>
:root{
  /* drawn from the watercolours: monarch orange, leaf green, coneflower pink, morning yellow */
  --orange:#D9762F; --orange-deep:#B4551C; --orange-lit:#E8934A;
  --leaf:#5E7A4F; --leaf-deep:#9A4413; --leaf-soft:#A8BE9B;
  /* deep coneflower plum, pulled from the petals in the artwork */
  --plum:#5F2A46;
  --pink:#C77BA6; --pink-soft:#E6BBD2;
  --sun:#F0D28A; --sun-soft:#F8ECC8;

  /* paper */
  --paper:#F7F0E3; --paper-2:#F1E8D8; --paper-3:#EAE0CC;
  /* tinted papers, each one a whisper of a palette colour */
  --wash-sun:#FBF1D9; --wash-leaf:#EAF0E2; --wash-pink:#F9E9F0;
  --wash-plum:#F2E6EC; --wash-sky:#E6EEF2;
  --bark:#3A3227; --bark-2:#6B6152; --bark-3:#948B7A;

  --maxw:1240px; --gut:clamp(1.25rem,4vw,3.5rem);

  /* set by script from the visitor's own clock; this is the pre dawn value */
  --foot:#43263C; --foot-2:#5F2A46;

  --ink-src:url("__HAND__");
  --flit-src:url("__FLIT__");
  --bot-src:url("__BOTANICAL__");
}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;overflow-x:clip}
body{
  margin:0;background:var(--paper);color:var(--bark);
  font-family:'Inter Tight',system-ui,-apple-system,sans-serif;
  font-size:clamp(16px,1.05vw,18px);line-height:1.62;overflow-x:hidden;
  -webkit-font-smoothing:antialiased;
}
h1,h2,h3{
  font-family:'Fraunces',Georgia,serif;
  font-variation-settings:'SOFT' 55,'WONK' 1,'opsz' 120;
  font-weight:500;line-height:.96;letter-spacing:-.032em;margin:0;text-wrap:balance;
}
h1{font-size:clamp(2.7rem,7.2vw,6.6rem);font-weight:400;line-height:.98}
h2{font-size:clamp(2.1rem,5.2vw,4.4rem)}
h3{font-size:clamp(1.25rem,2vw,1.75rem);letter-spacing:-.02em}
p{margin:0 0 1.15em;max-width:62ch}
a{color:inherit}
img{display:block;max-width:100%}
::selection{background:var(--orange);color:#fff}
:focus-visible{outline:2px solid var(--orange);outline-offset:4px;border-radius:2px}
.shell{width:min(100% - (var(--gut) * 2),var(--maxw));margin-inline:auto}
.skip{position:absolute;left:0;top:0;z-index:500;background:var(--bark);color:var(--paper);padding:1rem 1.5rem;transform:translateY(-120%)}
.skip:focus{transform:none}

.rise{opacity:0;transform:translateY(26px);transition:opacity .9s cubic-bezier(.2,.7,.3,1),transform .9s cubic-bezier(.2,.7,.3,1)}
.rise.in{opacity:1;transform:none}
.rise[data-d="1"]{transition-delay:.1s}
.rise[data-d="2"]{transition-delay:.2s}
.rise[data-d="3"]{transition-delay:.3s}

/* ---------------- nav ---------------- */
.nav{position:fixed;top:0;left:0;right:0;z-index:200;padding:1.15rem 0;border-bottom:1px solid transparent;transition:background .4s,border-color .4s,padding .4s}
.nav{background:var(--paper)}
.nav.stuck{background:rgba(251,246,234,.9);backdrop-filter:blur(18px) saturate(1.4);border-bottom-color:rgba(28,17,19,.1);padding:.75rem 0}
.nav-in{display:flex;align-items:center;justify-content:space-between;gap:2rem}
.wordmark{font-family:'Fraunces',serif;font-variation-settings:'SOFT' 60,'WONK' 1;font-size:1.42rem;font-weight:500;letter-spacing:-.03em;text-decoration:none;display:flex;align-items:baseline;gap:.42rem;color:var(--bark)}
.wordmark i{font-style:italic;color:var(--orange)}
.nav-r{display:flex;align-items:center;gap:clamp(1.15rem,1.9vw,2rem)}
.nav-r a:not(.cta){text-decoration:none;font-size:.94rem;font-weight:500;color:var(--bark-2);position:relative;padding:.2rem 0}
.nav-r a:not(.cta)::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;background:var(--orange);transform:scaleX(0);transform-origin:right;transition:transform .4s cubic-bezier(.2,.7,.3,1)}
.nav-r a:not(.cta):hover::after{transform:scaleX(1);transform-origin:left}
.nav-r a[aria-current]{color:var(--orange-deep)}
.nav-r a[aria-current]::after{transform:scaleX(1)}
.cta{display:inline-flex;align-items:center;gap:.55rem;background:var(--orange-deep);color:var(--paper);text-decoration:none;padding:.72rem 1.4rem;border-radius:0;font-size:.9rem;font-weight:500;letter-spacing:.01em;transition:background .3s}
.cta:hover{background:var(--bark)}
.cta .dot{width:5px;height:5px;background:var(--sun);flex:none}
.burger{display:none;background:none;border:0;cursor:pointer;padding:.4rem;width:38px}
.burger i{display:block;height:1.5px;background:var(--bark);margin:6px 0;transition:.3s}
@media (max-width:880px){
  .burger{display:block}
  .nav-r{position:fixed;inset:0;background:var(--leaf-deep);color:var(--paper);flex-direction:column;justify-content:center;gap:1.4rem;clip-path:circle(0% at 92% 4%);transition:clip-path .6s cubic-bezier(.7,0,.2,1)}
  .nav-r.open{clip-path:circle(150% at 92% 4%)}
  .nav-r a:not(.cta){font-family:'Fraunces',serif;font-size:2rem;color:var(--paper)}
  .nav-r .cta{background:var(--orange);color:#fff}
}

/* ---------------- hero ---------------- */
.hero{position:relative;padding:8.5rem 0 clamp(2rem,5vw,3.5rem);background:var(--paper);overflow:hidden}
.hero > .shell{position:relative;z-index:1}
.hero-stage{position:relative}
@media (min-width:881px){
  .hero-stage{width:100vw;margin-left:calc(50% - 50vw)}
}
.hero h1{color:var(--bark);max-width:11ch}
.hero h1 .lit{font-style:italic;color:var(--orange-deep)}
.hero-lede{font-size:clamp(1.02rem,1.2vw,1.16rem);color:var(--bark-2);max-width:36ch;margin:1.4rem 0 0}
.hero-meta{font-size:.86rem;color:var(--bark-2);margin:clamp(1.1rem,2vw,1.5rem) 0 0;display:flex;flex-wrap:wrap;gap:.15rem .9rem;align-items:baseline;max-width:44ch}
.hero-meta strong{color:var(--bark);font-weight:600}
.hero-meta span::before{content:"";display:inline-block;width:14px;height:1px;background:var(--orange);margin-right:.7rem;vertical-align:.32em}

/* the paper bleeds across the left of the painting so type stays legible */
.hero-wash{position:absolute;inset:0;z-index:2;pointer-events:none;
  background:linear-gradient(97deg,
    rgba(247,240,227,.98) 0%, rgba(247,240,227,.96) 30%,
    rgba(247,240,227,.88) 44%, rgba(247,240,227,.5) 56%,
    rgba(247,240,227,.12) 66%, rgba(247,240,227,0) 76%);
}
@media (min-width:881px){
  .hero-copy{position:absolute;z-index:3;inset:0 auto 0 0;width:60%;
    display:flex;flex-direction:column;justify-content:center;
    padding-block:clamp(1.5rem,3vw,3rem);
    padding-right:clamp(1.5rem,3vw,3rem);
    padding-left:max(var(--gut), calc((100vw - var(--maxw)) / 2 + var(--gut)));}
}
@media (max-width:880px){
  .hero{padding-top:7rem}
  .hero-copy{margin-bottom:1.6rem}
  .hero-wash{display:none}
  .hero-plate{max-height:44vh;overflow:hidden}
  .hero-plate img{height:44vh;object-fit:cover;object-position:62% 46%}
}

/* every illustration sits on the page as its own plate */
.plate{position:relative;background:var(--paper)}
.plate img{width:100%;height:auto;display:block}
.hero-plate{overflow:hidden;position:relative}
.hero-plate::after{
  content:"";position:absolute;inset:0;pointer-events:none;mix-blend-mode:soft-light;
  background:radial-gradient(56% 60% at 78% 18%, rgba(255,232,170,.9) 0%, rgba(255,222,150,.4) 34%, rgba(255,255,255,0) 68%);
}
.hero-plate img{animation:plateIn 1.6s cubic-bezier(.16,.8,.3,1) both}
@keyframes plateIn{from{opacity:0;transform:scale(1.03)}to{opacity:1;transform:none}}

/* ---------------- opening statement ---------------- */
.intro{padding:clamp(4.5rem,10vw,8.5rem) 0}
.intro-grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:clamp(2rem,6vw,5rem);align-items:start}
@media (max-width:880px){.intro-grid{grid-template-columns:1fr}}
.quote{font-family:'Fraunces',serif;font-variation-settings:'SOFT' 70,'WONK' 1;font-size:clamp(1.85rem,4.1vw,3.4rem);line-height:1.09;letter-spacing:-.03em;max-width:20ch;margin:0}
.quote .hl{background:linear-gradient(180deg,transparent 58%,rgba(255,176,31,.55) 58%)}
.intro-body{display:grid;gap:1.4rem;padding-top:.6rem}
.intro-body p{color:var(--bark-2);font-size:1.05rem;margin:0}

/* the continuous line drawing, revealed as if being drawn, on scroll */
.ink{position:absolute;z-index:0;aspect-ratio:1200/891;pointer-events:none;
  background:var(--orange-deep);opacity:.85;
  -webkit-mask:var(--ink-src) no-repeat center/contain;
          mask:var(--ink-src) no-repeat center/contain;
  clip-path:inset(0 100% 0 0);
  right:max(-7vw,-90px);top:clamp(1.5rem,3.5vw,3.5rem);width:min(56vw,720px)}
@media (max-width:900px){
  .ink{right:auto;left:50%;translate:-50% 0;top:1rem;width:min(108vw,600px);opacity:.55}
  .flit{opacity:.12}
}

/* faint drift of small butterflies over the paper */
.flit{position:absolute;inset:0;z-index:0;pointer-events:none;opacity:.17;
  background:var(--flit-src) repeat center/min(1500px,155vw);
  mix-blend-mode:multiply}

/* ---------------- metamorphosis ---------------- */
.meta{background:linear-gradient(180deg,var(--wash-sun),var(--wash-leaf));color:var(--bark);padding:clamp(5rem,11vw,9rem) 0 clamp(4.5rem,10vw,8rem);position:relative;overflow:hidden}
.meta > .shell{position:relative;z-index:1}
.meta h2{color:var(--bark);max-width:13ch}
.meta-head{margin-bottom:clamp(2.5rem,5vw,4rem);max-width:min(52%,30rem)}
@media (max-width:900px){
  .meta-head{max-width:none}
  .meta{padding-top:calc(1rem + min(80vw,446px))}
}
.meta-head p{color:var(--bark-2);margin:1.2rem 0 .4rem;max-width:40ch}
.stages{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(1rem,2.5vw,2rem)}
@media (max-width:1040px) and (min-width:761px){.stages{gap:1rem}}
@media (max-width:760px){
  .stages{grid-template-columns:1fr;gap:1.6rem}
  .stage{display:grid;grid-template-columns:36% minmax(0,1fr);gap:1.1rem;align-items:center}
  .stage figcaption{padding-top:0}
  .stage p{font-size:.9rem}
}
.stage{margin:0}
.stage .plate{background:var(--paper);aspect-ratio:2/3;overflow:hidden}
.stage .plate img{width:100%;height:100%;object-fit:cover}
.stage img{transition:transform 1.1s cubic-bezier(.2,.7,.3,1)}
.stage:hover img{transform:scale(1.02)}
.stage figcaption{padding-top:1.1rem}
.stage .n{font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:var(--orange-deep);display:block;margin-bottom:.45rem}
.stage h3{color:var(--bark)}
.stage p{color:var(--bark-2);font-size:.95rem;margin:.5rem 0 0;max-width:34ch}
.meta-note{margin-top:clamp(2rem,4vw,3rem);max-width:66ch;color:var(--bark-2);border-top:1px solid rgba(58,50,39,.2);padding-top:1.6rem}
.meta-note b{color:var(--orange-deep);font-weight:600}

/* ---------------- what it feels like ---------------- */
.work{background:linear-gradient(180deg,var(--wash-pink),var(--wash-sun));padding:clamp(4rem,9vw,7.5rem) 0}
.work-head{display:flex;flex-wrap:wrap;align-items:end;justify-content:space-between;gap:2rem;margin-bottom:clamp(2.5rem,5vw,4rem)}
.work-head p{color:var(--bark-2);max-width:38ch;margin:0}
.rows{border-top:1px solid rgba(58,50,39,.18)}
.row{
  position:relative;display:grid;
  grid-template-columns:3.4rem minmax(0,1.05fr) minmax(0,1fr);
  gap:clamp(1rem,3vw,2.6rem);align-items:baseline;
  padding:clamp(1.5rem,3vw,2.3rem) 0;
  border-bottom:1px solid rgba(58,50,39,.18);
  transition:padding-left .55s cubic-bezier(.2,.7,.3,1);
}
.row:hover{padding-left:1.2rem}
/* a thread drawing itself under each one */
.row::after{
  content:"";position:absolute;left:0;bottom:-1px;height:1px;width:100%;
  background:var(--tint,var(--orange));
  transform:scaleX(0);transform-origin:left;
  transition:transform .7s cubic-bezier(.2,.7,.3,1);
}
.row:hover::after{transform:scaleX(1)}
.row-num{
  font-family:'Fraunces',serif;font-size:.82rem;color:var(--bark-3);
  letter-spacing:.1em;font-weight:600;transition:color .4s;
}
.row:hover .row-num{color:var(--tint,var(--orange))}
.row h3{
  font-size:clamp(1.3rem,2.4vw,2.05rem);max-width:18ch;line-height:1.04;
  font-variation-settings:'SOFT' 70,'WONK' 1,'opsz' 120;
}
.row h3 i{font-style:italic;color:var(--tint,var(--orange))}
.row p{color:var(--bark-2);margin:0;font-size:1rem;line-height:1.6}
@media (max-width:820px){
  .row{grid-template-columns:2.4rem 1fr;gap:.5rem 1rem}
  .row p{grid-column:2;margin-top:.6rem}
}

/* ---------------- about ---------------- */
.about{padding:clamp(4.5rem,10vw,8rem) 0;background:linear-gradient(180deg,var(--wash-sky),var(--paper))}
.about-grid{display:grid;grid-template-columns:minmax(0,.82fr) minmax(0,1.18fr);gap:clamp(2rem,6vw,5rem);align-items:center}
@media (max-width:880px){.about-grid{grid-template-columns:1fr}}
.portrait{position:relative;border-radius:0;border:1px solid rgba(58,50,39,.32);background:var(--paper);overflow:hidden}
@media (max-width:880px){.portrait{max-width:420px}}
.portrait::after{content:"";position:absolute;inset:8px;border:1px solid rgba(58,50,39,.22);pointer-events:none}
.portrait img{width:100%;height:auto;display:block}
.about h2{max-width:15ch;margin-bottom:1.5rem}
.about p{color:var(--bark-2)}
.sig{font-family:'Fraunces',serif;font-style:italic;font-variation-settings:'SOFT' 90,'WONK' 1;font-size:1.5rem;color:var(--orange-deep);margin-top:1.6rem}
.facts{list-style:none;padding:0;margin:2.2rem 0 0;display:grid;gap:.85rem;max-width:40ch}
.facts li{display:flex;gap:1rem;font-size:.95rem;color:var(--bark-2);border-top:1px solid rgba(28,17,19,.15);padding-top:.85rem}
.facts b{font-weight:600;color:var(--leaf-deep);flex:none;width:8.5rem}

/* ---------------- workshops ---------------- */
.shops{background:linear-gradient(165deg,var(--wash-leaf),var(--wash-sun));padding:clamp(4.5rem,10vw,8rem) 0}
.sun-plate{margin:0 0 clamp(2rem,4vw,3.2rem);overflow:hidden}
.sun-plate img{max-height:clamp(210px,42vh,420px);width:100%;object-fit:cover;object-position:50% 34%}
.shops-head{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:clamp(1.5rem,5vw,4rem);align-items:end;margin-bottom:clamp(2.5rem,5vw,4rem)}
.shops-head h2{max-width:15ch}
.shops-head p{color:var(--bark-2);margin:0 0 .4rem;max-width:36ch}
@media (max-width:820px){.shops-head{grid-template-columns:1fr;align-items:start}}
.shop-list{border-top:1px solid rgba(28,17,19,.18)}
.shop{padding:clamp(1.6rem,3.4vw,2.4rem) 0;border-bottom:1px solid rgba(28,17,19,.18);display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr) 15.5rem;gap:clamp(1rem,3vw,2.5rem);align-items:center;transition:padding-left .5s cubic-bezier(.2,.7,.3,1)}
.shop:hover{padding-left:1.2rem}
.shop p{margin:0;color:var(--bark-2);font-size:1rem}
.tag{font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;font-weight:600;white-space:nowrap;padding:.3rem 0 .32rem;border-bottom:1.5px solid currentColor;justify-self:start;align-self:center}
.tag.open{color:var(--leaf)}
.tag.lic{color:var(--orange-deep)}
@media (max-width:820px){.shop{grid-template-columns:1fr;gap:.8rem}.tag{justify-self:start}}
.scope{margin-top:2.4rem;padding:1.4rem 1.6rem;border-radius:0;background:rgba(94,122,79,.09);border-left:2px solid var(--leaf);font-size:.96rem;color:var(--bark-2);max-width:72ch}
.scope b{color:var(--leaf-deep);font-weight:600}

/* ---------------- forms ---------------- */
.field{margin-bottom:1.5rem;position:relative}
.field label{display:block;font-size:.82rem;letter-spacing:.06em;text-transform:uppercase;font-weight:600;color:var(--bark-2);margin-bottom:.5rem}
.field input,.field select,.field textarea{width:100%;font:inherit;font-size:1.02rem;color:var(--bark);background:transparent;border:0;border-bottom:1.5px solid rgba(28,17,19,.26);padding:.7rem 0;border-radius:0;transition:border-color .3s}
.field textarea{min-height:96px;resize:vertical}
.field input:focus,.field select:focus,.field textarea:focus{outline:none;border-bottom-color:var(--orange)}
.field .note{font-size:.82rem;color:var(--bark-3);margin:.6rem 0 0;max-width:52ch}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem}
@media (max-width:640px){.duo{grid-template-columns:1fr}}
.hp{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}
.opts{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:.55rem;margin:.2rem 0 1.6rem}
.opts label{text-transform:none;letter-spacing:0;font-size:.94rem;font-weight:400;margin:0;display:flex;align-items:center;gap:.6rem;cursor:pointer;border:1px solid rgba(58,50,39,.26);border-radius:0;padding:.55rem 1rem;transition:.3s;color:var(--bark)}
.opts label:has(input:checked){border-color:var(--orange);background:rgba(255,90,31,.1)}
input[type=checkbox]{
  appearance:none;-webkit-appearance:none;
  width:18px;height:18px;min-width:18px;min-height:18px;flex:0 0 18px;aspect-ratio:1;
  margin:0;padding:0;box-sizing:border-box;border-radius:0;
  border:1px solid rgba(58,50,39,.5);background:transparent;
  display:grid;place-content:center;cursor:pointer;transition:.2s;
}
input[type=checkbox]::after{content:"";width:8px;height:8px;aspect-ratio:1;border-radius:0;background:var(--orange-deep);transform:scale(0);transition:.2s}
input[type=checkbox]:checked{border-color:var(--orange)}
input[type=checkbox]:checked::after{transform:scale(1)}
button.submit{font:inherit;font-weight:500;font-size:1rem;cursor:pointer;background:var(--orange-deep);color:var(--paper);border:0;border-radius:0;padding:.92rem 2rem;transition:background .3s}
button.submit:hover{background:var(--bark)}
button.submit:disabled{opacity:.55;cursor:default}
.status{display:none;margin-top:1.2rem;font-size:.95rem;color:var(--leaf-deep);border-left:2px solid var(--leaf-deep);padding-left:1rem}
.status.on{display:block}
.signup{background:var(--plum);color:var(--paper);border-radius:0;padding:clamp(1.75rem,4vw,3.5rem);margin-top:clamp(2.5rem,5vw,4rem);display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:clamp(1.5rem,5vw,4rem);align-items:start}
@media (max-width:880px){.signup{grid-template-columns:1fr;gap:1.5rem}}
.signup h3{color:var(--paper);margin-bottom:.6rem}
.signup .signup-copy p{color:rgba(253,244,233,.7)}
.signup label{color:rgba(253,244,233,.66)}
.signup input,.signup select{color:var(--paper);border-bottom-color:rgba(253,244,233,.3)}
.signup select option{color:var(--bark)}
.signup .opts label{color:var(--paper);border-color:rgba(253,244,233,.3)}
.signup .opts label:has(input:checked){border-color:var(--sun);background:rgba(255,176,31,.16)}
.signup input[type=checkbox]{border-color:rgba(253,244,233,.45)}
.signup input[type=checkbox]:checked{border-color:var(--sun)}
.signup input[type=checkbox]::after{background:var(--sun)}
.signup .note{color:rgba(253,244,233,.5)}
.signup button.submit{background:var(--orange);color:#fff}
.signup button.submit:hover{background:var(--sun);color:var(--bark)}
.signup .status{color:var(--sun);border-color:var(--sun)}

/* ---------------- contact ---------------- */
.contact{padding:clamp(4.5rem,10vw,9rem) 0 clamp(3.5rem,7vw,6rem);background:linear-gradient(180deg,var(--paper),var(--wash-plum))}
.contact-grid{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:clamp(2.5rem,6vw,5rem)}
@media (max-width:880px){.contact-grid{grid-template-columns:1fr}}
.contact h2{max-width:12ch;margin-bottom:1.4rem}
.details dl{margin:0;border-top:1px solid rgba(28,17,19,.18)}
.details dt{font-size:.76rem;letter-spacing:.13em;text-transform:uppercase;color:var(--leaf-deep);font-weight:600;margin-top:1.4rem}
.details dd{margin:.35rem 0 1.3rem;color:var(--bark-2);font-size:1rem;border-bottom:1px solid rgba(28,17,19,.1);padding-bottom:1.3rem}
.details dd:last-of-type{border-bottom:0}
.details a{color:var(--orange-deep)}
.urgent{margin-top:.5rem;padding:1.3rem 1.5rem;border-radius:0;background:rgba(217,118,47,.09);border-left:2px solid var(--orange);font-size:.94rem;color:var(--bark-2)}
.urgent b{color:var(--orange-deep);font-weight:600}

/* ---------------- inner pages: services, faq, legal ---------------- */
.pagehead{position:relative;padding:clamp(7rem,11vw,9.5rem) 0 clamp(1.5rem,3.5vw,2.75rem);
  background:linear-gradient(180deg,var(--wash,var(--paper)),var(--paper));overflow:hidden}
.pagehead > .shell{position:relative;z-index:2}
.pagehead .kicker{font-size:.74rem;letter-spacing:.17em;text-transform:uppercase;font-weight:600;
  color:var(--orange-deep);margin:0 0 1.1rem}
.pagehead h1{max-width:15ch;font-size:clamp(2.4rem,6vw,5.2rem)}
.pagehead .lede{font-size:clamp(1.05rem,1.35vw,1.24rem);color:var(--bark-2);max-width:52ch;margin:1.6rem 0 0}

/* the pen and ink botanical, tinted, rising out of the bottom corner */
.botanical{position:absolute;z-index:0;pointer-events:none;
  background:var(--leaf);opacity:.2;
  -webkit-mask:var(--bot-src) no-repeat bottom center/contain;
          mask:var(--bot-src) no-repeat bottom center/contain;
  right:max(-3vw,-40px);bottom:0;width:min(34vw,420px);aspect-ratio:540/1047}
.botanical.left{right:auto;left:max(-4vw,-50px);bottom:0;transform:scaleX(-1)}
.botanical.warm{background:var(--orange-deep);opacity:.16}
@media (max-width:820px){.botanical{width:min(58vw,300px);opacity:.13}}

/* the scattered butterflies live here now, not on the home page */
.flit-page{position:absolute;inset:0;z-index:0;pointer-events:none;opacity:.2;
  background:var(--flit-src) repeat center/min(1500px,155vw);mix-blend-mode:multiply}
@media (max-width:820px){.flit-page{opacity:.13}}

.band{position:relative;padding:clamp(3.5rem,8vw,6.5rem) 0;background:var(--paper)}
.pagehead + .band{padding-top:clamp(1.75rem,4vw,3.25rem)}
.band.alt{background:linear-gradient(180deg,var(--paper),var(--wash,var(--paper-2)))}
.band > .shell{position:relative;z-index:2}

/* services index */
.svc-list{border-top:1px solid rgba(28,17,19,.16)}
.svc{display:grid;grid-template-columns:auto minmax(0,1.25fr) minmax(0,1fr) auto;
  gap:clamp(1rem,3vw,2.5rem);align-items:baseline;
  padding:clamp(1.6rem,3.5vw,2.6rem) 0;border-bottom:1px solid rgba(28,17,19,.16);
  text-decoration:none;position:relative;transition:padding-left .5s cubic-bezier(.2,.7,.3,1)}
.svc:hover{padding-left:.9rem}
.svc::after{content:"";position:absolute;left:0;bottom:-1px;height:1px;width:100%;
  background:var(--tint,var(--orange));transform:scaleX(0);transform-origin:left;
  transition:transform .7s cubic-bezier(.2,.7,.3,1)}
.svc:hover::after{transform:scaleX(1)}
.svc .n{font-size:.74rem;letter-spacing:.14em;font-weight:600;color:var(--tint,var(--orange));
  font-variant-numeric:tabular-nums}
.svc h3{color:var(--bark);max-width:22ch}
.svc p{margin:0;color:var(--bark-2);font-size:.98rem;max-width:44ch}
.svc .go{font-size:1.4rem;line-height:1;color:var(--tint,var(--orange));
  transition:transform .5s cubic-bezier(.2,.7,.3,1)}
.svc:hover .go{transform:translateX(6px)}
@media (max-width:900px){
  .svc{grid-template-columns:auto minmax(0,1fr);gap:.5rem 1.1rem}
  .svc p{grid-column:2}
  .svc .go{display:none}
}

/* long form reading column */
.prose{display:grid;grid-template-columns:minmax(0,22ch) minmax(0,1fr);
  gap:clamp(1.5rem,5vw,4.5rem);align-items:start}
@media (max-width:860px){.prose{grid-template-columns:1fr;gap:1rem}}
.prose > h2{font-size:clamp(1.6rem,3.2vw,2.5rem);position:sticky;top:6.5rem;max-width:none}
@media (max-width:860px){.prose > h2{position:static;top:auto;margin-bottom:.3rem}}
.prose-body p{color:var(--bark-2);max-width:64ch}
.prose-body p:last-child{margin-bottom:0}
.prose-body h3{margin:2.2rem 0 .6rem;color:var(--bark)}
.prose-body h3:first-child{margin-top:0}
.prose-body ul{margin:0 0 1.15em;padding-left:1.1rem;color:var(--bark-2);max-width:62ch}
.prose-body li{margin-bottom:.5rem}
.prose-body li::marker{color:var(--orange)}
.prose-body b{color:var(--bark);font-weight:600}
.prose-body a{color:var(--orange-deep)}
.prose-body a.cta,.prose-body a.cta:hover{color:var(--paper)}
.prose + .prose{margin-top:clamp(2.5rem,6vw,4.5rem);padding-top:clamp(2.5rem,6vw,4.5rem);
  border-top:1px solid rgba(28,17,19,.14)}

/* faq */
.faq{border-top:1px solid rgba(28,17,19,.16);max-width:78ch}
.faq details{border-bottom:1px solid rgba(28,17,19,.16)}
.faq summary{list-style:none;cursor:pointer;padding:clamp(1.2rem,2.6vw,1.7rem) 3rem clamp(1.2rem,2.6vw,1.7rem) 0;
  position:relative;font-family:'Fraunces',serif;font-variation-settings:'SOFT' 55,'WONK' 1;
  font-size:clamp(1.1rem,1.7vw,1.4rem);letter-spacing:-.02em;color:var(--bark);transition:color .3s}
.faq summary::-webkit-details-marker{display:none}
.faq summary:hover{color:var(--orange-deep)}
.faq summary::after{content:"";position:absolute;right:.4rem;top:50%;width:13px;height:1.5px;
  background:var(--orange);transition:transform .4s}
.faq summary::before{content:"";position:absolute;right:.4rem;top:50%;width:13px;height:1.5px;
  background:var(--orange);transform:rotate(90deg);transition:transform .4s}
.faq details[open] summary::before{transform:rotate(0deg)}
.faq .a{padding:0 2.5rem 1.6rem 0;color:var(--bark-2);animation:fade .5s ease}
.faq .a p{margin:0 0 .9em}
.faq .a p:last-child{margin:0}
.faq .a a{color:var(--orange-deep)}
@keyframes fade{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}

/* legal type is smaller and quieter, but still readable */
.legal .prose-body{font-size:.96rem}
.legal .prose-body p{max-width:70ch}
.updated{font-size:.8rem;letter-spacing:.09em;text-transform:uppercase;color:var(--bark-3);
  font-weight:600;margin:0 0 2.5rem}
.callout{margin:0 0 1.6rem;padding:1.3rem 1.5rem;background:rgba(217,118,47,.09);
  border-left:2px solid var(--orange);font-size:.94rem;color:var(--bark-2);max-width:66ch}
.callout b{color:var(--orange-deep);font-weight:600}
.callout p:last-child{margin-bottom:0}
.todo{background:#FFE9A8;color:#6B4B00;padding:.05em .4em;font-weight:600;
  box-shadow:inset 0 -1px 0 #C79A20}

/* next / prev service */
.pager{display:flex;flex-wrap:wrap;gap:1rem;justify-content:space-between;align-items:center;
  margin-top:clamp(2.5rem,6vw,4rem);padding-top:2rem;border-top:1px solid rgba(28,17,19,.16)}
.pager a{text-decoration:none;font-weight:500;color:var(--orange-deep);font-size:.95rem}
.pager a:hover{color:var(--bark)}
.pager .lbl{display:block;font-size:.72rem;letter-spacing:.15em;text-transform:uppercase;
  color:var(--bark-3);font-weight:600;margin-bottom:.25rem}

/* ---------------- the light where you are ---------------- */
.sky{position:relative;background:linear-gradient(180deg,var(--wash-leaf),var(--wash-sky));overflow:hidden;
  padding:clamp(4rem,9vw,7rem) 0 clamp(3rem,6vw,5rem)}
.sky-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.95fr);
  gap:clamp(1.2rem,4vw,3.5rem);align-items:end;margin-bottom:clamp(2rem,4vw,3rem)}
@media (max-width:860px){.sky-head{grid-template-columns:1fr;align-items:start}}
.sky-head h2{max-width:13ch}
.sky-head p{color:var(--bark-2);margin:0;max-width:44ch}
.sky-frame{position:relative;width:100%;aspect-ratio:1100/1090;max-height:62vh;overflow:hidden}
@media (min-width:861px){.sky-frame{aspect-ratio:auto;height:clamp(340px,44vw,560px)}}
.sky-frame img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
  opacity:0;transform:scale(1.045);
  transition:opacity 1.1s ease,transform 2.4s cubic-bezier(.2,.7,.3,1)}
.sky-frame img.on{opacity:1;transform:none}
.sky-frame::after{content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,rgba(58,50,39,.22),rgba(58,50,39,0) 34%,rgba(58,50,39,0) 58%,rgba(58,50,39,.5))}
.sky-caption{position:absolute;left:0;right:0;bottom:0;z-index:2;
  display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:1rem;
  padding:clamp(1.1rem,3vw,2rem)}
.sky-now{font-family:'Fraunces',serif;font-variation-settings:'SOFT' 80,'WONK' 1;font-style:italic;
  font-size:clamp(1.15rem,2.4vw,1.9rem);color:#FBF6EA;margin:0;max-width:22ch;
  text-shadow:0 2px 22px rgba(30,20,14,.55)}
.states{display:flex;gap:.4rem;flex-wrap:wrap}
.states button{background:rgba(251,246,234,.14);border:1px solid rgba(251,246,234,.4);
  color:#FBF6EA;font:inherit;font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;
  font-weight:600;padding:.5rem .85rem;cursor:pointer;backdrop-filter:blur(6px);
  transition:background .3s,color .3s,border-color .3s;line-height:1.1;text-align:left}
.states button:hover{background:rgba(251,246,234,.3)}
.states button[aria-pressed="true"]{background:#FBF6EA;color:var(--bark);border-color:#FBF6EA}
.states button small{display:block;font-size:.72rem;letter-spacing:.02em;text-transform:none;
  font-weight:400;opacity:.78;font-variant-numeric:tabular-nums}

/* ---------------- footer ---------------- */
.greenhouse{position:relative;background:var(--paper-2);overflow:hidden}
.greenhouse img{width:100%;height:clamp(200px,38vh,520px);object-fit:cover;object-position:50% 46%;display:block}
.greenhouse::after{
  content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,var(--paper-2) 0%,rgba(245,238,221,0) 22%,rgba(245,238,221,0) 58%,color-mix(in oklab,var(--foot) 70%,transparent) 88%,var(--foot) 100%);
  transition:background 1.2s ease;
}
.greenhouse-line{
  position:absolute;left:0;right:0;bottom:clamp(1.5rem,4vw,3rem);z-index:2;text-align:center;
  font-family:'Fraunces',serif;font-variation-settings:'SOFT' 80,'WONK' 1;font-style:italic;
  font-size:clamp(1.2rem,2.6vw,2rem);color:#FBF6EA;text-shadow:0 2px 24px rgba(30,42,26,.6);
  margin:0;padding-inline:var(--gut);
}
footer{background:var(--foot);color:rgba(251,246,234,.8);padding:clamp(3.5rem,7vw,5.5rem) 0 3rem;font-size:.92rem;transition:background 1.2s ease;position:relative;overflow:hidden}
footer::before{content:"";position:absolute;inset:0;pointer-events:none;
  background:radial-gradient(120% 80% at 50% 118%,color-mix(in oklab,var(--foot-2) 85%,transparent),transparent 70%);
  transition:background 1.2s ease}
footer > .shell{position:relative;z-index:1}
.foot-mark{font-family:'Fraunces',serif;font-variation-settings:'SOFT' 60,'WONK' 1;font-size:clamp(2.8rem,10vw,7.5rem);line-height:.86;letter-spacing:-.045em;color:#FBF6EA;margin:0 0 2.5rem}
.foot-mark i{font-style:italic;color:var(--orange-lit)}
.foot-cols{display:grid;grid-template-columns:1.5fr 1fr 1fr;gap:2.5rem;padding-bottom:3rem;border-bottom:1px solid rgba(251,246,234,.18)}
@media (max-width:760px){.foot-cols{grid-template-columns:1fr}}
.foot-cols h4{font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--sun);font-weight:600;margin:0 0 1rem}
.foot-cols ul{list-style:none;padding:0;margin:0}
.foot-cols li{margin-bottom:.6rem}
.foot-cols a{text-decoration:none;transition:color .3s}
.foot-cols a:hover{color:var(--sun)}
.fine{padding-top:2.5rem;font-size:.81rem;line-height:1.72;color:rgba(251,246,234,.66);display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.4rem 3rem}
.fine p{max-width:52ch;margin:0}
.fine b{color:rgba(251,246,234,.78);font-weight:500}
.fine a{color:rgba(251,246,234,.78)}
.fine .full{grid-column:1/-1;padding-top:1rem;border-top:1px solid rgba(251,246,234,.14)}

@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:.001ms !important;animation-iteration-count:1 !important;transition-duration:.001ms !important}
  html{scroll-behavior:auto}
  .rise{opacity:1;transform:none}
}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<nav class="nav" id="nav">
  <div class="shell nav-in">
    <a class="wordmark" href="#top">Bloom<i>&amp;</i>Rise</a>
    <button class="burger" id="burger" aria-expanded="false" aria-controls="navr" aria-label="Menu"><i></i><i></i></button>
    <div class="nav-r" id="navr">
      <a href="#becoming">Becoming</a>
      <a href="#work">What it feels like</a>
      <a href="#about">Roshunda</a>
      <a href="#shops">Workshops</a>
      <a class="cta" href="#contact"><span class="dot"></span>Book a consult</a>
    </div>
  </div>
</nav>

<main id="main">

<header class="hero" id="top">
  <div class="shell">
    <div class="hero-stage">
      <figure class="plate hero-plate" style="margin:0">
        <img src="__HERO_ART__" alt="Watercolour of a monarch butterfly among milkweed" fetchpriority="high">
        <span class="hero-wash"></span>
      </figure>
      <div class="hero-copy">
        <h1>You've spent a long time being <span class="lit">the strong one.</span></h1>
        <p class="hero-lede">
          Therapy for anxiety, identity and self trust, body image, and
          depression. Online, with paint and paper never far from reach.
        </p>
        <p class="hero-meta">
          <strong>Roshunda M. Hartison, MEd, LPC</strong>
          <span>Online sessions for Texas, Virginia, and Colorado</span>
        </p>
      </div>
    </div>
  </div>
</header>

<section class="intro">
  <div class="shell intro-grid">
    <blockquote class="quote rise">
      Showing up for yourself is powerful. You <span class="hl">shouldn't have to</span> do it alone.
    </blockquote>
    <div class="intro-body">
      <p class="rise" data-d="1">
        Maybe you second guess every decision. Maybe you have put everyone else first so long
        that you have lost track of what you want. Maybe the thoughts have gotten loud enough
        that they are running your day.
      </p>
      <p class="rise" data-d="2">
        We work actively. We look at the patterns keeping you stuck, push back on the anxious
        thinking, and rehearse new ways of responding until they hold under pressure. When words
        run out, we use color and sound and making instead. Some weeks that is the whole session.
      </p>
    </div>
  </div>
</section>

<section class="meta" id="becoming">
  <span class="ink" id="ink" role="img" aria-label="A single unbroken line drawing of a butterfly lifting from an open hand"></span>
  <div class="shell">
    <div class="meta-head">
      <h2 class="rise">Most of the work happens in the dark part.</h2>
      <p class="rise" data-d="1">
        We tend to picture change as a before and an after. In real life there is a long
        middle between the two, and that middle is where almost all of the actual work happens.
      </p>
    </div>

    <div class="stages">
      <figure class="stage rise">
        <div class="plate"><img src="__STAGE_1__" alt="Watercolour of a monarch chrysalis hanging from a milkweed stem" loading="lazy"></div>
        <figcaption>
          <span class="n">One</span>
          <h3>The folding in</h3>
          <p>You stop performing fine. We put language to what is actually happening and treat it as serious.</p>
        </figcaption>
      </figure>
      <figure class="stage rise" data-d="1">
        <div class="plate"><img src="__STAGE_2__" alt="Watercolour of a monarch emerging from its chrysalis" loading="lazy"></div>
        <figcaption>
          <span class="n">Two</span>
          <h3>The hard middle</h3>
          <p>You stay with the discomfort instead of managing it away. Exposure work lives here, and so does most of the change.</p>
        </figcaption>
      </figure>
      <figure class="stage rise" data-d="2">
        <div class="plate"><img src="__STAGE_3__" alt="Watercolour of a monarch resting on a coneflower" loading="lazy"></div>
        <figcaption>
          <span class="n">Three</span>
          <h3>First light</h3>
          <p>You are steadier with yourself, and you know what to do the next time it gets loud.</p>
        </figcaption>
      </figure>
    </div>

    <p class="meta-note rise">
      <b>A caterpillar does not improve into a butterfly. It dissolves first.</b>
      Becoming yourself has less to do with stacking better habits onto who you have been, and more
      to do with letting the shape you were handed come apart so something truer can set. That is
      uncomfortable, and it is the part that works. You should not have to sit through it alone.
    </p>
  </div>
</section>

<section class="sky" id="sky">
  <div class="shell">
    <div class="sky-head">
      <h2 class="rise">The same sky, three states over.</h2>
      <p class="rise" data-d="1">
        Roshunda sees clients in Texas, Virginia, and Colorado, which means the working day
        starts and ends at three slightly different times. This is the light outside right now,
        wherever you happen to be reading. Tap a state to stand in it for a moment.
      </p>
    </div>
    <div class="sky-frame rise" data-d="1">
      <img id="sky1" src="__SKY_1__" alt="Watercolour of sunrise over a wildflower meadow" loading="lazy">
      <img id="sky2" src="__SKY_2__" alt="Watercolour of a green field and a stream under a bright midday sky" loading="lazy">
      <img id="sky3" src="__SKY_3__" alt="Watercolour of the sun setting over an open field" loading="lazy">
      <div class="sky-caption">
        <p class="sky-now" id="skyNow">Morning where you are.</p>
        <div class="states" id="states" role="group" aria-label="See the light in each licensed state">
          <button type="button" data-tz="America/Chicago"  aria-pressed="false">Texas<small></small></button>
          <button type="button" data-tz="America/New_York" aria-pressed="false">Virginia<small></small></button>
          <button type="button" data-tz="America/Denver"   aria-pressed="false">Colorado<small></small></button>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="work" id="work">
  <div class="shell">
    <div class="work-head">
      <h2 class="rise">Start with what<br>it feels like.</h2>
      <p class="rise" data-d="1">Not a diagnosis, not a checklist. Most people know the feeling long before they have a word for it.</p>
    </div>
    <div class="rows">
      <article class="row rise" style="--tint:#B4551C">
        <span class="row-num">01</span>
        <h3>When you don't <i>trust yourself</i></h3>
        <p>We trace the messages you picked up early, sort out who handed them to you, and work out which ones you still want to carry.</p>
      </article>
      <article class="row rise" style="--tint:#D9762F">
        <span class="row-num">02</span>
        <h3>When you've been putting <i>everyone else first</i></h3>
        <p>For the person everyone leans on. We make room for what you want, without you having to justify wanting it.</p>
      </article>
      <article class="row rise" style="--tint:#C77BA6">
        <span class="row-num">03</span>
        <h3>When you don't feel <i>like enough</i></h3>
        <p>Body image, self worth, and the running commentary. Weight inclusive care aimed at a life you are actually present for.</p>
      </article>
      <article class="row rise" style="--tint:#5F2A46">
        <span class="row-num">04</span>
        <h3>When relationships feel <i>complicated</i></h3>
        <p>Family, partners, friendships, and the patterns that keep turning up in all three.</p>
      </article>
      <article class="row rise" style="--tint:#5E7A4F">
        <span class="row-num">05</span>
        <h3>When life is changing, <i>and so are you</i></h3>
        <p>New city, new role, new body, or the quiet realization one morning that the old shape stopped fitting a while ago.</p>
      </article>
      <article class="row rise" style="--tint:#9A4413">
        <span class="row-num">06</span>
        <h3>When anxiety is <i>running the show</i></h3>
        <p>We separate what is anxiety talking from what is actually you. This is also where OCD and exposure work fit, when that is part of the picture.</p>
      </article>
    </div>
  </div>
</section>

<section class="about" id="about">
  <div class="shell about-grid">
    <div class="portrait rise">
      <img src="__PORTRAIT__" alt="Roshunda M. Hartison" loading="lazy">
    </div>
    <div>
      <h2 class="rise">Helping people find their way has been a thread throughout my life.</h2>
      <p class="rise" data-d="1">
        I am Roshunda. Sixteen years in mental health and community work, five and a half of
        them as a licensed clinician, most of it alongside people the system tends to overlook. Community health, domestic violence and sexual
        assault services, intellectual and developmental disabilities, juvenile detention,
        Big Brothers Big Sisters, United Way. All of it taught me the same lesson. Meet people
        exactly where they are, and honor how much courage it takes to ask.
      </p>
      <p class="rise" data-d="2">
        You can show up exactly as you are, on the days that feel like progress and the ones that
        feel like nothing. We will make room for the hard parts, and we will probably laugh more
        than you expect.
      </p>
      <p class="sig rise" data-d="2">Roshunda M. Hartison, MEd, LPC</p>
      <ul class="facts rise" data-d="3">
        <li><b>Licensed in</b><span>Texas, Virginia, and Colorado</span></li>
        <li><b>Sessions</b><span>Online now. In-person visits in Texas coming soon.</span></li>
        <li><b>Education</b><span>MEd Clinical Counseling, University of Houston Victoria</span></li>
        <li><b>Also</b><span>Founder of Evolving Thru Art Inc.</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="shops" id="shops">
  <div class="shell">
    <figure class="plate sun-plate rise">
      <img src="__SUN__" alt="Watercolour of a sun high over a field of scrub and grasses" loading="lazy">
    </figure>
    <div class="shops-head">
      <h2 class="rise">Workshops and groups, coming soon.</h2>
      <p class="rise" data-d="1">Still taking shape. Tell me what you would want to be in the room for and I will build with that in mind.</p>
    </div>
    <div class="shop-list">
      <article class="shop rise">
        <h3>Create, Inspire, Repeat</h3>
        <p>A hands on creative session. No artistic talent required, and honestly better without it. Making as a way of noticing what you are carrying.</p>
        <span class="tag open">Open to every state</span>
      </article>
      <article class="shop rise" data-d="1">
        <h3>Making peace with the mirror</h3>
        <p>A weight inclusive look at body image, the stories underneath it, and what changes when the goal stops being a smaller body.</p>
        <span class="tag open">Open to every state</span>
      </article>
      <article class="shop rise" data-d="2">
        <h3>OCD support group</h3>
        <p>A small ongoing group for people doing ERP work. The part where you find out you are not the only one.</p>
        <span class="tag lic">Texas, Virginia, Colorado</span>
      </article>
    </div>

    <p class="scope rise">
      <b>Why the difference.</b> Workshops and creative classes are educational and open to anyone,
      anywhere. They are not therapy and do not create a client relationship. Therapy groups are
      clinical services, so they are available only to participants located in Texas, Virginia, or
      Colorado, where Roshunda holds a license.
    </p>

    <form class="signup rise" id="interestForm" novalidate>
      <div class="signup-copy">
        <h3>Tell me when these open</h3>
        <p>No newsletter, no spam. Just a note when there is a date on the calendar.</p>
      </div>
      <div class="signup-fields">
        <div class="duo">
          <div class="field">
            <label for="i-name">First name</label>
            <input id="i-name" name="name" type="text" autocomplete="given-name" required>
          </div>
          <div class="field">
            <label for="i-email">Email</label>
            <input id="i-email" name="email" type="email" autocomplete="email" required>
          </div>
        </div>
        <div class="field">
          <label>I would be interested in</label>
          <div class="opts">
            <label><input type="checkbox" name="interest" value="creative"> Creative workshops</label>
            <label><input type="checkbox" name="interest" value="body"> Body image and food</label>
            <label><input type="checkbox" name="interest" value="ocd"> OCD support group</label>
            <label><input type="checkbox" name="interest" value="other"> Something else</label>
          </div>
        </div>
        <div class="field">
          <label for="i-state">Where are you located</label>
          <select id="i-state" name="state">
            <option value="">Select a state</option>
            <option>Texas</option><option>Virginia</option><option>Colorado</option>
            <option>Somewhere else in the United States</option>
            <option>Outside the United States</option>
          </select>
          <p class="note">This tells me whether to plan a workshop or a clinical group. Nothing here is a request for services.</p>
        </div>
        <input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
        <button class="submit" type="submit">Keep me posted</button>
        <div class="status" id="interestStatus" role="status"></div>
      </div>
    </form>
  </div>
</section>

<section class="contact" id="contact">
  <div class="shell contact-grid">
    <div>
      <h2 class="rise">Let's find out if we fit.</h2>
      <p class="rise" data-d="1" style="color:var(--bark-2);margin-bottom:2.5rem">
        A free fifteen minute consult. Ask me anything, including the awkward questions about money, insurance, and whether this is going to work.
      </p>
      <form id="contactForm" novalidate class="rise" data-d="2">
        <div class="duo">
          <div class="field"><label for="c-name">Name</label><input id="c-name" name="name" type="text" autocomplete="name" required></div>
          <div class="field"><label for="c-email">Email</label><input id="c-email" name="email" type="email" autocomplete="email" required></div>
        </div>
        <div class="duo">
          <div class="field"><label for="c-phone">Phone, optional</label><input id="c-phone" name="phone" type="tel" autocomplete="tel"></div>
          <div class="field">
            <label for="c-state">State you will be in during sessions</label>
            <select id="c-state" name="state" required>
              <option value="">Select</option>
              <option>Texas</option><option>Virginia</option><option>Colorado</option><option value="other">Another state</option>
            </select>
          </div>
        </div>
        <div class="field">
          <label for="c-msg">What brings you here</label>
          <textarea id="c-msg" name="message" required placeholder="A sentence or two is plenty."></textarea>
          <p class="note">Please keep this general and leave out sensitive health details. This form is not a secure or HIPAA compliant channel.</p>
        </div>
        <div class="field">
          <label style="text-transform:none;letter-spacing:0;font-weight:400;font-size:.94rem;display:flex;gap:.7rem;align-items:flex-start;color:var(--bark-2)">
            <input type="checkbox" required id="c-ack" style="margin-top:.3rem">
            <span>I understand this form is for general inquiries, is not confidential, and is not for emergencies.</span>
          </label>
        </div>
        <input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
        <button class="submit" type="submit">Send it</button>
        <div class="status" id="contactStatus" role="status"></div>
      </form>
    </div>
    <aside class="details rise" data-d="1">
      <dl>
        <dt>Sessions</dt><dd>Online only. Individuals, families, and groups. Teens through elders.</dd>
        <dt>Licensed in</dt><dd>Texas, license 86566. Virginia. Colorado.</dd>
        <dt>Investment</dt><dd>$175 individual, $200 couples. A limited sliding scale is available, please ask.</dd>
        <dt>Insurance</dt><dd>Aetna, Anthem, BlueCross BlueShield, Cigna and Evernorth, UnitedHealthcare and Optum, select EAPs, and out of network.</dd>
        <dt>Phone</dt><dd><a href="tel:+13465509348">(346) 550 9348</a></dd>
      </dl>
      <div class="urgent">
        <b>If you are in crisis, please do not wait on this form.</b>
        Call or text <a href="tel:988">988</a> for the Suicide and Crisis Lifeline, or call 911.
        Messages here are answered during business hours and are not monitored for emergencies.
      </div>
    </aside>
  </div>
</section>

</main>

<div class="greenhouse">
  <img src="__GREENHOUSE__" alt="Watercolour of a sunlit greenhouse full of potted plants, with a monarch at the window" loading="lazy">
  
</div>

<footer>
  <div class="shell">
    <p class="foot-mark">Bloom<i>&amp;</i>Rise</p>
    <div class="foot-cols">
      <div>
        <h4>The practice</h4>
        <p style="margin:0;max-width:34ch">Roshunda M. Hartison, MEd, LPC. Online therapy for Texas, Virginia, and Colorado. Creative workshops for everywhere else.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="#becoming">Becoming</a></li>
          <li><a href="#work">What it feels like</a></li>
          <li><a href="#about">About Roshunda</a></li>
          <li><a href="#shops">Workshops and groups</a></li>
          <li><a href="#contact">Book a consult</a></li>
        </ul>
      </div>
      <div>
        <h4>Elsewhere</h4>
        <ul>
          <li><a href="https://www.evolvingthruart.com/" target="_blank" rel="noopener">Evolving Thru Art Inc.</a></li>
          <li><a href="tel:+13465509348">(346) 550 9348</a></li>
        </ul>
      </div>
    </div>
    <div class="fine">
      <p><b>Scope of practice.</b> Roshunda M. Hartison is a Licensed Professional Counselor in Texas (license 86566), Virginia, and Colorado. Therapy services are available only to clients physically located in one of those states at the time of session. Workshops, classes, and creative programming are educational, are open to participants anywhere, and do not constitute therapy, a therapeutic relationship, or medical advice.</p>
      <p><b>Not an emergency service.</b> This website and its forms are not monitored continuously and are not appropriate for urgent or crisis needs. If you are in danger or thinking about harming yourself, call or text 988, or call 911.</p>
      <p>Information submitted through this site is not encrypted and is not a HIPAA secure channel. Please do not send protected health information. Content here is general information only and is not a substitute for individualized clinical care.</p>
      <p class="full">&copy; <span id="yr">2026</span> Bloom &amp; Rise. <a href="#">Privacy</a> &middot; <a href="#">Good Faith Estimate</a> &middot; <a href="#">Accessibility</a></p>
    </div>
  </div>
</footer>


<script>
(function(){
  'use strict';
  document.getElementById('yr').textContent = new Date().getFullYear();

  var nav=document.getElementById('nav'), burger=document.getElementById('burger'), navr=document.getElementById('navr');
  addEventListener('scroll',function(){nav.classList.toggle('stuck',scrollY>40)},{passive:true});
  burger.addEventListener('click',function(){var o=navr.classList.toggle('open');burger.setAttribute('aria-expanded',String(o))});
  navr.addEventListener('click',function(e){if(e.target.tagName==='A'){navr.classList.remove('open');burger.setAttribute('aria-expanded','false')}});

  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.15,rootMargin:'0px 0px -8% 0px'});
  document.querySelectorAll('.rise').forEach(function(el){io.observe(el)});

  /* ---- the line drawing reveals as if a pen were moving across it ---- */
  var ink = document.getElementById('ink'), meta = document.getElementById('becoming');
  var slow = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(ink && meta && !slow){
    var tick=false;
    function draw(){
      var r = meta.getBoundingClientRect();
      var t = (innerHeight - r.top) / (innerHeight + r.height);
      t = Math.max(0, Math.min(1, (t - .10) / .42));
      ink.style.clipPath = 'inset(0 ' + ((1 - t) * 100).toFixed(2) + '% 0 0)';
      tick=false;
    }
    addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(draw)}},{passive:true});
    addEventListener('resize',draw,{passive:true});
    draw();
  } else if(ink){ ink.style.clipPath='none' }

  /* ---- the light outside, on the visitor's own clock ---- */
  (function(){
    /* anchors round the clock, so the page warms and cools with the day */
    var KEY = [
      [ 0,'#3A2038','#5A2A46'], [ 5,'#5A2C3A','#8A3A22'],
      [ 7,'#9A4413','#C2611F'], [11,'#8A4A1E','#A85A22'],
      [16,'#A8481A','#D9762F'], [19,'#B4551C','#8A3A55'],
      [21,'#5A2A46','#7A3050'], [24,'#3A2038','#5A2A46']
    ];
    function hex(c){return [parseInt(c.substr(1,2),16),parseInt(c.substr(3,2),16),parseInt(c.substr(5,2),16)]}
    function mix(a,b,t){var A=hex(a),B=hex(b);return 'rgb('+A.map(function(v,i){return Math.round(v+(B[i]-v)*t)}).join(',')+')'}
    function foot(h){
      for(var i=0;i<KEY.length-1;i++){
        if(h>=KEY[i][0] && h<KEY[i+1][0]){
          var t=(h-KEY[i][0])/(KEY[i+1][0]-KEY[i][0]);
          return [mix(KEY[i][1],KEY[i+1][1],t), mix(KEY[i][2],KEY[i+1][2],t)];
        }
      }
      return [KEY[0][1],KEY[0][2]];
    }

    /* which panel of the triptych is true right now */
    function panel(h){ return (h>=5 && h<10) ? 1 : (h>=10 && h<17) ? 2 : 3 }
    var WORD = {
      1:['First light where you are.',            'Early morning in %s.'],
      2:['Full daylight where you are.',          'The middle of the day in %s.'],
      3:['The last of the light where you are.',  'Evening in %s.']
    };

    var imgs = [null,document.getElementById('sky1'),document.getElementById('sky2'),document.getElementById('sky3')];
    var now  = document.getElementById('skyNow');
    var wrap = document.getElementById('states');
    if(!imgs[1] || !wrap) return;

    function hourIn(tz){
      var s = new Intl.DateTimeFormat('en-US',{timeZone:tz,hour:'numeric',minute:'numeric',hour12:false}).formatToParts(new Date());
      var o = {}; s.forEach(function(p){o[p.type]=p.value});
      return (+o.hour % 24) + (+o.minute)/60;
    }
    function clock(tz){
      return new Intl.DateTimeFormat('en-US',{timeZone:tz,hour:'numeric',minute:'2-digit'}).format(new Date());
    }

    var btns = [].slice.call(wrap.querySelectorAll('button'));
    function show(h,label){
      var p = panel(h);
      for(var i=1;i<=3;i++) imgs[i].classList.toggle('on', i===p);
      now.textContent = label ? WORD[p][1].replace('%s',label) : WORD[p][0];
      var f = foot(h);
      document.documentElement.style.setProperty('--foot',  f[0]);
      document.documentElement.style.setProperty('--foot-2',f[1]);
    }

    var here = null;
    function refresh(){
      btns.forEach(function(b){
        b.querySelector('small').textContent = clock(b.dataset.tz);
      });
      if(here === null) show(hourIn(Intl.DateTimeFormat().resolvedOptions().timeZone || 'America/Chicago'));
    }
    btns.forEach(function(b){
      b.addEventListener('click',function(){
        var on = b.getAttribute('aria-pressed') === 'true';
        btns.forEach(function(x){x.setAttribute('aria-pressed','false')});
        if(on){ here=null; show(hourIn(Intl.DateTimeFormat().resolvedOptions().timeZone||'America/Chicago')); return }
        b.setAttribute('aria-pressed','true');
        here = b.dataset.tz;
        show(hourIn(here), b.childNodes[0].nodeValue.trim());
      });
    });
    refresh();
    setInterval(refresh, 30000);
  })();

  function wire(fid,sid,msg){
    var f=document.getElementById(fid), s=document.getElementById(sid);
    if(!f||!s) return;
    f.addEventListener('submit',function(e){
      e.preventDefault();
      if(f.querySelector('[name="website"]').value) return;
      if(!f.checkValidity()){f.reportValidity();return}
      s.textContent=msg; s.classList.add('on');
      f.querySelector('button.submit').disabled=true;
    });
  }
  wire('contactForm','contactStatus','Received. This is a mockup, so nothing was actually sent. On the live site this would reach Roshunda and she would reply within two business days.');
  wire('interestForm','interestStatus','Noted. Mockup only, nothing sent. On the live site you would be first to hear when dates are set.');
})();
</script>
</body>
</html>
'''

HTML = (HTML.replace('__HERO_ART__', HERO_ART)
            .replace('__STAGE_1__', STAGE_1)
            .replace('__STAGE_2__', STAGE_2)
            .replace('__STAGE_3__', STAGE_3)
            .replace('__GREENHOUSE__', GREENHOUSE)
            .replace('__HAND__', HAND)
            .replace('__FLIT__', FLIT)
            .replace('__BOTANICAL__', BOTANICAL)
            .replace('__SKY_1__', SKY_1)
            .replace('__SKY_2__', SKY_2)
            .replace('__SKY_3__', SKY_3)
            .replace('__SUN__', SUN)
            .replace('__PORTRAIT__', PORTRAIT))

open('bloom-and-rise-home.html','w').write(HTML)
print('written', round(len(HTML)/1024), 'KB')
