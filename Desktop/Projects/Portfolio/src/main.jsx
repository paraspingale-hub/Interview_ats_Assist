import { useEffect, useRef, useState } from 'react';
import { createRoot } from 'react-dom/client';
import professionalPhoto from './myimage.jpeg';
import personalPhoto from './nonprofessional.jpg';
import './styles.css';

const navItems = ['Home', 'About', 'Work', 'Blogs'];

function ConstellationCanvas() {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const context = canvas.getContext('2d');
    const pointer = { x: window.innerWidth * 0.55, y: window.innerHeight * 0.42 };
    let points = [];
    let frame;

    const makePoints = () => {
      const amount = Math.max(42, Math.floor((window.innerWidth * window.innerHeight) / 19000));
      points = Array.from({ length: amount }, () => ({
        x: Math.random() * window.innerWidth,
        y: Math.random() * window.innerHeight,
        vx: (Math.random() - 0.5) * 0.16,
        vy: (Math.random() - 0.5) * 0.16,
        r: Math.random() * 1.45 + 0.35
      }));
    };

    const resize = () => {
      const ratio = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = window.innerWidth * ratio;
      canvas.height = window.innerHeight * ratio;
      canvas.style.width = `${window.innerWidth}px`;
      canvas.style.height = `${window.innerHeight}px`;
      context.setTransform(ratio, 0, 0, ratio, 0, 0);
      makePoints();
    };

    const movePointer = (event) => {
      pointer.x = event.clientX;
      pointer.y = event.clientY;
    };

    const draw = () => {
      const width = window.innerWidth;
      const height = window.innerHeight;
      context.clearRect(0, 0, width, height);

      const ambient = context.createRadialGradient(pointer.x, pointer.y, 0, pointer.x, pointer.y, 430);
      ambient.addColorStop(0, 'rgba(255, 111, 24, 0.075)');
      ambient.addColorStop(0.42, 'rgba(255, 111, 24, 0.018)');
      ambient.addColorStop(1, 'rgba(255, 111, 24, 0)');
      context.fillStyle = ambient;
      context.fillRect(0, 0, width, height);

      points.forEach((point) => {
        point.x += point.vx;
        point.y += point.vy;
        if (point.x < -10 || point.x > width + 10) point.vx *= -1;
        if (point.y < -10 || point.y > height + 10) point.vy *= -1;
      });

      for (let i = 0; i < points.length; i += 1) {
        const point = points[i];
        const pointerDistance = Math.hypot(point.x - pointer.x, point.y - pointer.y);

        if (pointerDistance < 210) {
          const opacity = (1 - pointerDistance / 210) * 0.48;
          context.beginPath();
          context.moveTo(point.x, point.y);
          context.lineTo(pointer.x, pointer.y);
          context.strokeStyle = `rgba(255, 189, 140, ${opacity})`;
          context.lineWidth = 0.7;
          context.stroke();
        }

        for (let j = i + 1; j < points.length; j += 1) {
          const other = points[j];
          const distance = Math.hypot(point.x - other.x, point.y - other.y);
          if (distance < 150) {
            context.beginPath();
            context.moveTo(point.x, point.y);
            context.lineTo(other.x, other.y);
            context.strokeStyle = `rgba(218, 223, 225, ${(1 - distance / 150) * 0.22})`;
            context.lineWidth = 0.55;
            context.stroke();
          }
        }

        context.beginPath();
        context.arc(point.x, point.y, point.r, 0, Math.PI * 2);
        context.fillStyle = pointerDistance < 210 ? 'rgba(255, 173, 115, .9)' : 'rgba(231, 234, 235, .55)';
        context.fill();
      }
      frame = requestAnimationFrame(draw);
    };

    resize();
    window.addEventListener('resize', resize);
    window.addEventListener('pointermove', movePointer);
    draw();
    return () => {
      cancelAnimationFrame(frame);
      window.removeEventListener('resize', resize);
      window.removeEventListener('pointermove', movePointer);
    };
  }, []);

  return <canvas className="constellation" ref={canvasRef} aria-hidden="true" />;
}

function MaharashtraMark() {
  return (
    <svg className="maharashtra-mark" viewBox="0 0 106 72" role="img" aria-label="Maharashtra">
      <path d="M6 29l10-9 13 1 7-10 16 6 10-5 13 9 18 2 7 11-8 9 2 11-13 2-9 11-15-5-12 6-8-9-15-2-4-10-15-4z" />
      <path className="map-line" d="M22 32l15 5 13-10 13 7 15-5M45 58l5-24 12 15 10 17" />
    </svg>
  );
}

function DesktopSetup() {
  return (
    <div className="desktop-setup" aria-label="Desktop displaying Java code">
      <div className="tower" aria-hidden="true">
        <span className="tower-light" /><span className="tower-slot" />
        <span className="tower-ports"><i /><i /><i /></span>
        <span className="tower-lines"><i /><i /><i /></span>
      </div>
      <div className="monitor-unit">
        <div className="monitor">
          <div className="monitor-top"><span className="window-dots"><i /><i /><i /></span><span>PortfolioApplication.java</span><b>●</b></div>
          <pre className="java-code"><code><span className="syntax-keyword">public class</span> <span className="syntax-type">Paras</span> {'{'}{`\n`}  <span className="syntax-keyword">private final</span> <span className="syntax-type">Curiosity</span> mind;{`\n`}{`\n`}  <span className="syntax-keyword">public</span> <span className="syntax-type">Future</span> <span className="syntax-method">build</span>() {'{'}{`\n`}    <span className="syntax-keyword">return</span> <span className="syntax-string">"ideas in motion"</span>;{`\n`}  {'}'}{`\n`}{'}'}</code></pre>
          <div className="monitor-glow" />
        </div>
        <div className="monitor-neck" /><div className="monitor-base" />
      </div>
    </div>
  );
}

function SocialIcon({ type, href, title, children }) {
  return (
    <a className={`social-link ${type}`} href={href} target={type === 'email' ? undefined : '_blank'} rel={type === 'email' ? undefined : 'noreferrer'} aria-label={title}>
      <span className="social-symbol">{children}</span>
      <span className="social-preview" aria-hidden="true">
        <span className="preview-top"><i /> {type === 'linkedin' ? 'linkedin.com/in/paraspingale' : type === 'github' ? 'github.com/paraspingale-hub' : 'paraspingales@gmail.com'}</span>
        <span className="preview-content"><b>{type === 'linkedin' ? 'Paras Rahul Pingale' : type === 'github' ? 'paras pingale' : 'Let’s build together'}</b><small>{type === 'linkedin' ? 'Developer · Creator · Thinker' : type === 'github' ? 'repositories / projects / experiments' : 'Click to compose an email'}</small></span>
      </span>
    </a>
  );
}

const buildPrinciples = [
  { group: 'code', icon: '{}', title: 'Strongly Typed', text: 'Types as documentation and guardrails. Catch errors at compile time, not runtime.' },
  { group: 'code', icon: '✣', title: 'KISS & YAGNI', text: 'Simple solutions, no speculative features. Why abstract logic that will only ever be used one way? Building for problems that may never come is a waste of time and money.' },
  { group: 'code', icon: '⬡', title: 'SOLID Principles', text: 'Single responsibility, Open-closed, Liskov substitution, Interface segregation, Dependency inversion. Apply wisely, where needed—not as dogma that adds unnecessary complexity.' },
  { group: 'code', icon: '▥', title: 'Clean Architecture', text: 'Keep business logic free from infrastructure concerns—but stay pragmatic. Abstraction layers that serve no realistic future are just complexity in disguise.' },
  { group: 'code', icon: '♢', title: 'Fail Fast', text: 'When input or conditions are invalid, fail immediately. Check lightweight validations before expensive operations—exit early, fail cheap.' },
  { group: 'code', icon: '▧', title: 'Code as Documentation', text: 'Code that speaks for itself. Clear naming over cryptic abbreviations that lose context within a month.' },
  { group: 'code', icon: '⌘', title: 'Design Patterns', text: 'Proven solutions to common problems. Creational, structural, and behavioral patterns applied thoughtfully.' },
  { group: 'code', icon: '⇄', title: "Don't Repeat Yourself (DRY)", text: 'Reusable, maintainable code that reduces redundancy.' },
  { group: 'code', icon: '◈', title: 'Domain-Driven Design', text: 'Code that speaks the language of the business. Models reflect real-world concepts.' },
  { group: 'code', icon: '▤', title: 'Separation of Concerns', text: 'Separation of layers and responsibilities. No business logic in your templates, no database queries in your controllers.' },
  { group: 'code', icon: '♢', title: 'Defensive Programming', text: 'Anticipate misuse and invalid input. Validate assumptions, handle edge cases, trust nothing.' },
  { group: 'work', icon: '▧', title: 'Infrastructure as Code (IaC)', text: 'Version-controlled, reproducible environments. No more snowflake servers or manual configuration drift.' },
  { group: 'work', icon: 'ϟ', title: 'Rapid Application Development (RAD)', text: 'The quicker you iterate proofs of concept and reach a minimal viable product (MVP), the better.' },
  { group: 'work', icon: '⌘', title: 'Continuous Integration & Deployment (CI/CD)', text: 'Automated pipelines for consistent, reliable delivery.' },
  { group: 'work', icon: '▣', title: 'Accelerated Intelligence', text: 'Leveraging AI tools to deliver more in less time. Modern development, amplified.' },
  { group: 'work', icon: '⌁', title: 'Pragmatic Testing', text: 'Tests are a tool, not a goal. Test your code, not the framework, language, or vendor packages—assume they work.' },
  { group: 'work', icon: '▤', title: 'Database as Code (DaC)', text: 'Manual changes kill replayability and consistency. Migrations track what changed, when, and why.' }
];

function BuildProcess({ filter, onFilterChange, isStandalone = false }) {
  const filters = [
    { id: 'all', label: 'All', icon: '▱' },
    { id: 'code', label: 'How I Code', icon: '<>' },
    { id: 'work', label: 'How I Work', icon: '⌕' },
    { id: 'deliver', label: 'How I Deliver', icon: '↗' }
  ];
  const visiblePrinciples = filter === 'all' ? buildPrinciples : buildPrinciples.filter((principle) => principle.group === filter);

  return (
    <section className={`building-section ${isStandalone ? 'is-full-page' : ''}`} id="building-section" aria-labelledby="building-title">
      <div className="building-panel">
        {isStandalone && <a className="build-back" href="#home">← Back to portfolio</a>}
        <p className="section-kicker"><span /> BUILDING SECTION</p>
        <h2 id="building-title">How I build software.</h2>
        <div className="build-filters" role="tablist" aria-label="Building process categories">
          {filters.map((item) => (
            <button key={item.id} className={filter === item.id ? 'is-active' : ''} onClick={() => onFilterChange(item.id)} role="tab" aria-selected={filter === item.id}>
              <span>{item.icon}</span>{item.label}
            </button>
          ))}
        </div>
        <div className="principles-grid">
          {visiblePrinciples.length ? visiblePrinciples.map((principle) => (
            <article className="principle-card" key={principle.title}>
              <header><span className="principle-icon" aria-hidden="true">{principle.icon}</span><h3>{principle.title}</h3><b aria-hidden="true">&lt;&gt;</b></header>
              <p>{principle.text}</p>
            </article>
          )) : <p className="delivery-note">Delivery is built into every step: thoughtful architecture, rapid feedback, and reliable deployment.</p>}
        </div>
      </div>
    </section>
  );
}

const projects = [
  {
    title: 'SmartHire – AI Mock Interview Agent',
    stack: ['Python', 'LLMs', 'Ollama', 'Llama 3', 'Gemini API', 'Streamlit'],
    github: 'https://github.com/paraspingale-hub/Interview_ats_Assist',
    highlights: [
      'Designed a multi-agent evaluation architecture where specialized agents assess technical accuracy, communication clarity, and confidence for more reliable, bias-resistant feedback.',
      'Integrated Ollama (Llama 3) and Gemini API with structured prompt engineering for role-specific questions and personalized feedback reports.',
      'Built automated PDF reports and a LangChain RAG pipeline to ground interview questions in the target job description.'
    ]
  },
  {
    title: 'Text Sentiment Analysis (RNN / LSTM)',
    stack: ['Python', 'TensorFlow', 'Keras', 'NLTK', 'Word2Vec'],
    github: 'https://github.com/paraspingale-hub/Text-Sentiment-Analysis',
    highlights: [
      'Built a stacked LSTM network for multi-class sentiment classification on movie-review and social-media text.',
      'Created a complete NLP pipeline with tokenization and Word2Vec embeddings.',
      'Applied dropout regularization and Adam optimizer tuning to control overfitting on variable-length sequences.'
    ]
  },
  {
    title: 'Surface Crack Detection using CNN',
    stack: ['Python', 'TensorFlow', 'Keras', 'OpenCV', 'Scikit-learn'],
    github: 'https://github.com/paraspingale-hub/CNN_Casestudy',
    highlights: [
      'Built a binary CNN classifier for industrial surface defects on a 40,000-image dataset, achieving 94.2% test accuracy.',
      'Designed a multi-stage preprocessing workflow for resizing, normalization, and augmentation.',
      'Visualized confusion matrices, ROC curves, and activation maps to guide iterative model improvement.'
    ]
  },
  {
    title: 'Automated ML Algorithm Selection System',
    stack: ['Python', 'Scikit-learn', 'Pandas', 'NumPy', 'Matplotlib'],
    github: 'https://github.com/paraspingale-hub/Automated-machine-learning-algorithm-selection-system',
    highlights: [
      'Built an AutoML framework that benchmarks 7+ algorithms across regression, classification, and clustering tasks.',
      'Automatically selects the best performer by Accuracy, F1, and RMSE.',
      'Automated GridSearchCV hyperparameter tuning and result visualization to remove manual trial-and-error.'
    ]
  },
  {
    title: 'Study Tracker Analytics Platform',
    stack: ['Java', 'React', 'MySQL', 'Power BI'],
    github: 'https://github.com/paraspingale-hub/ScholarLog',
    highlights: [
      'Architected a Java and React application that structures raw interaction logs into a centralized data warehousing schema.',
      'Executed SQL in MySQL using joins and indexing to optimize query execution for analytics.'
    ]
  },
  {
    title: 'Logic Building',
    stack: ['Java', 'C++', 'C', 'Python'],
    github: 'https://github.com/paraspingale-hub/Logic-building-',
    highlights: ['A comprehensive collection of algorithmic and logic-building problems solved across multiple languages and domains.']
  },
  {
    title: 'Machine Learning Case Studies',
    stack: ['Python', 'Supervised Learning', 'Unsupervised Learning', 'Reinforcement Learning'],
    github: 'https://github.com/paraspingale-hub/Machine_LearningCaseStudy',
    highlights: ['A collection of machine-learning case studies that clarify the working and flow of model building across supervised, unsupervised, and reinforcement learning.']
  }
];

function ProjectPage() {
  return (
    <main className="projects-page">
      <a className="projects-back" href="#home">← Back to portfolio</a>
      <header className="projects-intro"><p>SELECTED WORK / 2026</p><h1>Project section</h1></header>
      <section className="project-list" aria-label="Selected projects">
        {projects.map((project, index) => (
          <article className={`project-row ${index % 2 ? 'is-reversed' : ''}`} key={project.title}>
            <a className="project-stack" href={project.github} target="_blank" rel="noreferrer" aria-label={`Open ${project.title} on GitHub`}>
              <span className="stack-label">MAIN TECH STACK</span>
              <span className="stack-grid" aria-hidden="true" />
              <span className="stack-name">{project.stack.slice(0, 2).join(' · ')}</span>
              <span className="stack-tags">{project.stack.slice(2).map((item) => <i key={item}>{item}</i>)}</span>
              <span className="project-visit"><b>↗</b><small>VIEW<br />GITHUB</small></span>
            </a>
            <div className="project-description">
              <p className="project-number">{String(index + 1).padStart(2, '0')}</p>
              <h2>{project.title}</h2>
              <ul>{project.highlights.map((highlight) => <li key={highlight}>{highlight}</li>)}</ul>
              <a href={project.github} target="_blank" rel="noreferrer">View repository <span>↗</span></a>
            </div>
          </article>
        ))}
      </section>
    </main>
  );
}

const techGroups = [
  { title: 'Programming Languages', icon: '▣', items: [['Python', 'python/python-original.svg'], ['Java', 'java/java-original.svg'], ['C++', 'cplusplus/cplusplus-original.svg'], ['C', 'c/c-original.svg'], ['Go', 'go/go-original.svg'], ['PHP', 'php/php-original.svg']] },
  { title: 'Frontend Development', icon: '▱', items: [['HTML', 'html5/html5-original.svg'], ['CSS', 'css3/css3-original.svg'], ['React', 'react/react-original.svg'], ['Three.js', 'builtin:threejs']] },
  { title: 'Databases', icon: '▤', items: [['SQL', 'mysql/mysql-original.svg'], ['PL/SQL', 'oracle/oracle-original.svg'], ['MongoDB', 'mongodb/mongodb-original.svg']] },
  { title: 'Analytics & BI', icon: '◫', items: [['Power BI', 'builtin:powerbi'], ['Tableau', 'builtin:tableau']] },
  { title: 'DevOps & Cloud', icon: '☁', items: [['CI/CD', 'githubactions/githubactions-original.svg'], ['Docker', 'docker/docker-original.svg'], ['AWS', 'amazonwebservices/amazonwebservices-original-wordmark.svg']] },
  { title: 'Machine Learning', icon: '✦', items: [['Tensor Flow', 'tensorflow/tensorflow-original.svg'], ['Keras', 'keras/keras-original.svg'], ['Pytorch', 'pytorch/pytorch-original.svg'], ['SKLearn', 'scikitlearn/scikitlearn-original.svg'], ['Hugging Face', 'https://cdn.simpleicons.org/huggingface/FFD21E']] },
  { title: 'Development Tools', icon: '⌘', items: [['Jupyter Notebook', 'jupyter/jupyter-original.svg'], ['VS Code', 'vscode/vscode-original.svg'], ['Google Colab', 'https://cdn.simpleicons.org/googlecolab/F9AB00'], ['Anaconda', 'anaconda/anaconda-original.svg']] }
];

function TechLogo({ name, logo }) {
  if (logo === 'builtin:threejs') return <svg className="tech-logo tech-logo-three" viewBox="0 0 64 64" aria-hidden="true"><path d="M32 5 57 50 32 60 7 50Z" /><path d="m32 5 7 45-7 10-7-10zM7 50l25-12 25 12" /></svg>;
  if (logo === 'builtin:powerbi') return <svg className="tech-logo tech-logo-powerbi" viewBox="0 0 64 64" aria-hidden="true"><path d="M10 27h10v29H10zM24 18h10v38H24zM38 10h10v46H38zM52 4h8v52h-8z" /></svg>;
  if (logo === 'builtin:tableau') return <svg className="tech-logo tech-logo-tableau" viewBox="0 0 64 64" aria-hidden="true"><path d="M32 5v54M5 32h54M14 14l36 36M50 14 14 50" /><path d="m32 15 3 14-3 8-3-8zm0 34 3-14-3-8-3 8zM15 32l14-3 8 3-8 3zm34 0-14-3-8 3 8 3z" /></svg>;
  return <img src={logo.startsWith('http') ? logo : `https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/${logo}`} alt={`${name} logo`} />;
}

function TechStackPage() {
  return (
    <main className="tech-page">
      <a className="tech-back" href="#home">← Back to portfolio</a>
      <header className="tech-intro"><p><span>&lt;&gt;</span> SKILLS</p><h1>My technical expertise</h1></header>
      <section className="tech-groups" aria-label="Technical expertise">
        {techGroups.map((group) => (
          <article className="tech-group" key={group.title}>
            <h2><span>{group.icon}</span>{group.title}</h2>
            <div className="tech-items">
              {group.items.map(([name, logo]) => (
                <div className="tech-item" key={name}>
                  <TechLogo name={name} logo={logo} /><p>{name}</p><i />
                </div>
              ))}
            </div>
          </article>
        ))}
      </section>
    </main>
  );
}

function AboutPage() {
  return (
    <main className="about-page">
      <a className="about-back" href="#home">← Back to portfolio</a>
      <section className="about-hero-section">
        <div className="about-code-wrap">
          <p className="about-eyebrow">PARAS RAHUL PINGALE&nbsp; // &nbsp;AI / ML ENGINEER&nbsp; // &nbsp;PUNE</p>
          <h1>Hi, my name is Paras<span>.</span></h1>
          <div className="about-code" aria-label="Professional profile in Java format">
            <div className="about-code-top"><span><i /><i /><i /></span><b>ParasPingale.java</b></div>
            <pre><code><span className="code-keyword">package</span> profile;{`\n\n`}<span className="code-keyword">public final class</span> <span className="code-type">ParasPingale</span> <span className="code-keyword">implements</span> <span className="code-type">AIMLEngineer</span> {'{'}{`\n`}  <span className="code-keyword">private final</span> String role = <span className="code-string">"AI / ML Engineer"</span>;{`\n`}  <span className="code-keyword">private final</span> String location = <span className="code-string">"Pune, Maharashtra"</span>;{`\n`}  <span className="code-keyword">private final</span> String education = <span className="code-string">"B.E. AI & Data Science · CGPA 8.6"</span>;{`\n\n`}  <span className="code-keyword">private final</span> String[] focus = {'{'}{`\n`}    <span className="code-string">"Deep Learning"</span>, <span className="code-string">"Generative AI"</span>, <span className="code-string">"LLMs & RAG"</span>,{`\n`}    <span className="code-string">"Computer Vision"</span>, <span className="code-string">"Production ML"</span>{`\n`}  {'}'};{`\n\n`}  <span className="code-keyword">public</span> String <span className="code-method">mission</span>() {'{'}{`\n`}    <span className="code-keyword">return</span> <span className="code-string">"Building useful AI systems, from ideas to impact."</span>;{`\n`}  {'}'}{`\n`}{'}'}</code></pre>
          </div>
          <p className="about-role-line">AI / ML ENGINEER &nbsp;//&nbsp; DEEP LEARNING &nbsp;//&nbsp; GENERATIVE AI</p>
        </div>
        <figure className="about-photo about-photo-professional"><img src={professionalPhoto} alt="Portrait of Paras Rahul Pingale" /></figure>
      </section>

      <section className="about-life-section">
        <div className="about-life-copy">
          <p className="about-eyebrow">OFF THE CLOCK&nbsp; // &nbsp;THE HUMAN SIDE</p>
          <h2>More than the work.</h2>
          <div className="life-notes">
            <article><span>01</span><div><h3>Nature photographer</h3><p>I chase quiet landscapes and honest light, using photography to notice the small stories that usually pass by.</p></div></article>
            <article><span>02</span><div><h3>Blog writer</h3><p>I turn ideas, learning, and everyday observations into clear, thoughtful writing worth sharing.</p></div></article>
            <article><span>03</span><div><h3>Psychology learner</h3><p>I explore psychological skills to better understand people, build empathy, and communicate with more intention.</p></div></article>
          </div>
        </div>
        <figure className="about-photo about-photo-personal"><img src={personalPhoto} alt="Paras holding a camera by the water" /><figcaption>LOOKING CLOSER, STAYING CURIOUS.</figcaption></figure>
      </section>
    </main>
  );
}

function App() {
  const [theme, setTheme] = useState('dark');
  const [active, setActive] = useState('Home');
  const [menuOpen, setMenuOpen] = useState(false);
  const [buildFilter, setBuildFilter] = useState('all');
  const [isBuildPage, setIsBuildPage] = useState(() => window.location.hash === '#building');
  const [isProjectsPage, setIsProjectsPage] = useState(() => window.location.hash === '#projects');
  const [isTechPage, setIsTechPage] = useState(() => window.location.hash === '#tech-stack');
  const [isAboutPage, setIsAboutPage] = useState(() => window.location.hash === '#about');

  useEffect(() => {
    document.documentElement.dataset.theme = theme;
  }, [theme]);

  useEffect(() => {
    const syncBuildPage = () => {
      const showingBuildPage = window.location.hash === '#building';
      const showingProjectsPage = window.location.hash === '#projects';
      const showingTechPage = window.location.hash === '#tech-stack';
      const showingAboutPage = window.location.hash === '#about';
      setIsBuildPage(showingBuildPage);
      setIsProjectsPage(showingProjectsPage);
      setIsTechPage(showingTechPage);
      setIsAboutPage(showingAboutPage);
      if (showingBuildPage || showingProjectsPage || showingTechPage || showingAboutPage) window.scrollTo(0, 0);
    };
    window.addEventListener('hashchange', syncBuildPage);
    return () => window.removeEventListener('hashchange', syncBuildPage);
  }, []);

  const selectNav = (item) => {
    setActive(item);
    setMenuOpen(false);
  };

  if (isBuildPage) {
    return <BuildProcess filter={buildFilter} onFilterChange={setBuildFilter} isStandalone />;
  }

  if (isProjectsPage) {
    return <ProjectPage />;
  }

  if (isTechPage) {
    return <TechStackPage />;
  }

  if (isAboutPage) {
    return <AboutPage />;
  }

  return (
    <main className="portfolio-shell">
      <ConstellationCanvas />
      <div className="grain" aria-hidden="true" />
      <header className="topbar">
        <a className="brand" href="#home" aria-label="Paras Rahul Pingale home">
          <span className="monogram">PR</span>
          <span className="brand-divider" />
          <span className="brand-copy"><small>CREATIVE DEVELOPER</small><b>BUILDING FOR THE FUTURE</b></span>
        </a>

        <nav className={`navigation ${menuOpen ? 'is-open' : ''}`} aria-label="Main navigation">
          {navItems.map((item) => (
            <button key={item} className={active === item ? 'active' : ''} onClick={() => selectNav(item)}>{item}</button>
          ))}
          <button onClick={() => selectNav('More')} className="more-link">More <span>⌄</span></button>
          <span className="nav-separator" />
          <button className="availability" aria-label="Availability status"><i /> Available</button>
        </nav>

        <div className="header-actions">
          <button className="theme-toggle" onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')} aria-label="Toggle light and dark mode">
            <span className="sun">☼</span><span className="moon">☾</span>
          </button>
          <button className="menu-toggle" onClick={() => setMenuOpen(!menuOpen)} aria-label="Open navigation menu"><span /><span /></button>
        </div>
      </header>

      <section className="hero" id="home">
        <p className="eyebrow"><span /> DIGITAL CRAFT, HUMAN FOCUS</p>
        <h1><span>PARAS</span><span>RAHUL</span><span>PINGALE</span></h1>
        <div className="hero-bottom-copy">
          <p>DEVELOPER&nbsp; • &nbsp;CREATOR&nbsp; • &nbsp;THINKER&nbsp; • &nbsp;LEARNER</p>
          <p className="signature">making ideas <em>move.</em></p>
        </div>
      </section>

      <footer className="meta-row">
        <div className="location">
          <MaharashtraMark />
          <p><strong>BASED IN PUNE,</strong><span>MAHARASHTRA, INDIA</span></p>
        </div>
        <p className="scroll-cue"><span className="scroll-line" /> SCROLL TO EXPLORE</p>
        <div className="role"><span className="role-icon">🤖</span><p><strong></strong><span>PROBLEM SOLVER</span></p></div>
      </footer>

      <section className="system-map" id="explore">
        <div className="section-kicker"><span /> NAVIGATE THE SYSTEM</div>
        <div className="system-heading"><p>ONE DESK. SIX PATHS.</p><h2>Explore the work <em>behind</em> the screen.</h2></div>
        <div className="system-stage">
          <svg className="circuit-arrows" viewBox="0 0 1400 680" aria-hidden="true" preserveAspectRatio="none">
            <defs><marker id="arrowhead" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9" /></marker></defs>
            
          </svg>
          <div className="path-links path-left">
            <a href="#about"><span>01</span> ABOUT ME <b>↖</b></a>
            <a href="#certifications"><span>02</span> CERTIFICATIONS <b>↖</b></a>
            <a href="#experience"><span>03</span> EXPERIENCE <b>↖</b></a>
          </div>
          <DesktopSetup />
          <div className="path-links path-right">
            <a href="#tech-stack"><span>04</span> TECH STACK <b>↗</b></a>
            <a href="#projects"><span>05</span> PROJECTS <b>↗</b></a>
            <a href="#building"><span>06</span> BUILD PROCESS <b>↗</b></a>
          </div>
        </div>
        <div className="contact-dock">
          <p><span /> INTERLINKED WITH WHAT I BUILD</p>
          <div className="social-links">
            <SocialIcon type="linkedin" href="https://www.linkedin.com/in/paraspingale" title="Visit Paras Pingale on LinkedIn"><svg viewBox="0 0 24 24"><path d="M6.5 8.4H3.2V21h3.3V8.4zM4.8 3A1.9 1.9 0 1 0 4.8 6.8 1.9 1.9 0 0 0 4.8 3zM20.9 13.8c0-3.8-2-5.6-4.7-5.6-2.2 0-3.1 1.2-3.6 2v-1.8H9.3V21h3.3v-6.2c0-1.6.3-3.2 2.3-3.2 2 0 2 1.8 2 3.3V21h3.3v-7.2z" /></svg></SocialIcon>
            <SocialIcon type="github" href="https://github.com/paraspingale-hub" title="Visit Paras Pingale on GitHub"><svg viewBox="0 0 24 24"><path d="M12 2.4A9.6 9.6 0 0 0 9 21.1c.5.1.7-.2.7-.5v-1.8c-2.8.6-3.4-1.2-3.4-1.2-.5-1.2-1.1-1.5-1.1-1.5-.9-.6.1-.6.1-.6 1 .1 1.6 1.1 1.6 1.1.9 1.6 2.4 1.1 3 .9.1-.6.4-1.1.7-1.3-2.3-.3-4.7-1.1-4.7-5a3.9 3.9 0 0 1 1-2.7c-.1-.2-.4-1.2.1-2.7 0 0 .8-.3 2.8 1.1a9.8 9.8 0 0 1 5.1 0c2-1.4 2.8-1.1 2.8-1.1.5 1.5.2 2.5.1 2.7a3.9 3.9 0 0 1 1 2.7c0 3.8-2.4 4.7-4.7 5 .4.3.7.9.7 1.8v2.7c0 .3.2.6.7.5A9.6 9.6 0 0 0 12 2.4z" /></svg></SocialIcon>
            <SocialIcon type="email" href="https://mail.google.com/mail/?view=cm&fs=1&to=paraspingales%40gmail.com" title="Compose an email to paraspingales@gmail.com"><svg viewBox="0 0 24 24"><path d="M3.1 5.5h17.8c.7 0 1.2.5 1.2 1.2v10.6c0 .7-.5 1.2-1.2 1.2H3.1c-.7 0-1.2-.5-1.2-1.2V6.7c0-.7.5-1.2 1.2-1.2zm.5 2.1v.2l8.4 5.8 8.4-5.8v-.2H3.6zm16.8 8.8V9.8L12 15.6 3.6 9.8v6.6h16.8z" /></svg></SocialIcon>
          </div>
        </div>
      </section>
    </main>
  );
}

createRoot(document.getElementById('root')).render(<App />);
