import base64, os

def b64(p, mime='image/webp'):
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(p,'rb').read()).decode())

PORTRAIT = b64('source/rosh-plate.webp')

# Watercolour plates supplied by the client
HERO_ART   = b64('source/art-hero.webp')
STAGE_1    = b64('source/art-stage-1.webp')
STAGE_2    = b64('source/art-stage-2.webp')
STAGE_3    = b64('source/art-stage-3.webp')
GREENHOUSE = b64('source/art-greenhouse.webp')

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bloom &amp; Rise — Roshunda M. Hartison, MEd, LPC</title>
<meta name="description" content="Creative, weight inclusive therapy for anxiety, OCD, body image, and self trust. Online sessions in Texas, Virginia, and Colorado.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://images.unsplash.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,300..900,0..100,0..1;1,9..144,300..900,0..100,0..1&family=Inter+Tight:ital,wght@0,300;0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<style>
:root{
  /* drawn from the watercolours: monarch orange, leaf green, coneflower pink, morning yellow */
  --orange:#D9762F; --orange-deep:#B4551C; --orange-lit:#E8934A;
  --leaf:#5E7A4F; --leaf-deep:#3C5236; --leaf-soft:#A8BE9B;
  --pink:#C77BA6; --pink-soft:#E6BBD2;
  --sun:#F0D28A; --sun-soft:#F8ECC8;

  /* paper */
  --paper:#F7F0E3; --paper-2:#F1E8D8; --paper-3:#EAE0CC;
  --bark:#3A3227; --bark-2:#6B6152; --bark-3:#948B7A;

  --maxw:1240px; --gut:clamp(1.25rem,4vw,3.5rem);
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
.nav-r{display:flex;align-items:center;gap:2.2rem}
.nav-r a:not(.cta){text-decoration:none;font-size:.94rem;font-weight:500;color:var(--bark-2);position:relative;padding:.2rem 0}
.nav-r a:not(.cta)::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;background:var(--orange);transform:scaleX(0);transform-origin:right;transition:transform .4s cubic-bezier(.2,.7,.3,1)}
.nav-r a:not(.cta):hover::after{transform:scaleX(1);transform-origin:left}
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

/* ---------------- hero: a plate on paper ---------------- */
.hero{position:relative;padding:9.5rem 0 clamp(2rem,5vw,3.5rem);background:var(--paper);overflow:hidden}
@media (max-width:640px){.hero{padding-top:7.5rem}.hero-plate{max-height:46vh;overflow:hidden}.hero-plate img{height:46vh;object-fit:cover;object-position:60% 45%}}
/* first light, coming in from the upper right */
.hero::before{
  content:"";position:absolute;z-index:0;pointer-events:none;
  top:-32%;right:-14%;width:min(78vw,1020px);aspect-ratio:1;border-radius:50%;
  background:radial-gradient(circle, rgba(255,224,150,.62) 0%, rgba(250,206,128,.34) 38%, rgba(247,240,227,0) 70%);
}
.hero > .shell{position:relative;z-index:1}
.hero-top{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:clamp(1.5rem,5vw,4rem);align-items:end;margin-bottom:clamp(2rem,4vw,3.2rem)}
@media (max-width:880px){.hero-top{grid-template-columns:1fr;align-items:start;gap:1.5rem}}
.hero h1{color:var(--bark);max-width:13ch}
.hero h1 .lit{font-style:italic;color:var(--orange-deep)}
.hero-lede{font-size:clamp(1.02rem,1.25vw,1.2rem);color:var(--bark-2);max-width:42ch;margin:0 0 .3rem}
.hero-meta{font-size:.86rem;color:var(--bark-2);margin:clamp(1.2rem,2.5vw,1.8rem) 0 0;display:flex;flex-wrap:wrap;gap:.2rem .9rem;align-items:baseline}
.hero-meta strong{color:var(--bark);font-weight:600}
.hero-meta span::before{content:"";display:inline-block;width:14px;height:1px;background:var(--orange);margin-right:.7rem;vertical-align:.32em}

/* every illustration sits in a plate, echoing the rule inside the artwork */
.plate{position:relative;background:var(--paper)}
.plate img{width:100%;height:auto;display:block}
.hero-plate{overflow:hidden;position:relative}
.hero-plate::after{
  content:"";position:absolute;inset:0;pointer-events:none;mix-blend-mode:soft-light;
  background:
    radial-gradient(58% 62% at 80% 16%, rgba(255,232,170,.95) 0%, rgba(255,222,150,.42) 34%, rgba(255,255,255,0) 68%),
    linear-gradient(112deg, rgba(120,140,110,.16) 0%, rgba(255,255,255,0) 42%);
}
.hero-plate::before{
  content:"";position:absolute;z-index:2;inset:0;pointer-events:none;
  background:radial-gradient(38% 44% at 82% 14%, rgba(255,236,186,.42), rgba(255,236,186,0) 68%);
}
.hero-plate img{animation:plateIn 1.8s cubic-bezier(.16,.8,.3,1) both}
@keyframes plateIn{from{opacity:0;transform:scale(1.04)}to{opacity:1;transform:none}}
.plate-cap{display:flex;justify-content:space-between;gap:1rem;margin-top:.85rem;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--bark-3)}

/* ---------------- opening statement ---------------- */
.intro{padding:clamp(4.5rem,10vw,8.5rem) 0}
.intro-grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:clamp(2rem,6vw,5rem);align-items:start}
@media (max-width:880px){.intro-grid{grid-template-columns:1fr}}
.quote{font-family:'Fraunces',serif;font-variation-settings:'SOFT' 70,'WONK' 1;font-size:clamp(1.85rem,4.1vw,3.4rem);line-height:1.09;letter-spacing:-.03em;max-width:20ch;margin:0}
.quote .hl{background:linear-gradient(180deg,transparent 58%,rgba(255,176,31,.55) 58%)}
.intro-body{display:grid;gap:1.4rem;padding-top:.6rem}
.intro-body p{color:var(--bark-2);font-size:1.05rem;margin:0}

/* ---------------- metamorphosis ---------------- */
.meta{background:linear-gradient(180deg,#EFEDDC,#E9EBD6);color:var(--bark);padding:clamp(4.5rem,10vw,8rem) 0}
.meta h2{color:var(--bark);max-width:15ch}
.meta-head{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:clamp(1.5rem,5vw,4rem);align-items:end;margin-bottom:clamp(2.5rem,5vw,4rem)}
@media (max-width:820px){.meta-head{grid-template-columns:1fr;align-items:start}}
.meta-head p{color:var(--bark-2);margin:0 0 .4rem;max-width:40ch}
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

/* ---------------- numbered work list ---------------- */
.work{background:var(--paper);padding:clamp(4rem,9vw,7.5rem) 0}
.work-head{display:flex;flex-wrap:wrap;align-items:end;justify-content:space-between;gap:2rem;margin-bottom:clamp(2.5rem,5vw,4rem)}
.work-head p{color:var(--bark-2);max-width:38ch;margin:0}
.rows{border-top:1px solid rgba(28,17,19,.18)}
.row{position:relative;display:grid;grid-template-columns:5rem minmax(0,1fr) minmax(0,1.15fr);gap:clamp(1rem,3vw,2.5rem);align-items:start;padding:clamp(1.6rem,3.4vw,2.6rem) 0;border-bottom:1px solid rgba(28,17,19,.18);transition:padding-left .5s cubic-bezier(.2,.7,.3,1)}
.row::before{content:"";position:absolute;inset:0 -1.5rem;z-index:-1;background:var(--tint,var(--orange));opacity:0;transition:opacity .5s}
.row:hover::before{opacity:.09}
.row:hover{padding-left:1.5rem}
.row-num{font-family:'Fraunces',serif;font-size:.98rem;color:var(--tint,var(--orange));letter-spacing:.04em;padding-top:.42rem;font-weight:600}
.row h3{max-width:16ch}
.row p{color:var(--bark-2);margin:0;font-size:1.02rem}
@media (max-width:820px){.row{grid-template-columns:3rem 1fr}.row p{grid-column:2}}

/* ---------------- about ---------------- */
.about{padding:clamp(4.5rem,10vw,8rem) 0;background:var(--paper)}
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
.shops{background:var(--paper-2);padding:clamp(4.5rem,10vw,8rem) 0}
.shops-head{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:clamp(1.5rem,5vw,4rem);align-items:end;margin-bottom:clamp(2.5rem,5vw,4rem)}
.shops-head h2{max-width:15ch}
.shops-head p{color:var(--bark-2);margin:0 0 .4rem;max-width:36ch}
@media (max-width:820px){.shops-head{grid-template-columns:1fr;align-items:start}}
.shop-list{border-top:1px solid rgba(28,17,19,.18)}
.shop{padding:clamp(1.6rem,3.4vw,2.4rem) 0;border-bottom:1px solid rgba(28,17,19,.18);display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr) auto;gap:clamp(1rem,3vw,2.5rem);align-items:center;transition:padding-left .5s cubic-bezier(.2,.7,.3,1)}
.shop:hover{padding-left:1.2rem}
.shop p{margin:0;color:var(--bark-2);font-size:1rem}
.tag{font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;font-weight:600;white-space:nowrap;padding:.3rem 0 .32rem;border-bottom:1.5px solid currentColor}
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
.opts{display:flex;flex-wrap:wrap;gap:.5rem;margin:.2rem 0 1.6rem}
.opts label{text-transform:none;letter-spacing:0;font-size:.94rem;font-weight:400;margin:0;display:inline-flex;align-items:center;gap:.55rem;cursor:pointer;border:1px solid rgba(58,50,39,.26);border-radius:0;padding:.55rem 1rem;transition:.3s;color:var(--bark)}
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
.signup{background:var(--leaf-deep);color:var(--paper);border-radius:0;padding:clamp(1.75rem,4vw,3.5rem);margin-top:clamp(2.5rem,5vw,4rem);display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:clamp(1.5rem,5vw,4rem);align-items:start}
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
.contact{padding:clamp(4.5rem,10vw,9rem) 0 clamp(3.5rem,7vw,6rem);background:var(--paper)}
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

/* ---------------- footer ---------------- */
.greenhouse{position:relative;background:var(--paper-2);overflow:hidden}
.greenhouse img{width:100%;height:clamp(200px,38vh,520px);object-fit:cover;object-position:50% 46%;display:block}
.greenhouse::after{
  content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,var(--paper-2) 0%,rgba(245,238,221,0) 22%,rgba(245,238,221,0) 58%,rgba(60,82,54,.55) 88%,var(--leaf-deep) 100%);
}
.greenhouse-line{
  position:absolute;left:0;right:0;bottom:clamp(1.5rem,4vw,3rem);z-index:2;text-align:center;
  font-family:'Fraunces',serif;font-variation-settings:'SOFT' 80,'WONK' 1;font-style:italic;
  font-size:clamp(1.2rem,2.6vw,2rem);color:#FBF6EA;text-shadow:0 2px 24px rgba(30,42,26,.6);
  margin:0;padding-inline:var(--gut);
}
footer{background:var(--leaf-deep);color:rgba(251,246,234,.68);padding:clamp(3.5rem,7vw,5.5rem) 0 3rem;font-size:.92rem}
.foot-mark{font-family:'Fraunces',serif;font-variation-settings:'SOFT' 60,'WONK' 1;font-size:clamp(2.8rem,10vw,7.5rem);line-height:.86;letter-spacing:-.045em;color:#FBF6EA;margin:0 0 2.5rem}
.foot-mark i{font-style:italic;color:var(--orange-lit)}
.foot-cols{display:grid;grid-template-columns:1.5fr 1fr 1fr;gap:2.5rem;padding-bottom:3rem;border-bottom:1px solid rgba(251,246,234,.18)}
@media (max-width:760px){.foot-cols{grid-template-columns:1fr}}
.foot-cols h4{font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--sun);font-weight:600;margin:0 0 1rem}
.foot-cols ul{list-style:none;padding:0;margin:0}
.foot-cols li{margin-bottom:.6rem}
.foot-cols a{text-decoration:none;transition:color .3s}
.foot-cols a:hover{color:var(--sun)}
.fine{padding-top:2.5rem;font-size:.81rem;line-height:1.72;color:rgba(251,246,234,.5);display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.4rem 3rem}
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
      <a href="#work">The work</a>
      <a href="#about">Roshunda</a>
      <a href="#shops">Workshops</a>
      <a class="cta" href="#contact"><span class="dot"></span>Book a consult</a>
    </div>
  </div>
</nav>

<main id="main">

<header class="hero" id="top">
  <div class="shell">
    <div class="hero-top">
      <h1>You don't have to have it figured out <span class="lit">to begin.</span></h1>
      <p class="hero-lede">
        Creative, weight inclusive therapy for the people who hold everyone else together.
        Anxiety, OCD, body image, self trust, and the slow unglamorous work of becoming who you are.
      </p>
    </div>

    <figure class="plate hero-plate" style="margin:0">
      <img src="__HERO_ART__" alt="Watercolour of a monarch butterfly among green leaves" fetchpriority="high">
    </figure>

    <p class="hero-meta">
      <strong>Roshunda M. Hartison, MEd, LPC</strong>
      <span>Online sessions for Texas, Virginia, and Colorado</span>
    </p>
  </div>
</header>

<section class="intro">
  <div class="shell intro-grid">
    <blockquote class="quote rise">
      Showing up for yourself is powerful. You <span class="hl">shouldn't have to</span> do it alone.
    </blockquote>
    <div class="intro-body">
      <p class="rise" data-d="1">
        Maybe you are tired of second guessing yourself. Maybe you have been putting everyone
        else first for so long that you have lost the thread of what you actually want.
        Maybe the thoughts have gotten loud enough that they are running the day.
      </p>
      <p class="rise" data-d="2">
        Therapy here is supportive, collaborative, and active. We look at the patterns keeping
        you stuck, challenge the anxious thinking, and practice new ways of responding.
        When words are not enough, we reach for color and sound and making instead.
        Some weeks that is the whole session, and it still counts as movement toward morning.
      </p>
    </div>
  </div>
</section>

<section class="meta" id="becoming">
  <div class="shell">
    <div class="meta-head">
      <h2 class="rise">The cocoon is not a waiting room.</h2>
      <p class="rise" data-d="1">
        Metamorphosis gets sold as a before and after photo. It is not. The middle is dark,
        disorienting, and longer than anyone warns you. That middle is most of the work,
        and the light on the other side arrives the way light actually arrives, slowly.
      </p>
    </div>

    <div class="stages">
      <figure class="stage rise">
        <div class="plate"><img src="__STAGE_1__" alt="Watercolour of a monarch chrysalis hanging from a milkweed stem" loading="lazy"></div>
        <figcaption>
          <span class="n">One</span>
          <h3>The folding in</h3>
          <p>Where you stop performing fine. We name what is actually happening and take the weight of it seriously.</p>
        </figcaption>
      </figure>
      <figure class="stage rise" data-d="1">
        <div class="plate"><img src="__STAGE_2__" alt="Watercolour of a monarch emerging from its chrysalis" loading="lazy"></div>
        <figcaption>
          <span class="n">Two</span>
          <h3>The hard middle</h3>
          <p>Sitting with the discomfort instead of running from it. This is where exposure work, and most real change, actually lives.</p>
        </figcaption>
      </figure>
      <figure class="stage rise" data-d="2">
        <div class="plate"><img src="__STAGE_3__" alt="Watercolour of a monarch resting on a coneflower" loading="lazy"></div>
        <figcaption>
          <span class="n">Three</span>
          <h3>First light</h3>
          <p>Not a finished person. A rested one, who trusts herself more than she did, and knows what to do the next time it gets loud.</p>
        </figcaption>
      </figure>
    </div>

    <p class="meta-note rise">
      <b>A caterpillar does not improve into a butterfly.</b>
      It dissolves first. Becoming who you are is less about adding good habits on top of who you
      have been, and more about letting the shape you were handed come apart so something truer
      can set. That part is uncomfortable. It is also the point. And what comes after is not a
      spotlight, it is a sunrise. Slow, ordinary, and impossible to miss once it starts.
      You do not have to sit through the dark part by yourself.
    </p>
  </div>
</section>

<section class="work" id="work">
  <div class="shell">
    <div class="work-head">
      <h2 class="rise">Different doors,<br>the same room.</h2>
      <p class="rise" data-d="1">Most people arrive through one of these. Almost everyone finds the others waiting inside it.</p>
    </div>
    <div class="rows">
      <article class="row rise" style="--tint:#C93A0C">
        <span class="row-num">01</span>
        <h3>OCD and anxiety</h3>
        <p>Exposure and Response Prevention, with full transparency about what the work asks of you. Together we pick apart what is OCD and what is actually you.</p>
      </article>
      <article class="row rise" style="--tint:#FF5A1F">
        <span class="row-num">02</span>
        <h3>Body image and food</h3>
        <p>Weight inclusive care. The goal is not a smaller body. It is a life you are present for, and a truce with the one you are in.</p>
      </article>
      <article class="row rise" style="--tint:#FFB01F">
        <span class="row-num">03</span>
        <h3>Self esteem and women's issues</h3>
        <p>For the second guessers and the everyone else firsters. We connect the messages you have been carrying to the person you are becoming.</p>
      </article>
      <article class="row rise" style="--tint:#0B5F52">
        <span class="row-num">04</span>
        <h3>Life transitions</h3>
        <p>New season, new city, new body, new role, or just the quiet realization that the old shape does not fit anymore.</p>
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
      <h2 class="rise">Warmth, humor, transparency, and a lot of color.</h2>
      <p class="rise" data-d="1">
        I am Roshunda. A Licensed Professional Counselor, an educator, a musician, and a maker
        of things. I have worked in community health, domestic violence shelters, juvenile
        detention, and alongside people managing OCD. All of it taught me the same lesson.
        Meet people exactly where they are, and honor how much courage it takes to ask for help.
      </p>
      <p class="rise" data-d="2">
        You can show up exactly as you are, mid transformation and unfinished, on the days it
        feels like progress and on the ones that feel like nothing at all. We will make room for
        the hard stuff, notice the light when it turns, and probably laugh along the way.
      </p>
      <p class="sig rise" data-d="2">Roshunda M. Hartison, MEd, LPC</p>
      <ul class="facts rise" data-d="3">
        <li><b>Licensed in</b><span>Texas, Virginia, and Colorado</span></li>
        <li><b>Education</b><span>MEd Clinical Counseling, University of Houston Victoria</span></li>
        <li><b>Also</b><span>Founder of Evolving Thru Art Inc.</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="shops" id="shops">
  <div class="shell">
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
        A free fifteen minute consult, no pressure attached. Ask me anything, including the awkward questions. Beginning is the only part you have to do today.
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
  <p class="greenhouse-line">Somewhere warm to grow, with the door left open.</p>
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
          <li><a href="#work">The work</a></li>
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

  /* the page warms as you scroll, night into morning */
  var body=document.body, tick=false;
  function paint(){
    var max=document.documentElement.scrollHeight-innerHeight;
    var t=max>0?Math.min(1,scrollY/max):0;
    body.style.setProperty('--cream','hsl('+(33-t*4)+' '+(62+t*12)+'% '+(95-t*3)+'%)');
    body.style.setProperty('--cream-warm','hsl('+(30-t*4)+' '+(63+t*12)+'% '+(90-t*3)+'%)');
  }
  addEventListener('scroll',function(){if(tick)return;tick=true;requestAnimationFrame(function(){paint();tick=false})},{passive:true});
  paint();

  function wire(fid,sid,msg){
    var f=document.getElementById(fid), s=document.getElementById(sid);
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
            .replace('__PORTRAIT__', PORTRAIT))

open('bloom-and-rise-home.html','w').write(HTML)
print('written', round(len(HTML)/1024), 'KB')
