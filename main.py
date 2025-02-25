<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Portfolio & Registration Form</title>
  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap" rel="stylesheet">
  <style>
    /* Global Styles */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Poppins', sans-serif;
      scroll-behavior: smooth;
    }
    body {
      background: linear-gradient(135deg, #001f3f, #002f5f);
      color: #f5f5dc;
      text-align: center;
      line-height: 1.6;
    }
    a {
      color: inherit;
    }
    /* Navigation Bar */
    nav {
      background: linear-gradient(90deg, #001f3f, #002f5f);
      padding: 15px 30px;
      display: flex;
      align-items: center;
      position: fixed;
      width: 100%;
      top: 0;
      left: 0;
      z-index: 1000;
      box-shadow: 0 2px 5px rgba(0,0,0,0.3);
    }
    .logo {
      font-size: 1.8em;
      font-weight: 700;
      color: #f5f5dc;
    }
    nav ul {
      list-style: none;
      display: flex;
      margin: 0;
      margin-right: auto;
      padding: 0;
    }
    nav ul li {
      margin: 0 15px;
    }
    nav ul li a {
      text-decoration: none;
      color: #f5f5dc;
      font-size: 1.1em;
      transition: color 0.3s;
    }
    nav ul li a:hover {
      color: #d2b48c;
    }
    .signup-btn {
      background: #f5f5dc;
      color: #001f3f;
      border: none;
      border-radius: 5px;
      padding: 8px 16px;
      font-size: 1em;
      cursor: pointer;
      transition: background 0.3s, transform 0.3s;
    }
    .signup-btn:hover {
      background: #d2b48c;
      transform: scale(1.05);
    }
    /* Sections */
    .section {
      padding: 100px 20px 80px;
      max-width: 900px;
      margin: 0 auto;
    }
    .section-title {
      font-size: 2.5em;
      font-weight: 700;
      margin-bottom: 20px;
      border-bottom: 2px solid #f5f5dc;
      display: inline-block;
      padding-bottom: 5px;
    }
    /* Portfolio Section */
    #portfolio-section {
      display: block;
      margin-top: 80px; /* Pour compenser la nav fixe */
    }
    /* Hero Section sans image de fond */
    #hero {
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      padding: 20px;
    }
    .profile-img {
      width: 150px;
      height: 150px;
      border-radius: 50%;
      margin-bottom: 20px;
      border: 4px solid #f5f5dc;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
    }
    /* Texte amélioré pour "Welcome to My Portfolio" */
    #hero h1 {
      font-size: 4em;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 3px;
      margin-bottom: 20px;
      color: #f5f5dc;
      text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
      opacity: 0;
      animation: fadeIn 2s forwards;
    }
    #hero p {
      font-size: 1.6em;
      font-weight: 300;
      margin-top: 10px;
      color: #dcdcdc;
      line-height: 1.4;
      opacity: 0;
      animation: fadeIn 2s 0.5s forwards;
    }
    @keyframes fadeIn {
      to { opacity: 1; }
    }
    /* Projects Section */
    .projects-container {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 20px;
      margin-top: 30px;
    }
    .project-card {
      background: #f5f5dc;
      color: #001f3f;
      padding: 20px;
      width: 280px;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
      text-align: center;
      transition: transform 0.3s, box-shadow 0.3s;
    }
    .project-card:hover {
      transform: translateY(-10px);
      box-shadow: 0 6px 15px rgba(0,0,0,0.3);
    }
    .project-card h3 {
      font-size: 1.5em;
      margin-bottom: 10px;
    }
    /* Contact Section */
    #contact p {
      font-size: 1.2em;
      margin: 5px 0;
    }
    /* Registration Form Section */
    #form-section {
      display: none;
      padding-top: 120px; /* Pour compenser la nav fixe */
    }
    #form-section form {
      background: rgba(0, 0, 0, 0.6);
      padding: 20px;
      border-radius: 10px;
      width: 400px;
      margin: 0 auto;
      box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    #form-section form h2 {
      margin-bottom: 20px;
      text-align: center;
    }
    #form-section form label {
      display: block;
      margin: 10px 0 5px;
      text-align: left;
    }
    #form-section form input,
    #form-section form select {
      width: 100%;
      padding: 8px;
      border: none;
      border-radius: 5px;
      margin-bottom: 10px;
    }
    #form-section form input[type="submit"],
    #form-section form button.back-btn {
      background: #f5f5dc;
      color: #001f3f;
      font-weight: bold;
      cursor: pointer;
      transition: background 0.3s;
      border: none;
      padding: 10px 20px;
      border-radius: 5px;
    }
    #form-section form input[type="submit"]:hover,
    #form-section form button.back-btn:hover {
      background: #d2b48c;
    }
    /* Custom File Input */
    .custom-file-label {
      display: inline-block;
      padding: 8px 12px;
      background: #f5f5dc;
      color: #001f3f;
      border-radius: 5px;
      cursor: pointer;
      margin-bottom: 10px;
      transition: background 0.3s;
    }
    .custom-file-label:hover {
      background: #d2b48c;
    }
    /* Footer */
    footer {
      text-align: center;
      padding: 20px;
      background: rgba(0, 0, 50, 0.9);
      color: #f5f5dc;
      margin-top: 40px;
    }
    /* Responsive ajustement */
    @media (max-width: 480px) {
      #hero h1 {
        font-size: 2.8em;
      }
      #hero p {
        font-size: 1.2em;
      }
      .signup-btn {
        padding: 6px 12px;
        font-size: 0.9em;
      }
      #form-section form {
        width: 90%;
      }
    }
  </style>
</head>
<body>
  <!-- Navigation Bar -->
  <nav>
    <div class="logo">Zeroual Assiya</div>
    <ul>
      <li><a href="#" onclick="showSection('portfolio')">Home</a></li>
      <li><a href="#about">About</a></li>
      <li><a href="#projects">Projects</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
    <!-- Bouton Sign Up positionné en haut à droite -->
    <button class="signup-btn" onclick="showSection('form')">Sign Up</button>
  </nav>

  <!-- Portfolio Section -->
  <div id="portfolio-section">
    <!-- Hero Section -->
    <section id="hero">
      <img src="photo-profil.jpg" alt="Profile Photo" class="profile-img">
      <h1>Welcome to My Portfolio </h1>
      <p>I'm a software and data engineer.<br><br>Discover my work and projects.</p>
    </section>

    <!-- About Section -->
    <section id="about" class="section">
      <h2 class="section-title">About Me</h2>
      <p>Hello, my name is Zeroual Assiya, and I am a Software and Data Engineering student at ENSAKH.
      Throughout my studies, I have developed a strong foundation in software development and data management.
      I have worked on various academic projects involving database design and data processing, which have helped me enhance my technical and problem-solving skills.
      Passionate about technology and data-driven solutions, I am eager to apply my knowledge in real-world projects and continuously expand my expertise in this dynamic field.</p>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="section">
      <h2 class="section-title">Projects</h2>
      <div class="projects-container">
        <div class="project-card">
          <h3>Project 1</h3>
          <p>Traitement d'image (Python)</p>
        </div>
        <div class="project-card">
          <h3>Project 2</h3>
          <p>Projet de gestion de base de données (gestion des avions) (SQL)</p>
        </div>
        <div class="project-card">
          <h3>Project 3</h3>
          <p>This portfolio</p>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section">
      <h2 class="section-title">Contact Me</h2>
      <p>Email: <a href="mailto:lascience.doc22@gmail.com" style="color: #f5f5dc; text-decoration: underline;">lascience.doc22@gmail.com</a></p>
    </section>
  </div>

  <!-- Registration Form Section -->
  <div id="form-section">
    <form action="#" method="post" enctype="multipart/form-data">
      <h2>Registration Form</h2>

      <label for="firstName">First Name</label>
      <input type="text" id="firstName" name="firstName" required>

      <label for="lastName">Last Name</label>
      <input type="text" id="lastName" name="lastName" required>

      <label for="formEmail">Email</label>
      <input type="email" id="formEmail" name="email" required>

      <label for="password">Password</label>
      <input type="password" id="password" name="password" required>

      <label for="phone">Phone Number</label>
      <input type="tel" id="phone" name="phone" pattern="\+?\d{10,15}" placeholder="+1234567890" required>

      <label for="gender">Gender</label>
      <select id="gender" name="gender" required>
        <option value="">Select</option>
        <option value="male">Male</option>
        <option value="female">Female</option>
      </select>

      <label for="dob">Date of Birth</label>
      <input type="date" id="dob" name="dob" required>

      <!-- Custom File Input -->
      <label for="picture" class="custom-file-label">Select a picture</label>
      <input type="file" id="picture" name="picture" accept="image/*" style="display: none;">

      <input type="submit" value="Submit">
      <!-- Bouton pour revenir à la section Portfolio -->
      <button type="button" class="back-btn" onclick="showSection('portfolio')" style="margin-top:10px;">Back</button>
    </form>
  </div>

  <!-- Footer -->
  <footer>
    thank you for your visit (^_^)
  </footer>

  <script>
    function showSection(section) {
      if(section === 'form') {
        document.getElementById('portfolio-section').style.display = 'none';
        document.getElementById('form-section').style.display = 'block';
      } else {
        document.getElementById('form-section').style.display = 'none';
        document.getElementById('portfolio-section').style.display = 'block';
      }
    }
    // Mise à jour du label de fichier personnalisé
    document.getElementById('picture').addEventListener('change', function(){
      var fileName = this.files.length > 0 ? this.files[0].name : 'Select a picture';
      document.querySelector('.custom-file-label').textContent = fileName;
    });
  </script>
</body>
</html>
