// ==========================================
// Varun K N Portfolio - Main JavaScript
// ==========================================

document.addEventListener('DOMContentLoaded', function() {
    
    // ========== Navigation ==========
    const navbar = document.getElementById('navbar');
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    
    // Sticky navigation on scroll
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
    
    // Mobile menu toggle
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
        
        // Close menu when clicking nav links
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
            });
        });
    }
    
    // ========== Scroll to Top Button ==========
    const scrollTopBtn = document.getElementById('scrollTop');
    
    if (scrollTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                scrollTopBtn.classList.add('visible');
            } else {
                scrollTopBtn.classList.remove('visible');
            }
        });
        
        scrollTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // ========== Typing Effect ==========
    const typingText = document.getElementById('typingText');
    
    if (typingText) {
        const phrases = [
            'AI Researcher',
            'IEEE Published Developer',
            'Machine Learning Engineer',
            'Deep Learning Specialist',
            'Production ML Systems Builder'
        ];
        
        let phraseIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        let typingSpeed = 100;
        
        function type() {
            const currentPhrase = phrases[phraseIndex];
            
            if (isDeleting) {
                typingText.textContent = currentPhrase.substring(0, charIndex - 1);
                charIndex--;
                typingSpeed = 50;
            } else {
                typingText.textContent = currentPhrase.substring(0, charIndex + 1);
                charIndex++;
                typingSpeed = 100;
            }
            
            if (!isDeleting && charIndex === currentPhrase.length) {
                isDeleting = true;
                typingSpeed = 2000; // Pause at end
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                phraseIndex = (phraseIndex + 1) % phrases.length;
                typingSpeed = 500; // Pause before next phrase
            }
            
            setTimeout(type, typingSpeed);
        }
        
        // Start typing effect
        setTimeout(type, 1000);
    }
    
    // ========== Alert Close Buttons ==========
    const alertCloseButtons = document.querySelectorAll('.alert-close');
    
    alertCloseButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.parentElement.style.animation = 'slideIn 0.3s ease reverse';
            setTimeout(() => {
                this.parentElement.remove();
            }, 300);
        });
    });
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.animation = 'slideIn 0.3s ease reverse';
            setTimeout(() => {
                alert.remove();
            }, 300);
        }, 5000);
    });

    // ========== Smooth Scrolling for Anchor Links ==========
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && document.querySelector(href)) {
                e.preventDefault();
                const target = document.querySelector(href);
                const offset = 80; // navbar height
                const targetPosition = target.offsetTop - offset;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // ========== Skill Progress Animation ==========
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const skillObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBars = entry.target.querySelectorAll('.skill-progress');
                progressBars.forEach(bar => {
                    bar.style.animation = 'progressAnimation 1.5s ease-out';
                });
                skillObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.skill-category').forEach(category => {
        skillObserver.observe(category);
    });
    
    // ========== Form Validation (if contact form exists) ==========
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const name = this.querySelector('[name="name"]');
            const email = this.querySelector('[name="email"]');
            const subject = this.querySelector('[name="subject"]');
            const message = this.querySelector('[name="message"]');
            
            let isValid = true;
            
            // Basic validation
            if (name && !name.value.trim()) {
                isValid = false;
                showFieldError(name, 'Name is required');
            }
            
            if (email && !isValidEmail(email.value)) {
                isValid = false;
                showFieldError(email, 'Please enter a valid email');
            }
            
            if (subject && !subject.value.trim()) {
                isValid = false;
                showFieldError(subject, 'Subject is required');
            }
            
            if (message && !message.value.trim()) {
                isValid = false;
                showFieldError(message, 'Message is required');
            }
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    }
    
    function isValidEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }
    
    function showFieldError(field, message) {
        field.style.borderColor = '#ef4444';
        const errorDiv = document.createElement('div');
        errorDiv.className = 'field-error';
        errorDiv.style.color = '#ef4444';
        errorDiv.style.fontSize = '0.875rem';
        errorDiv.style.marginTop = '0.25rem';
        errorDiv.textContent = message;
        
        // Remove existing error if any
        const existingError = field.parentElement.querySelector('.field-error');
        if (existingError) {
            existingError.remove();
        }
        
        field.parentElement.appendChild(errorDiv);
        
        // Remove error on input
        field.addEventListener('input', function() {
            this.style.borderColor = '';
            const error = this.parentElement.querySelector('.field-error');
            if (error) {
                error.remove();
            }
        });
    }
    
    // ========== Hero Video Control - Enhanced & Smart ==========
    const heroVideo = document.querySelector('#heroVideo');
    const videoContainer = document.querySelector('#videoContainer');
    const videoWrapper = document.querySelector('.video-wrapper');
    const playPrompt = document.querySelector('#playPrompt');
    const promptPlayBtn = document.querySelector('#promptPlayBtn');
    const videoOverlay = document.querySelector('#videoOverlay');
    const videoPlayBtn = document.querySelector('#videoPlayBtn');
    const videoCaptionText = document.querySelector('#videoCaptionText');
    const videoDuration = document.querySelector('#videoDuration');
    
    console.log('Video elements found:', {
        heroVideo: !!heroVideo,
        videoContainer: !!videoContainer,
        playPrompt: !!playPrompt,
        promptPlayBtn: !!promptPlayBtn
    });
    
    let hasPlayed = false;
    let isManuallyPaused = false;
    
    if (heroVideo && videoContainer) {
        console.log('Video source:', heroVideo.querySelector('source')?.src);
        console.log('Video ready state:', heroVideo.readyState);
        
        // Get and display video duration when loaded
        heroVideo.addEventListener('loadedmetadata', function() {
            console.log('Video metadata loaded, duration:', this.duration);
            const duration = Math.floor(this.duration);
            const minutes = Math.floor(duration / 60);
            const seconds = duration % 60;
            if (videoDuration) {
                videoDuration.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
            }
        });
        
        // Video error handling
        heroVideo.addEventListener('error', function(e) {
            console.error('Video loading error:', e);
            const source = this.querySelector('source');
            console.error('Video source:', source?.src);
            console.error('Error code:', this.error?.code, 'Message:', this.error?.message);
            if (playPrompt) {
                playPrompt.innerHTML = '<p style="color: #ef4444; padding: 20px;">Video failed to load. Please check the file.</p>';
            }
        });
        
        // Initial play button click
        if (promptPlayBtn) {
            promptPlayBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                startVideo();
            });
        }
        
        // Play prompt click (anywhere on overlay)
        if (playPrompt) {
            playPrompt.addEventListener('click', function() {
                startVideo();
            });
        }
        
        function startVideo() {
            console.log('Starting video...');
            heroVideo.play().then(() => {
                console.log('Video playing successfully');
                hasPlayed = true;
                isManuallyPaused = false;
                playPrompt.classList.add('hidden');
                videoWrapper.classList.add('playing');
                if (videoCaptionText) {
                    videoCaptionText.textContent = 'Now Playing';
                }
            }).catch(err => {
                console.error('Video play error:', err);
                alert('Error playing video: ' + err.message);
            });
        }
        
        // Hover overlay play/pause toggle
        if (videoPlayBtn) {
            videoPlayBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                if (heroVideo.paused) {
                    heroVideo.play();
                    isManuallyPaused = false;
                    this.innerHTML = '<i class="fas fa-pause"></i>';
                    videoWrapper.classList.add('playing');
                    if (videoCaptionText) {
                        videoCaptionText.textContent = 'Now Playing';
                    }
                } else {
                    heroVideo.pause();
                    isManuallyPaused = true;
                    this.innerHTML = '<i class="fas fa-play"></i>';
                    videoWrapper.classList.remove('playing');
                    if (videoCaptionText) {
                        videoCaptionText.textContent = 'Paused';
                    }
                }
            });
        }
        
        // Update button based on video state
        heroVideo.addEventListener('play', function() {
            if (videoPlayBtn) {
                videoPlayBtn.innerHTML = '<i class="fas fa-pause"></i>';
            }
            videoWrapper.classList.add('playing');
        });
        
        heroVideo.addEventListener('pause', function() {
            if (videoPlayBtn) {
                videoPlayBtn.innerHTML = '<i class="fas fa-play"></i>';
            }
            videoWrapper.classList.remove('playing');
        });
        
        // Video ended - show replay option
        heroVideo.addEventListener('ended', function() {
            videoWrapper.classList.remove('playing');
            if (videoCaptionText) {
                videoCaptionText.textContent = 'Click to Replay';
            }
            // Show overlay with replay option
            if (videoOverlay) {
                videoOverlay.classList.add('show');
                setTimeout(() => {
                    videoOverlay.classList.remove('show');
                }, 3000);
            }
        });
        
        // ========== SCROLL-BASED AUTO PAUSE/PLAY ==========
        const heroSection = document.querySelector('.hero');
        let lastScrollY = window.scrollY;
        
        function checkVideoVisibility() {
            if (!hasPlayed || isManuallyPaused) return;
            
            const heroRect = heroSection.getBoundingClientRect();
            const videoRect = videoContainer.getBoundingClientRect();
            
            // Check if video is in viewport (at least 50% visible)
            const isVideoVisible = (
                videoRect.top < window.innerHeight * 0.5 &&
                videoRect.bottom > window.innerHeight * 0.5
            );
            
            // Check if user scrolled away from hero section
            const hasScrolledPastHero = heroRect.bottom < window.innerHeight * 0.3;
            
            if (hasScrolledPastHero && !heroVideo.paused) {
                // User scrolled down - pause video
                heroVideo.pause();
                videoWrapper.classList.add('paused-by-scroll');
                if (videoCaptionText) {
                    videoCaptionText.textContent = 'Paused - Scroll up to continue';
                }
            } else if (!hasScrolledPastHero && heroVideo.paused && !isManuallyPaused) {
                // User scrolled back up - resume video
                heroVideo.play();
                videoWrapper.classList.remove('paused-by-scroll');
                if (videoCaptionText) {
                    videoCaptionText.textContent = 'Now Playing';
                }
            }
        }
        
        // Throttled scroll listener
        let scrollTimeout;
        window.addEventListener('scroll', function() {
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(checkVideoVisibility, 100);
        });
        
        // Check on page load
        checkVideoVisibility();
    }
    
    console.log('Portfolio loaded successfully! 🚀');
});
