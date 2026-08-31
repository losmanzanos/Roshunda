# Builds the pages that are not slices of the home page: services, the five
# individual service pages, the FAQ, and the four legal pages.
import re

UPDATED = 'Last updated <span class="todo">[DATE]</span>'

# ---------------------------------------------------------------- services --

SERVICES = [
 dict(f='anxiety.html', wash='#FBEDE0', tint='#B4551C', n='01',
  nm='Anxiety and overwhelm',
  blurb='For when your baseline is bracing, and rest feels like something you have to earn.',
  h1='Anxiety and <i>overwhelm</i>',
  lede='You are functional. You are also exhausted. Anxiety that looks like competence from '
       'the outside is still anxiety, and it still costs you something every day.',
  body=[
   ('What this looks like', """
<p>Most people who come to Roshunda for anxiety are not falling apart in any way other
people can see. They are the ones who answer the message, cover the shift, remember the
birthday. The anxiety shows up underneath that: the replaying of a conversation for three
days, the tightness that arrives before the alarm does, the sense that if you stopped
managing everything for a week it would all come down.</p>
<p>Some of what people bring here:</p>
<ul>
<li>Waking up already behind, or already braced</li>
<li>Overthinking a decision so thoroughly that you never make it</li>
<li>Physical symptoms with no medical cause, or a medical cause that has been ruled out twice</li>
<li>Saying yes and then resenting it, then feeling guilty about the resentment</li>
<li>Rest that does not restore anything, because you spend it worrying about what you are not doing</li>
</ul>"""),
   ('How the work goes', """
<p>Early on, the work is mostly about accuracy. Anxiety is very good at presenting a
guess as a fact, and a lot of the first few sessions is separating what actually happened
from what your nervous system concluded about it.</p>
<p>From there it gets practical. We look at the specific situations that spike you, what
you do to bring the spike down, and whether those strategies are helping or quietly making
the next spike bigger. Avoidance is usually the honest answer, and it is usually not a
character flaw. It worked once. It is just expensive now.</p>
<p>Roshunda works from a cognitive behavioral base with exposure and response prevention
where it fits, plus mindfulness and somatic work when talking about it is not getting there.
If you are someone who thinks in images or sound rather than sentences, the art and music
side of her practice is available too, and it is not a consolation prize.</p>"""),
   ('What changes', """
<p>Realistically: the anxiety does not vanish. What changes is how much of your day it gets
to run. People finish this work able to notice the alarm going off without treating it as
information, make a decision without needing certainty first, and stop paying the tax of
constant preemptive management.</p>"""),
  ]),

 dict(f='ocd.html', wash='#FCF0E2', tint='#D9762F', n='02',
  nm='OCD and intrusive thoughts',
  blurb='Evidence based OCD treatment, including exposure and response prevention.',
  h1='OCD and <i>intrusive thoughts</i>',
  lede='The thought is not the problem. The deal you have made with the thought is the '
       'problem, and that deal is treatable.',
  body=[
   ('What OCD actually is', """
<p>OCD is badly served by the way it gets talked about. It is not tidiness and it is not a
personality trait. It is a loop: an intrusive thought, image, or urge arrives, it lands as
unbearable, and you do something to make the feeling stop. The thing you do works, briefly.
Doing it teaches your brain that the thought was in fact dangerous, so the thought comes
back louder. That is the whole mechanism.</p>
<p>The compulsion is not always visible. A lot of OCD is entirely internal: mental review,
silent reassurance, counting, praying to undo, checking your own body for a feeling.
Roshunda works with all of it, including the themes people are most afraid to say out loud.
Harm, contamination, relationships, religion and morality, sexuality, health. She has heard
them. She will not be alarmed.</p>"""),
   ('Exposure and response prevention', """
<p>ERP is the treatment with the strongest evidence behind it, and it is the core of this
work. In plain terms: you deliberately move toward the thing that triggers the thought, and
you do not perform the compulsion afterward. Your brain gets to learn, from experience
rather than from argument, that the feeling passes on its own.</p>
<p>It is uncomfortable and it is collaborative. You are not ambushed. You and Roshunda build
the ladder together, you decide the pace, and you start somewhere you can actually do. She
has treated OCD both in private practice and through NOCD, so this is routine work for her
rather than an occasional case.</p>
<p><b>One thing worth saying plainly.</b> If you have been told your thoughts mean something
about who you are, that was wrong. People with OCD are, as a group, notable for how much
they do not want to do the thing they are afraid of. That is why it sticks.</p>"""),
   ('If you have tried therapy before', """
<p>A lot of people with OCD have already done a round of talk therapy that made things
slightly worse, usually because a well meaning therapist offered reassurance, which is the
compulsion in a nicer outfit. If that was your experience, it does not mean treatment does
not work on you. It means you have not had this treatment yet.</p>"""),
  ]),

 dict(f='body-image.html', wash='#F9E9F1', tint='#C77BA6', n='03',
  nm='Body image, food, and weight inclusive care',
  blurb='Weight inclusive work on body image, eating, and being in a body at all.',
  h1='Body image and <i>being in a body</i>',
  lede='Weight inclusive means the goal is not a smaller body. The goal is a life that is '
       'not organized around one.',
  body=[
   ('Where this starts', """
<p>Most people arrive having already tried to fix this by changing the body. Sometimes for
decades. Sometimes successfully, and then it came back, and the coming back felt like proof
of something about them. That is the part worth treating.</p>
<p>This work is weight inclusive. That means Roshunda does not treat body size as a symptom
to be corrected, does not set weight loss as a therapeutic goal, and does not use your body
as evidence about your discipline, health, or worth. What gets treated is the distress,
the preoccupation, and the rules.</p>"""),
   ('What we work on', """
<ul>
<li>The running commentary, and how much of your attention it takes</li>
<li>Food rules, and the rebound that follows breaking them</li>
<li>Avoiding photographs, mirrors, swimming, intimacy, medical care</li>
<li>Comparison, and the specific way it spikes online</li>
<li>Being on the receiving end of other people's comments, including from family and from doctors</li>
<li>Grief, when you are letting go of a body you spent years trying to have</li>
</ul>
<p>For some people this overlaps with disordered eating. Roshunda will be direct with you
about scope. If what you need is a treatment team with medical and nutritional support,
she will say so and help you find it rather than working around the edge of something that
needs more.</p>"""),
   ('The identity part', """
<p>Body image work is rarely only about the body. It usually turns out to be about being
looked at, being judged, taking up space, and who taught you that you needed permission.
That is where this work tends to go, and it is the part that holds after the noise settles.</p>"""),
  ]),

 dict(f='identity.html', wash='#F1E7EC', tint='#5F2A46', n='04',
  nm='Identity, self trust, and life transitions',
  blurb='For the stretch between who you were and who you are turning into.',
  h1='Identity and <i>self trust</i>',
  lede='You can be doing everything right and still not recognize the life you built. '
       'That is not ingratitude. That is information.',
  body=[
   ('The middle stretch', """
<p>Some people come in with a symptom. Others come in with a question, and the question is
usually some version of: who am I when I stop being useful to everyone.</p>
<p>This shows up around real events, and the events are often ones you are supposed to be
happy about. A promotion. A move. A wedding. A degree. The kids getting old enough not to
need you the same way. It also shows up with no event at all, which is more disorienting,
because there is nothing to point at.</p>"""),
   ('Self trust specifically', """
<p>A great many people can list what everyone else in their life wants and cannot answer
what they want. If you learned early that reading the room kept you safe, or kept someone
else calm, you got very good at a skill that is now running without your permission.</p>
<p>The work here is slow and it is worth it. We look at where your read on things got
overridden, how you learned to check with other people before you check with yourself, and
what it takes to rebuild a working relationship with your own judgment. Roshunda is direct
in this work. She will not simply mirror you back at yourself for a year.</p>"""),
   ('Who this tends to be for', """
<p>Roshunda works often with Black women, with first generation professionals, with
caregivers, and with people who have been the reliable one in a family system since they
were young. Not exclusively. But if you have been carrying something for a long time and
have never been asked what it costs, this is that conversation.</p>"""),
  ]),

 dict(f='creative-therapy.html', wash='#EAF0E2', tint='#5E7A4F', n='05',
  nm='Creative and expressive work',
  blurb='Art, color, and sound in session, for the weeks when words are not getting there.',
  h1='When words <i>run out</i>',
  lede='Roshunda is a working artist and musician. That is not a hobby she mentions in her '
       'bio. It is a tool she uses in the room.',
  body=[
   ('Why this exists', """
<p>There is a certain kind of week where talking about it does not do anything. You can
describe the situation accurately, in order, with insight, and leave the session exactly as
you came in. Sometimes the material is preverbal. Sometimes you have told the story so many
times that the words have worn smooth and stopped carrying anything.</p>
<p>For those weeks there is another way in. Color, mark making, sound, movement on paper.
You do not need to be able to draw. Nobody is assessing the work. The point is that making
something gets at material that explaining it does not.</p>"""),
   ('What it looks like in practice', """
<p>This is not a separate service you book instead of therapy. It is a mode inside the
therapy, available when it is useful, and it is always your call. Some clients never use
it. Some use it for one session in a hard month. Some find it is the only thing that moves
anything and build most of their work around it.</p>
<p>Everything happens over video, so materials are whatever you have. Printer paper and a
pen is enough. Roshunda will tell you if something else would help.</p>"""),
   ('The wider work', """
<p>Roshunda also runs <a href="https://www.evolvingthruart.com/" target="_blank" rel="noopener">Evolving Thru Art</a>,
which brings creative programming to communities outside a therapy office entirely. If you
are looking for that rather than for individual therapy, the
<a href="workshops.html">workshops and groups</a> page is the better door, and those are
open to people in any state.</p>"""),
  ]),
]

SVC_INDEX = ('<a class="svc rise" href="%(f)s" style="--tint:%(tint)s">'
             '<span class="n">%(n)s</span>'
             '<h3>%(nm)s</h3>'
             '<p>%(blurb)s</p>'
             '<span class="go" aria-hidden="true">&rarr;</span></a>')

CONSULT = """
<section class="band alt">
  <span class="botanical left" aria-hidden="true"></span>
  <div class="shell">
    <div class="prose">
      <h2 class="rise">Start with a consult.</h2>
      <div class="prose-body rise" data-d="1">
        <p>A free 15 minute call, no paperwork, no obligation. It exists so you can hear how
        Roshunda thinks and decide whether it fits. If it does not, she will point you
        somewhere that does.</p>
        <p><a class="cta" href="contact.html" style="margin-top:.6rem"><span class="dot"></span>Book a consult</a></p>
      </div>
    </div>
  </div>
</section>"""

# --------------------------------------------------------------------- faq --

FAQ = [
 ('Who can actually work with you?',
  """<p>Therapy clients need to be physically located in <b>Texas, Virginia, or Colorado</b>
  at the time of the session. That is a licensing rule, not a preference. Roshunda is a
  Licensed Professional Counselor in all three.</p>
  <p>Workshops, classes, and creative programming are educational rather than clinical, so
  those are open to anyone anywhere. See <a href="workshops.html">workshops and groups</a>.</p>"""),
 ('Is everything online?',
  """<p>Yes. All sessions are held over a secure video platform. You will get a link before
  each appointment and you do not need to install anything unusual.</p>
  <p>You do need somewhere you can talk without managing who might hear you. A car in a
  parking lot counts. Plenty of good work has happened in a parked car.</p>"""),
 ('What does it cost?',
  """<p>Roshunda's self pay rate is <span class="todo">$[RATE]</span> for a 50 minute
  session. A limited number of <span class="todo">sliding scale</span> spots are available;
  ask on the consult call and she will tell you honestly whether one is open.</p>
  <p>If you are paying out of pocket, you are entitled to a written estimate before you
  start. See <a href="good-faith-estimate.html">Good Faith Estimate</a>.</p>"""),
 ('Do you take insurance?',
  """<p><span class="todo">[Insurance: confirm which plans, and whether via Headway]</span></p>
  <p>If your plan is not accepted directly, many plans reimburse a portion of out of network
  care. Roshunda can provide a superbill, which is an itemized receipt you submit to your
  insurer yourself. Reimbursement is between you and them, and it is worth calling to ask
  what your out of network mental health benefit actually is before you assume there is not one.</p>"""),
 ('How long does this take?',
  """<p>It depends on what you are bringing. Focused OCD work with exposure and response
  prevention often runs a defined course of a few months. Identity and self trust work is
  usually longer and less linear.</p>
  <p>What Roshunda will do is tell you what she thinks the shape of it is, early, and revisit
  that with you rather than letting it drift indefinitely without anyone naming it.</p>"""),
 ('What happens on the free consult?',
  """<p>Fifteen minutes, video or phone. You say what brings you in, in whatever order it
  comes out. She asks some questions, tells you how she would approach it, and answers
  yours. Nobody signs anything.</p>
  <p>It is genuinely fine to use it to decide she is not the right fit. That is what it is for.</p>"""),
 ('What does weight inclusive mean?',
  """<p>It means weight loss is not a goal of the therapy, your body is not treated as a
  problem to be solved, and your size will not be used as evidence about your health or your
  discipline. The work targets distress, preoccupation, and food rules rather than the body.</p>
  <p>More on that on the <a href="body-image.html">body image</a> page.</p>"""),
 ('I have intrusive thoughts I am afraid to say out loud.',
  """<p>Say them. Roshunda treats OCD regularly, including harm, contamination, relationship,
  religious, and sexual themes. She has heard these before and she will not be alarmed by
  yours.</p>
  <p>Having a thought is not the same as wanting it. That distinction is most of the
  treatment. See <a href="ocd.html">OCD and intrusive thoughts</a>.</p>"""),
 ('Are the workshops therapy?',
  """<p>No, and this matters legally as well as practically. Workshops and creative
  programming are educational. Attending one does not make you a client, does not create a
  therapeutic relationship, and is not a substitute for treatment.</p>
  <p>That separation is why workshops can be open nationally while therapy cannot.</p>"""),
 ('What is your cancellation policy?',
  """<p><span class="todo">[Confirm: typically 24 or 48 hours notice, and the fee for a late
  cancel or no show]</span></p>
  <p>Life happens and she is a reasonable person about genuine emergencies. The policy exists
  so that a reserved hour means something.</p>"""),
 ('Is what I say confidential?',
  """<p>Yes, with the limits every licensed therapist works under: risk of serious harm to
  yourself or someone else, suspected abuse or neglect of a child, an older adult, or a
  person with a disability, and a valid court order. Roshunda will go through these with you
  in the first session rather than leaving them in the paperwork.</p>
  <p>Separately, the forms on this website are not a secure channel. Do not send clinical
  detail through them. See <a href="privacy.html">privacy</a>.</p>"""),
 ('What if I am in crisis right now?',
  """<p>This practice is not a crisis service and messages here are not monitored
  continuously. If you are in danger or thinking about harming yourself, call or text
  <b>988</b> for the Suicide and Crisis Lifeline, or call 911.</p>
  <p>If you are not in immediate danger but you are not okay, say that plainly in your
  message and Roshunda will treat it accordingly.</p>"""),
]

# ------------------------------------------------------------------ legal --

DISCLAIM = """
<div class="callout">
  <p><b>For Roshunda, before launch.</b> These pages are a solid, standard starting point,
  not legal advice. Anything highlighted needs a real answer from you, and it is worth
  having your attorney or your liability carrier read the final wording once.</p>
</div>"""

PRIVACY = [
 ('What this covers', """
<p>This notice explains what happens to information you give to this website. It is
separate from the Notice of Privacy Practices you receive as a client, which covers your
protected health information under HIPAA and governs the actual clinical record.</p>
<p><b>Short version.</b> The only information collected here is what you type into a form
and send on purpose. There is no account to create, nothing is sold, and there is no
advertising on this site.</p>"""),
 ('What is collected', """
<h3>Information you send</h3>
<p>The consult form and the workshop interest form collect your name, your email address,
and whatever you write in the message field. That is used to reply to you and, for the
interest list, to tell you when workshop dates are set.</p>
<h3>Information collected automatically</h3>
<p>The site is hosted on <span class="todo">[Cloudflare Pages]</span>, which keeps standard
server logs including IP address, browser type, and pages requested. These are used for
security and reliability. <span class="todo">[If analytics are added later, name the tool
here and say whether it uses cookies.]</span></p>
<p>This site sets no advertising cookies and runs no third party trackers. Web fonts are
loaded from Google Fonts, which means your browser makes a request to Google to fetch them.</p>"""),
 ('Who else touches it', """
<p>Form submissions and email are handled by <span class="todo">[email and form provider,
e.g. Kit and Google Workspace]</span>. Scheduling and the clinical record live in
<span class="todo">[EHR, e.g. SimplePractice]</span>, which is a separate system with its own
protections and its own agreement.</p>
<p>Information is not sold, rented, or traded. It is disclosed only where the law requires
it, or where you have asked for it to be.</p>"""),
 ('Not a secure channel', """
<div class="callout">
<p><b>Please do not send protected health information through this website.</b> The forms
and ordinary email are not encrypted end to end and are not a HIPAA secure channel. Send
enough to get a conversation started. Clinical detail belongs in session or in the secure
client portal.</p>
</div>"""),
 ('Your choices', """
<p>You can ask what is held about you, ask for it to be corrected, or ask for it to be
deleted, by writing to <a href="mailto:hello@bloomandrisetherapy.com">hello@bloomandrisetherapy.com</a>.
Clinical records are a separate matter and are kept for the period the law requires
regardless of a deletion request.</p>
<p>Every email from the interest list has an unsubscribe link and it works immediately.</p>
<p>Texas residents have specific rights under the Texas Data Privacy and Security Act, and
Colorado residents under the Colorado Privacy Act, including access, correction, deletion,
and the right not to have personal data sold. This practice does not sell personal data.
Requests go to the same address.</p>"""),
 ('Children', """
<p>This site is not directed at children under 13 and does not knowingly collect their
information. <span class="todo">[Confirm whether Roshunda sees minors, and at what age.]</span></p>"""),
 ('Changes', """
<p>If this notice changes materially, the date at the top changes and the new version is
posted here. Questions go to
<a href="mailto:hello@bloomandrisetherapy.com">hello@bloomandrisetherapy.com</a>.</p>"""),
]

TERMS = [
 ('Agreement', """
<p>By using bloomandrisetherapy.com you agree to what follows. If you do not, please do not
use the site. These terms cover the website only. Therapy itself is governed by the informed
consent and practice policies you sign as a client, and where the two differ, those documents
control.</p>"""),
 ('This website is not treatment', """
<div class="callout">
<p>Everything here is general information. Reading it, filling in a form, or emailing
Roshunda does not create a therapist and client relationship. That relationship begins only
when you have completed intake and Roshunda has agreed in writing to work with you.</p>
</div>
<p>Nothing on this site is a substitute for individualized assessment, diagnosis, or care
from a qualified professional. Do not delay seeking care because of something you read here.</p>"""),
 ('Scope of practice and location', """
<p>Roshunda M. Hartison is a Licensed Professional Counselor in Texas (license 86566),
Virginia, and Colorado. Therapy is available only to clients physically located in one of
those states at the time of session, and you agree to tell her if your location changes.</p>
<p>Workshops, classes, and creative programming are educational, are open to participants
anywhere, and are not therapy. Attending one does not make you a client.</p>"""),
 ('Not for emergencies', """
<p>This site and its forms are not monitored continuously. Do not use them to communicate
anything urgent. If you are in danger or thinking about harming yourself, call or text
<b>988</b>, or call 911, or go to your nearest emergency department.</p>"""),
 ('Your responsibilities', """
<ul>
<li>Give accurate information when you fill in a form</li>
<li>Do not send protected health information through this site</li>
<li>Do not use the site to harass anyone, to break the law, or to attempt to gain access to
systems you are not authorized to use</li>
<li>Do not scrape, republish, or resell the content here</li>
</ul>"""),
 ('Intellectual property', """
<p>The writing, artwork, photography, and design on this site belong to Bloom &amp; Rise and
its licensors and may not be reproduced without written permission. The butterfly and
botanical artwork is used under licence and is not available for reuse.</p>
<p>Health at Every Size and HAES are registered trademarks of the Association for Size
Diversity and Health. This practice describes its approach as weight inclusive and does not
claim affiliation with ASDAH.</p>"""),
 ('Third party links', """
<p>Links to other sites are offered as a convenience. Roshunda does not control them and is
not responsible for their content, their accuracy, or their privacy practices.</p>"""),
 ('Disclaimer and limitation of liability', """
<p>This site is provided as is, without warranties of any kind, express or implied,
including any warranty that it will be uninterrupted, error free, or fit for a particular
purpose. To the fullest extent the law allows, Bloom &amp; Rise and Roshunda M. Hartison are
not liable for indirect, incidental, or consequential damages arising from your use of this
site.</p>
<p>Nothing here limits liability that cannot be limited by law, including liability arising
from professional services actually rendered to a client.</p>"""),
 ('Governing law and changes', """
<p>These terms are governed by the laws of the State of Texas, without regard to conflict of
law rules. <span class="todo">[Confirm venue with counsel.]</span></p>
<p>Terms may be updated; the date at the top will change when they are. Continuing to use the
site after that means you accept the revision.</p>
<p>Questions go to
<a href="mailto:hello@bloomandrisetherapy.com">hello@bloomandrisetherapy.com</a>.</p>"""),
]

GFE = [
 ('Your right to a Good Faith Estimate', """
<p>Under the federal No Surprises Act, you have the right to know what your care will cost
before you receive it. If you are uninsured, or you are insured but choosing not to use your
insurance for these services, you are entitled to a written Good Faith Estimate of the total
expected cost.</p>
<p>This applies to you whether or not you ask. Roshunda will provide one. You may also
request one at any time, for any reason.</p>"""),
 ('What you get and when', """
<p>The estimate is in writing and includes the expected services, the diagnosis and service
codes, and the total expected charge. Timing works like this:</p>
<ul>
<li>If you schedule at least <b>3 business days</b> ahead, you receive the estimate at least
<b>1 business day</b> before the appointment</li>
<li>If you schedule at least <b>10 business days</b> ahead, you receive it at least
<b>3 business days</b> before</li>
<li>If you ask for one without scheduling, you receive it within <b>3 business days</b></li>
</ul>
<p>Because therapy is ongoing rather than a single procedure, the estimate covers an expected
course of care, for example a stated number of sessions over twelve months, and says clearly
that the actual number may differ as the work develops.</p>"""),
 ('Current rates', """
<p>Individual therapy, 50 minutes: <span class="todo">$[RATE]</span></p>
<p>Initial intake session: <span class="todo">$[INTAKE RATE]</span></p>
<p><span class="todo">[Add any other billable service and its rate, and note the sliding
scale if one is offered.]</span></p>
<p>An estimate is an estimate. It is not a contract and it does not commit you to any number
of sessions.</p>"""),
 ('If your bill is higher than your estimate', """
<div class="callout">
<p>If you are billed <b>at least $400 more</b> than your Good Faith Estimate, you can dispute
the bill through the federal patient provider dispute resolution process. You have
<b>120 days</b> from the date of the bill to start a dispute.</p>
<p>Start at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a>
or call 1&#8209;800&#8209;985&#8209;3059. Starting a dispute will not affect the quality of
your care, and Roshunda will not retaliate for it.</p>
</div>
<p>Keep a copy of your estimate. Ask for another one any time your situation changes.</p>"""),
 ('Questions', """
<p>Ask on your consult call, or write to
<a href="mailto:hello@bloomandrisetherapy.com">hello@bloomandrisetherapy.com</a>. Nobody
here thinks it is rude to ask what something costs.</p>"""),
]

ACCESS = [
 ('The commitment', """
<p>This site is built to be usable by as many people as possible, including people using
screen readers, keyboard only navigation, magnification, or reduced motion settings. The
target is the Web Content Accessibility Guidelines, version 2.2, at level AA.</p>"""),
 ('What has been done', """
<ul>
<li>Every page works by keyboard alone, with a visible focus outline and a skip link to the
main content</li>
<li>Headings are in real order, so a screen reader can navigate by structure</li>
<li>Images carry descriptive alternative text, and decorative artwork is hidden from
assistive technology rather than announced</li>
<li>Text contrast meets or exceeds the AA ratio against its background</li>
<li>Text resizes and reflows without loss of content or horizontal scrolling</li>
<li>Motion and the scroll driven artwork are disabled automatically when your device is set
to reduce motion</li>
<li>Form fields have real labels, and errors are described in text rather than by colour alone</li>
</ul>"""),
 ('Known gaps', """
<p><span class="todo">[Update after an audit. If anything is known to fall short, name it
here with a date for the fix. Being specific about a gap is better than a blanket claim of
full compliance.]</span></p>"""),
 ('Sessions themselves', """
<p>Accessibility in the therapy is a separate question and a real one. If you need captions,
a screen reader friendly intake process, extra time, materials in a different format, or any
other accommodation, say so on the consult call or write ahead. It is not an imposition and
you do not need to explain why.</p>"""),
 ('Tell us what is broken', """
<p>If you hit a barrier on this site, please write to
<a href="mailto:hello@bloomandrisetherapy.com">hello@bloomandrisetherapy.com</a> and say what
page you were on and what happened. Reports get a reply within
<span class="todo">[2 business days]</span> and are taken seriously.</p>"""),
]

# ------------------------------------------------------------------ build --

def prose(sections, cls=''):
    out = []
    for h, b in sections:
        out.append('<div class="prose%s">\n<h2 class="rise">%s</h2>\n'
                   '<div class="prose-body rise" data-d="1">%s</div>\n</div>' % (cls, h, b))
    return '\n'.join(out)


def build(HEAD, GREEN, SCRIPT, swap_nav, build_foot):
    FOOT = build_foot(GREEN)

    def page(fname, title, desc, body, current='', keep=()):
        head = HEAD
        head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % title, head, count=1)
        head = re.sub(r'(<meta name="description" content=")[^"]*(">)',
                      lambda m: m.group(1) + desc + m.group(2), head, count=1)
        # only carry the base64 artwork a page actually uses
        for var, flag in (('ink-src', 'ink'), ('flit-src', 'flit'), ('bot-src', 'bot')):
            if flag not in keep:
                head = re.sub(r'(--%s:)url\("[^"]*"\)' % var, r'\1none', head, count=1)
        head = swap_nav(head, current)
        out = head + '<main id="main">\n' + body + '</main>\n\n' + FOOT + SCRIPT
        open(fname, 'w').write(out)
        print(fname, round(len(out) / 1024), 'KB')

    # ---- services overview
    rows = '\n'.join(SVC_INDEX % s for s in SERVICES)
    body = """
<header class="pagehead" style="--wash:var(--wash-leaf)">
  <span class="botanical" aria-hidden="true"></span>
  <div class="shell">
    <p class="kicker">Services</p>
    <h1>What we can <i style="color:var(--orange-deep)">work on</i> together.</h1>
    <p class="lede">Individual therapy, online, for adults in Texas, Virginia, and Colorado.
    Most people arrive with more than one of these at once, which is normal and does not
    need sorting out before you call.</p>
  </div>
</header>

<section class="band">
  <div class="shell">
    <div class="svc-list">%s</div>
  </div>
</section>

<section class="band alt">
  <div class="shell">
    <div class="prose">
      <h2 class="rise">How sessions work.</h2>
      <div class="prose-body rise" data-d="1">
        <p>Sessions are 50 minutes, held over secure video, usually weekly to start. Roshunda
        has been doing this work for over sixteen years, across community mental health,
        shelters, juvenile detention, and IDD services before private practice, which is a
        long way of saying very little will surprise her.</p>
        <p>She is warm and she is direct. You will get an actual opinion rather than a year
        of your own words handed back to you.</p>
        <p><b>Therapy is available only to clients physically located in Texas, Virginia, or
        Colorado at the time of session.</b> Workshops and creative programming are
        educational, are not therapy, and are open to anyone anywhere. See
        <a href="workshops.html">workshops and groups</a>.</p>
      </div>
    </div>
  </div>
</section>
%s""" % (rows, CONSULT)
    page('services.html', 'Services | Bloom &amp; Rise Therapy',
         'Individual online therapy for anxiety, OCD, body image, identity, and self trust. '
         'Texas, Virginia, and Colorado.', body, 'services.html', keep=('bot',))

    # ---- individual service pages
    for i, s in enumerate(SERVICES):
        prev, nxt = SERVICES[i - 1], SERVICES[(i + 1) % len(SERVICES)]
        pager = ('<div class="pager">'
                 '<a href="%s"><span class="lbl">Previous</span>&larr; %s</a>'
                 '<a href="services.html"><span class="lbl">All</span>Services</a>'
                 '<a href="%s" style="text-align:right"><span class="lbl">Next</span>%s &rarr;</a>'
                 '</div>') % (prev['f'], prev['nm'], nxt['f'], nxt['nm'])
        body = """
<header class="pagehead" style="--wash:%(wash)s">
  <span class="botanical" aria-hidden="true" style="background:%(tint)s;opacity:.17"></span>
  <div class="shell">
    <p class="kicker"><a href="services.html" style="color:inherit;text-decoration:none">Services</a> / %(n)s</p>
    <h1>%(h1)s</h1>
    <p class="lede">%(lede)s</p>
  </div>
</header>

<section class="band">
  <div class="shell">
    %(prose)s
    %(pager)s
  </div>
</section>
%(consult)s""" % dict(s, prose=prose(s['body']), pager=pager,
                              consult=CONSULT.replace('class="band alt"', 'class="band alt" style="--wash:%s"' % s['wash']))
        page(s['f'], '%s | Bloom &amp; Rise Therapy' % s['nm'], s['blurb'],
             body, 'services.html', keep=('bot',))

    # ---- faq
    items = '\n'.join('<details><summary>%s</summary><div class="a">%s</div></details>'
                      % (q, a) for q, a in FAQ)
    body = """
<header class="pagehead" style="--wash:var(--wash-sun)">
  <span class="flit-page" aria-hidden="true"></span>
  <div class="shell">
    <p class="kicker">Questions people ask</p>
    <h1>The things you were going to <i style="color:var(--orange-deep)">ask anyway.</i></h1>
    <p class="lede">Cost, insurance, what the first call is like, and whether any of this
    applies to you. If your question is not here, ask it on the consult call. Nobody minds.</p>
  </div>
</header>

<section class="band">
  <div class="shell">
    <div class="faq rise">%s</div>
  </div>
</section>
%s""" % (items, CONSULT)
    page('faq.html', 'Questions people ask | Bloom &amp; Rise Therapy',
         'Fees, insurance, licensure, what a free consult is like, and how online therapy '
         'with Roshunda M. Hartison works.', body, keep=('flit', 'bot'))

    # ---- legal
    LEGAL = [
      ('privacy.html', 'Privacy', 'Privacy notice',
       'How Bloom &amp; Rise handles information submitted through this website.', PRIVACY),
      ('terms.html', 'Terms of use', 'Terms of use',
       'Terms governing use of the Bloom &amp; Rise website.', TERMS),
      ('good-faith-estimate.html', 'Good Faith Estimate', 'Good Faith Estimate',
       'Your right to a written estimate of costs under the federal No Surprises Act.', GFE),
      ('accessibility.html', 'Accessibility', 'Accessibility',
       'How this site is built to be usable, and how to report a barrier.', ACCESS),
    ]
    for fname, kicker, h1, desc, sections in LEGAL:
        body = """
<header class="pagehead">
  <span class="botanical left warm" aria-hidden="true"></span>
  <div class="shell">
    <p class="kicker">%s</p>
    <h1>%s</h1>
  </div>
</header>

<section class="band legal">
  <div class="shell">
    <p class="updated">%s</p>
    %s
    %s
  </div>
</section>""" % (kicker, h1, UPDATED, DISCLAIM, prose(sections))
        page(fname, '%s | Bloom &amp; Rise Therapy' % h1, desc, body, keep=('bot',))
