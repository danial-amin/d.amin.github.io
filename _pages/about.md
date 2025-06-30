---
layout: about
title: about
permalink: /
subtitle: Fairness in Generative AI, FaAct Human Computer Interaction, User Representation, Personas for Social Good, GenAI Personas, Global South
profile:
  align: right
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular
  more_info: >
    <p>University of Vaasa</p>
    <p>Espoo, Finland</p>
    <p>+358 46 801 4291</p>
selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page
announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder
latest_posts:
  enabled: true
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 2 # leave blank to include all the blog posts
---

<div id="bio-short">
I am a <a href="#">doctoral researcher</a> at the <a href="https://personateam.xyz/members/" target=blank>University of Vaasa, Finland</a>, under the supervision of <a href="https://jonisalminen.com/" target=blank>Dr. Joni Salminen</a> focusing on <a href="#">Generative AI (GenAI) and user representation research</a>. Tandemly, I work as an AI Research Scientist at <a href="#">Samsung Design Innovation Center in France</a>, developing GenAI tools that help designers create more representative products.

<button id="read-more-btn" onclick="expandBio()" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 8px 16px; border-radius: 20px; cursor: pointer; font-size: 14px; margin-top: 10px; transition: all 0.3s ease;">Read More</button>
</div>

<div id="bio-expanded" style="display: none;">
I am a <a href="#">doctoral student</a> at the <a href="https://personateam.xyz/members/" target=blank>University of Vaasa, Finland</a>, under the supervision of <a href="https://jonisalminen.com/" target=blank>Dr. Joni Salminen</a> focusing on <a href="#">Generative AI (GenAI) and user representation research</a>.  Tandemly, I work as an AI Research Scientist at <a href="#">Samsung Design Innovation Center in France</a>, developing GenAI tools that help designers create more representative products. Previously, I have led AI teams at several companies and collaborated with the Government of Pakistan on complex engineering systems. I have a background in engineering and have earned multiple degrees in data science and business from institutions like <a href="#">MIT</a> and UC San Diego.<br>

My research centers on making <a href="#">GenAI systems fairer and more inclusive</a> towards representation of users. I study how GenAI creates user personas and work to reduce bias, especially for <a href="#">marginalized communities</a>. I use large language models and NLP to build better representations of different groups of people. My goal is ensuring GenAI systems don't perpetuate stereotypes. I also explore how GenAI can be used responsibly in design and decision-making.<br>

I speak four languages: English, Urdu, Punjabi, and some (petit :smile) French. I enjoy writing poetry and dark prose. When I am not working, I'm probably <a href="#">overthinking or cooking</a>. I have been involved in space education programs in Pakistan for many years, helping to organize events such as World Space Week. I enjoy <a href="#">mentoring startups</a> and helping them ethically utilize GenAI.
<br>
<button id="read-less-btn" onclick="collapseBio()" style="background: #6c757d; color: white; border: none; padding: 8px 16px; border-radius: 20px; cursor: pointer; font-size: 14px; margin-top: 10px; transition: all 0.3s ease;">Read Less</button>
</div>

<script>
function expandBio() {
    document.getElementById('bio-short').style.display = 'none';
    document.getElementById('bio-expanded').style.display = 'block';
}

function collapseBio() {
    document.getElementById('bio-short').style.display = 'block';
    document.getElementById('bio-expanded').style.display = 'none';
}

// Add hover effects
document.addEventListener('DOMContentLoaded', function() {
    const readMoreBtn = document.getElementById('read-more-btn');
    const readLessBtn = document.getElementById('read-less-btn');
    
    if (readMoreBtn) {
        readMoreBtn.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = '0 4px 8px rgba(102, 126, 234, 0.4)';
        });
        readMoreBtn.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 2px 4px rgba(102, 126, 234, 0.3)';
        });
    }
    
    if (readLessBtn) {
        readLessBtn.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.backgroundColor = '#5a6268';
        });
        readLessBtn.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.backgroundColor = '#6c757d';
        });
    }
});
</script>