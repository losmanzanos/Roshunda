# Builds the pages that are not slices of the home page: services, the five
# individual service pages, the FAQ, and the four legal pages.
import re

UPDATED = 'Last updated October 2026'

# ---------------------------------------------------------------- services --

SERVICES = [
 dict(f='anxiety.html', wash='#FBEDE0', tint='#B4551C', n='01',
  nm='Anxiety and overwhelm',
  blurb='For when your mind rarely slows down, even while you keep everything moving.',
  h1='Anxiety and <i>overwhelm</i>',
  lede='You are functional. You are also exhausted. Anxiety that looks like competence from '
       'the outside is still anxiety, and it still costs you something every day.',
  body=[
   ('What this looks like', """
<p>Sometimes anxiety does not look the way people expect. You may be the person everyone depends
on. The one who answers the message, remembers the birthday, shows up for everyone else, and
somehow keeps everything moving. Underneath all of that, your mind rarely slows down.</p>
<p>It is replaying a conversation days after it happened. Waking up with tension in your body
before the day has started. Feeling like if you stopped managing everything, even for a moment,
something might fall apart.</p>
<p>Or maybe anxiety has made it harder to keep up. You are avoiding things you once handled with
ease, struggling to concentrate, withdrawing from people, or feeling flattened by ordinary
responsibilities. Whether you are holding it together on the outside or struggling to get through
the day, your anxiety deserves attention and care.</p>
<p>Some of what you may be experiencing:</p>
<ul>
<li>Waking up already behind, or mentally preparing for everything that could go wrong</li>
<li>Overthinking decisions to the point that making one feels impossible</li>
<li>Physical tension, racing thoughts, or symptoms that intensify when you are anxious</li>
<li>Saying yes when you want to say no, then feeling guilty or resentful afterward</li>
<li>Avoiding situations, responsibilities, or conversations because they feel like too much</li>
<li>Struggling to rest because your mind keeps listing what you have not done</li>
</ul>"""),
   ('How the work goes', """
<p>We start by getting to know you. Your experiences, what anxiety looks like in your everyday
life, and how you have been managing it. There is no expectation that you have anything figured
out before you arrive.</p>
<p>Together we begin to recognize patterns. The thoughts that keep you stuck, the situations that
bring anxiety up, and the ways you have learned to cope. Some of those strategies helped you get
through difficult moments. They may not be helping you now.</p>
<p>From there we get practical. We explore ways to challenge unhelpful thinking, respond
differently to anxiety, set healthier boundaries, and gradually face what you have been avoiding.
The goal is not to push you before you are ready. It is to build your confidence in handling
discomfort and uncertainty.</p>
<p>Roshunda's approach draws from cognitive behavioral therapy, acceptance and commitment therapy,
mindfulness, and exposure based strategies where they fit. And because not everyone processes
their experiences through conversation alone, there is room for creative expression, music, or
other ways of connecting with what you are feeling.</p>
<p>Therapy is collaborative. You will work out together what helps, and she will encourage you to
practice it outside of session so it becomes part of your life rather than part of the hour.</p>"""),
   ('What changes', """
<p>The goal is not necessarily to eliminate anxiety. It is to feel less controlled by it.</p>
<p>You may begin to notice anxious thoughts without automatically believing them, make decisions
without needing to feel completely certain, and recognize when you are carrying more than you have
the capacity to hold.</p>
<p>Some days will still be hard. Over time you can build the confidence, flexibility, and tools to
meet those days differently. You do not have to wait until everything falls apart to start making
space for yourself.</p>"""),
  ]),

 dict(f='identity.html', wash='#F1E7EC', tint='#5F2A46', n='02',
  nm='Identity and self-trust',
  blurb='For the stretch between who you were and who you are becoming.',
  h1='Identity and <i>self-trust</i>',
  lede='You can be doing everything right and still not recognize the life you built. '
       'That is not ingratitude. That is information.',
  body=[
   ('When life starts to feel different', """
<p>Sometimes you come to therapy because something is wrong. Other times it is because something
no longer feels right, even if you cannot quite explain why.</p>
<p>Maybe you have spent so much time meeting expectations, taking care of others, or following the
path you thought you were supposed to take that you have lost touch with what you actually want.</p>
<p>Or maybe you are entering a new season. A career change, graduation, a relationship shift,
becoming a parent, an unexpected loss, or simply realizing that the version of yourself you have
always known is changing. And sometimes there is no event at all. Just a growing sense that
something needs to shift.</p>
<p>You do not have to have the answers to begin exploring who you are and who you are becoming.</p>"""),
   ('Rebuilding trust in yourself', """
<p>When you have spent years weighing everyone else's needs, opinions, and expectations, it can
become difficult to recognize your own voice.</p>
<p>You may second guess your decisions, look to others for reassurance, struggle to set
boundaries, or feel guilty when you choose something for yourself. Sometimes those patterns
developed because they helped you navigate relationships, responsibilities, or hard experiences.
What once helped you get through may no longer be helping you grow.</p>
<p>In this work you will explore where those patterns began, how they show up today, and what it
looks like to make decisions that reflect your own values. Roshunda offers a space where you are
heard and understood, and she will also ask questions, challenge patterns when it is useful, and
encourage you to try something different.</p>
<p>The goal is not to become someone new. It is to build a stronger relationship with yourself
and make room for the person you are becoming.</p>"""),
   ('Who this tends to resonate with', """
<p>This work may feel familiar if you have spent much of your life being the dependable one,
navigating family or cultural expectations, or trying to meet standards that leave little room for
your own needs.</p>
<p>It may also resonate if you are navigating:</p>
<ul>
<li>Transitions that have you questioning your direction or sense of purpose</li>
<li>People pleasing, perfectionism, or difficulty setting boundaries</li>
<li>Self doubt and constantly seeking reassurance</li>
<li>Changes in relationships, family roles, career, or personal identity</li>
<li>The pressure to be strong, successful, or to have everything figured out</li>
<li>A wish to reconnect with your values, interests, and sense of self</li>
</ul>
<p><b>You are allowed to grow beyond the version of yourself that everyone else has gotten used
to.</b></p>"""),
  ]),

 dict(f='body-image.html', wash='#F9E9F1', tint='#C77BA6', n='03',
  nm='Body image and self-worth',
  blurb='Weight inclusive work on body image, self worth, and being in a body at all.',
  h1='Body image and <i>self-worth</i>',
  lede='Your body is not a problem to solve. And your worth has never been determined by its '
       'size, shape, or appearance.',
  body=[
   ('Where this starts', """
<p>Your relationship with your body is shaped by far more than what you see in the mirror.</p>
<p>Maybe you have spent years trying to change how your body looks, hoping that reaching a certain
size or number would finally let you feel comfortable in your own skin. Maybe you have experienced
criticism, comparison, or unwanted comments about your appearance. Or perhaps changes from aging,
health, pregnancy, or other experiences have left you feeling disconnected from yourself.</p>
<p>Sometimes the struggle is not about wanting to change your body at all. It is about wanting to
stop feeling uncomfortable, ashamed, or constantly aware of how others might see you.</p>
<p>Whatever brought you here, you deserve a space where your body is not judged and your
experiences are taken seriously.</p>"""),
   ('What we work on', """
<ul>
<li>The constant self criticism or negative thoughts about your body</li>
<li>Comparing your appearance to others, especially online</li>
<li>Feeling uncomfortable in photographs, mirrors, clothing, or social situations</li>
<li>Avoiding activities, relationships, or experiences because of how you feel about your body</li>
<li>Shame, guilt, or rigid beliefs connected to food and appearance</li>
<li>Unwanted comments or judgment from family, partners, or healthcare providers</li>
<li>Adjusting to body changes, and grieving expectations you once held</li>
<li>Building self compassion and a sense of worth that does not depend on how you look</li>
</ul>"""),
   ('A weight-inclusive approach', """
<p>Roshunda approaches body image from a weight inclusive perspective. That means she does not
view body size as a problem that needs correcting, and weight loss is not a goal of the work.</p>
<p>Instead you will look at how your thoughts, beliefs, experiences, and emotions shape your
relationship with your body and with yourself. You will not be asked to earn self acceptance by
changing your appearance.</p>
<p>Her role is to help you explore the patterns keeping you stuck, challenge the harmful messages
you have taken in, and begin building a relationship with yourself rooted in respect rather than
criticism.</p>
<div class="callout">
<p><b>When additional support is needed.</b> As a Licensed Professional Counselor, Roshunda's work
focuses on the emotional and psychological side of body image and self worth. She does not provide
nutritional counseling, prescribe diets, or develop meal plans.</p>
<p>If concerns about eating, nutrition, or physical health need more, you can talk through
connecting with qualified professionals, including registered dietitians and clinicians who
specialize in eating disorders. A collaborative approach helps make sure you are cared for as a
whole person.</p>
</div>"""),
   ('Beyond the mirror', """
<p>Body image work often opens the door to deeper conversations about identity, relationships,
belonging, and the messages you have received about what makes someone worthy.</p>
<p>It is about what it means to take up space without apologizing, to participate in life without
waiting for your body to change, and to treat yourself with the compassion you offer other people
so freely.</p>
<p><b>You deserve to live fully in the body you have today, not just the one you imagine having
someday.</b></p>"""),
  ]),

 dict(f='ocd.html', wash='#FCF0E2', tint='#D9762F', n='05',
  nm='OCD and intrusive thoughts',
  blurb='Evidence based OCD treatment, including exposure and response prevention.',
  h1='OCD and <i>intrusive thoughts</i>',
  lede='You do not have to believe every thought your mind produces. And you do not have to keep '
       'organizing your life around trying to make those thoughts go away.',
  body=[
   ('Understanding OCD', """
<p>OCD is about much more than cleanliness, organization, or wanting things a certain way.</p>
<p>It often involves unwanted thoughts, images, urges, or feelings that create distress, doubt, or
uncertainty. In response, you do something to feel better, to prevent something bad, or to get a
sense of certainty. That response brings relief briefly. Over time the cycle becomes exhausting.</p>
<p>Not all compulsions are visible. Sometimes OCD looks like checking locks, washing hands, or
avoiding certain situations. Other times it happens entirely in your mind: replaying
conversations, analyzing your intentions, seeking reassurance, mentally reviewing memories, or
repeating certain words or prayers to feel safe.</p>
<p>OCD also tends to attach itself to what you care about most. Your relationships, your faith,
your health, your identity, the people you love.</p>
<p>Some common experiences:</p>
<ul>
<li>Unwanted thoughts or images involving harm, sexuality, religion, morality, or other
distressing themes</li>
<li>Repeated checking, cleaning, counting, arranging, or repeating</li>
<li>Constantly questioning your intentions, feelings, memories, or decisions</li>
<li>Seeking reassurance from others, or repeatedly reassuring yourself</li>
<li>Avoiding people, places, or situations that trigger intrusive thoughts</li>
<li>Needing certainty, completeness, or for things to feel just right</li>
<li>Spending significant time mentally reviewing or trying to figure something out</li>
</ul>
<p>If you have been afraid to say your thoughts out loud because of how someone might react, you
can say them here. You do not have to filter your experience or find the perfect words first.</p>"""),
   ('Exposure and response prevention', """
<p>One of the primary treatments Roshunda uses for OCD is Exposure and Response Prevention, a
well established, evidence based approach that changes how you respond to obsessive thoughts and
uncertainty.</p>
<p>ERP is not about forcing yourself into situations you are not ready for, and it does not expose
you to actual danger. You will identify together the situations, thoughts, and experiences that
trigger your OCD, along with the compulsions and avoidance keeping the cycle going. From there you
build a personalized plan to approach those triggers gradually while practicing new ways of
responding.</p>
<p>The goal is not to prove your fears could never happen, or to make every uncomfortable thought
disappear. It is to build your confidence in being able to sit with uncertainty and discomfort
without letting OCD decide what you do next. You move through it collaboratively, with guidance,
encouragement, and chances to practice between sessions.</p>"""),
   ('What if my thoughts are disturbing or embarrassing', """
<p>OCD can involve thoughts that feel completely opposite to your values and intentions. You may
find yourself questioning what those thoughts say about you, or worrying that having a thought
means you might act on it.</p>
<p>Unwanted intrusive thoughts are not, by themselves, evidence of anyone's character or
intentions. Part of this work is learning to recognize when OCD is pulling you into a cycle of
fear, analysis, and attempts to be certain.</p>
<p>Roshunda has worked with people experiencing a wide range of OCD themes, including harm,
relationships, religion, morality, contamination, health, and sexuality. Her role is not to judge
what shows up in your mind. It is to understand it and help you build a healthier relationship
with it.</p>"""),
   ('If you have tried therapy before', """
<p>Maybe you have already been in therapy, talked at length about your fears, or tried to reason
your way out of intrusive thoughts. Maybe you felt temporary relief and then found yourself in the
same cycle again. That does not mean you did not try hard enough.</p>
<p>Traditional talk therapy helps with many concerns, but OCD usually needs a more targeted
approach. Repeatedly analyzing fears or offering reassurance can unintentionally reinforce the
cycle. ERP focuses on responding differently rather than trying to resolve every doubt.</p>
<p>Whether you are newly diagnosed, have lived with OCD for years, or are still working out what
you are experiencing, you can start by talking through what has been happening.</p>"""),
   ('What change can look like', """
<p>Progress does not mean never having another intrusive thought.</p>
<p>It may look like spending less time mentally reviewing, making decisions without checking
repeatedly, returning to things you have been avoiding, or letting uncertainty be there without
needing to resolve it. It can also mean reconnecting with relationships and parts of your life
that OCD has gradually pushed aside.</p>
<p><b>Your thoughts do not have to make every decision for you. There is room to live beyond
OCD.</b></p>"""),
  ]),

 dict(f='creative-therapy.html', wash='#EAF0E2', tint='#5E7A4F', n='06',
  nm='When words run out',
  blurb='Creative expression in session, for the weeks when talking is not getting there.',
  h1='When words <i>run out</i>',
  lede='Sometimes words are not enough. And that is okay. There are other ways to explore what '
       'you are feeling.',
  body=[
   ('Why creative expression', """
<p>Roshunda has always had a love for music and creativity. She is not a formally trained artist
or art therapist, and she will tell you that plainly. What she believes is that creative
expression can be a meaningful way to explore emotions, find insight, and connect with yourself.</p>
<p>Sometimes you can explain exactly what is happening in your life and still struggle to express
how it feels. That is where creativity offers another way in.</p>
<p>You do not need artistic skill or musical talent. This is not about making something beautiful
or getting it right. It is about the process, not the finished thing.</p>"""),
   ('What it looks like in session', """
<p>Creative expression is not a separate service you book instead of therapy. It is something that
can be part of a session when it feels useful and fits your goals.</p>
<p>That might be drawing, journaling, music, colour, or another simple activity that helps you
explore your thoughts and feelings. Some clients enjoy this. Others prefer to talk. Either is
completely fine.</p>
<p><b>You do not have to be an artist to express yourself creatively. And neither does she.</b></p>"""),
   ('Beyond the therapy room', """
<p>Roshunda's passion for creativity also reaches into the community through
<a href="https://www.evolvingthruart.com/" target="_blank" rel="noopener">Evolving Thru Art</a>, a
nonprofit focused on creating opportunities for young people to explore creative expression,
connection, and personal growth.</p>
<p>For community workshops and groups, see the <a href="workshops.html">workshops and groups</a>
page.</p>"""),
  ]),
]

DEPRESSION = dict(f='depression.html', wash='#E9EEF3', tint='#4A6076',
  nm='Depression and low motivation',
  blurb='For the flat stretch, when the things that once brought you joy feel out of reach.',
  h1='Depression and <i>low motivation</i>',
  lede='Depression is not always sadness. Sometimes it is the slow narrowing of your world until '
       'the things that once brought you joy, connection, or purpose begin to feel out of reach.',
  body=[
   ('What it can look like', """
<p>Depression does not always look the way people expect. Sometimes it is crying, sadness, or
feeling overwhelmed. Other times it is feeling disconnected, emotionally numb, irritable, or
simply exhausted by ordinary life.</p>
<p>Getting out of bed takes negotiation. Things you used to enjoy do not feel the same. You find
yourself going through the motions, wondering why everything is so difficult, then criticizing
yourself for not doing more. And sometimes you are still showing up for work, school, and family
while quietly struggling to feel present in your own life.</p>
<p>Some of what you may be experiencing:</p>
<ul>
<li>Sleeping more than usual, struggling to sleep, or waking already exhausted</li>
<li>Difficulty finding motivation for responsibilities or things you once enjoyed</li>
<li>Withdrawing from people even when you miss feeling connected</li>
<li>Feeling hopeless, numb, irritable, or overwhelmed</li>
<li>Being hard on yourself, or feeling like you are never doing enough</li>
<li>Struggling with concentration, decisions, or finishing everyday tasks</li>
<li>Feeling disconnected from yourself, your relationships, or your life</li>
</ul>"""),
   ('How we work through it', """
<p>You start by understanding what depression looks like for you, how it is affecting your days,
and what you have been carrying. Roshunda's approach uses cognitive behavioral therapy and
behavioral activation, along with other strategies based on your needs and goals.</p>
<p><b>Cognitive behavioral therapy</b> explores the thoughts and beliefs feeding hopelessness,
guilt, or low self worth. Together you recognize patterns, question unhelpful conclusions, and
build more balanced ways of responding to yourself.</p>
<p><b>Behavioral activation</b> works from the other direction, reconnecting you with activities,
relationships, and routines that bring meaning, enjoyment, or a sense of accomplishment. When you
are depressed, waiting until you feel motivated tends to keep you stuck. So you start small, with
steps that fit your current capacity rather than expecting everything to change at once.</p>
<p>There may be chances to practice something between sessions. This is not about adding pressure.
It is about building momentum, noticing progress, and making change at a pace that works.</p>
<p>Some weeks progress looks like reconnecting with something you enjoy. Other weeks it looks like
getting out of bed, reaching out to someone, or simply showing up. <b>Small steps still
count.</b></p>"""),
   ('Additional support when needed', """
<p>Depression affects people differently, and sometimes therapy is only one part of what someone
needs.</p>
<p>If medication may help, you can talk through a referral to a qualified prescriber. Therapy and
medication can work together, depending on your needs and preferences.</p>
<div class="callout">
<p>If you are experiencing thoughts of self harm or suicide, Roshunda encourages you to share that
openly. Those conversations matter, and they are met with care, without judgment, and with your
safety in mind. Depending on what you need, additional services or a different level of support
may be recommended.</p>
<p>If you are in an immediate mental health crisis, call or text <b>988</b>. If you are in
immediate danger or need emergency medical help, call 911 or go to the nearest emergency
department.</p>
</div>"""),
   ('What change can look like', """
<p>The goal is not to force yourself to be happy or productive all the time. It is to gradually
reconnect with yourself, recognize what you need, and make space for the parts of life that matter
to you.</p>
<p>There may still be difficult days. You do not have to navigate them without support.</p>
<p><b>You do not have to feel motivated to begin. Sometimes beginning is how we make room for
hope.</b></p>"""),
  ])

SERVICES.append(DEPRESSION)

# Roshunda's preferred order of emphasis
ORDER = ['anxiety.html', 'identity.html', 'body-image.html',
         'depression.html', 'ocd.html', 'creative-therapy.html']
SERVICES.sort(key=lambda d: ORDER.index(d['f']))
for i, d in enumerate(SERVICES, 1):
    d['n'] = '%02d' % i


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
  Licensed Professional Counselor in all three, and sees clients in person in Katy, Texas.</p>
  <p>Workshops, classes, and creative programming are educational rather than clinical, so
  those are open to anyone anywhere. See <a href="workshops.html">workshops and groups</a>.</p>"""),
 ('Is everything online?',
  """<p>Not everything. <b>In person appointments are available in Katy, Texas</b>, with limited
  scheduling options, so mention it on the consult call if sitting in the same room matters to
  you.</p>
  <p>Virtual sessions are held over a secure video platform and are open to clients physically
  located in Texas, Virginia, or Colorado. You get a link before each appointment and do not need
  to install anything unusual.</p>
  <p>You do need somewhere you can talk without managing who might hear you. A car in a
  parking lot counts. Plenty of good work has happened in a parked car.</p>"""),
 ('What does it cost?',
  """<p>Roshunda's self pay rate is $175 for a 50 minute individual session and $200 for a
  couples session. A limited number of sliding scale spots are available;
  ask on the consult call and she will tell you honestly whether one is open.</p>
  <p>If you are paying out of pocket, you are entitled to a written estimate before you
  start. See <a href="good-faith-estimate.html">Good Faith Estimate</a>.</p>"""),
 ('Do you take insurance?',
  """<p>Yes. Roshunda is in network with Aetna, Anthem, BlueCross BlueShield, Cigna and Evernorth,
  and UnitedHealthcare and Optum, along with select employee assistance programs (EAPs).
  Coverage varies by plan, so it is worth confirming your benefits before the first session.</p>
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
  """<p>Please give at least 24 hours notice if you need to cancel or reschedule. Sessions
  cancelled with less notice, or missed without notice, may be charged the full session fee.
  Insurance does not cover missed sessions.</p>
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

DISCLAIM = ""

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
<p>The site is hosted on Cloudflare Pages, which keeps standard
server logs including IP address, browser type, and pages requested. These are used for
security and reliability. The site does not currently use analytics.</p>
<p>This site sets no advertising cookies and runs no third party trackers. Web fonts are
loaded from Google Fonts, which means your browser makes a request to Google to fetch them.</p>"""),
 ('Who else touches it', """
<p>The consult request form is delivered by EmailJS, workshop interest signups are held in
Kit, and email is handled by Google Workspace. Scheduling and the clinical record live in
SimplePractice, which is a separate system with its own
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
information. Therapy for anyone under 18 begins only with the consent of a parent or
legal guardian.</p>"""),
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
Virginia (license 86566), and Colorado (license LPC.0021147). Therapy is available only to clients physically located in one of
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
law rules. Any dispute will be handled in the state or federal courts located in
Texas.</p>
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
<p>Initial intake session: $175</p>
<p>Individual therapy, 50 minutes: $175</p>
<p>Couples therapy, 50 minutes: $200</p>
<p>A limited number of sliding scale spots are available. Ask on the consult call.</p>
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
<p>No known issues as of the last review in October 2026. If you find one, please tell us
using the address below so it can be fixed.</p>"""),
 ('Sessions themselves', """
<p>Accessibility in the therapy is a separate question and a real one. If you need captions,
a screen reader friendly intake process, extra time, materials in a different format, or any
other accommodation, say so on the consult call or write ahead. It is not an imposition and
you do not need to explain why.</p>"""),
 ('Tell us what is broken', """
<p>If you hit a barrier on this site, please write to
<a href="mailto:hello@bloomandrisetherapy.com">hello@bloomandrisetherapy.com</a> and say what
page you were on and what happened. Reports get a reply within
two business days and are taken seriously.</p>"""),
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
        head = head.replace('__CANON__', fname)
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
        <p>Sessions are typically 50 minutes, available virtually or in person in Katy, Texas.
        Most people begin weekly, and the frequency depends on your needs and goals.</p>
        <p>Roshunda's years in mental health have taught her that no two people experience life's
        challenges the same way, so the work is collaborative and built around you, meeting you
        where you are while helping you move toward where you want to be.</p>
        <p>Her style is warm, collaborative, and direct. She wants to hear your story and
        understand your experience, and she will also ask questions, challenge patterns when it
        helps, and encourage you to put what you are learning into practice. Therapy is not about
        being told how to live. It is about understanding yourself, building confidence in your
        decisions, and making changes that hold.</p>
        <h3>Session availability</h3>
        <p><b>In person</b> appointments are available in Katy, Texas, with limited scheduling
        options.</p>
        <p><b>Virtual</b> therapy is available to clients physically located in Texas, Virginia, or
        Colorado at the time of their session.</p>
        <p>Workshops and creative programming are educational experiences, not psychotherapy
        services. More on the <a href="workshops.html">workshops and groups</a> page.</p>
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
