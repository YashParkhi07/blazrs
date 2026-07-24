document.addEventListener('DOMContentLoaded', () => {
    // Accordion toggle functionality for services page
    const accordions = document.querySelectorAll('.accordion-item');
    accordions.forEach((item) => {
        const trigger = item.querySelector('.accordion-trigger');
        const content = item.querySelector('.accordion-content');

        if (trigger && content) {
            // Set initial state for accessibility
            trigger.setAttribute('aria-expanded', 'false');
            content.setAttribute('aria-hidden', 'true');

            trigger.addEventListener('click', () => {
                const isOpen = item.classList.contains('open');
                
                // Toggle current item
                if (isOpen) {
                    item.classList.remove('open');
                    trigger.setAttribute('aria-expanded', 'false');
                    content.setAttribute('aria-hidden', 'true');
                } else {
                    item.classList.add('open');
                    trigger.setAttribute('aria-expanded', 'true');
                    content.setAttribute('aria-hidden', 'false');
                }
            });
        }
    });

    // Contact form handling
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();

            const submitBtn = document.getElementById('contact-submit');
            const successMsg = document.getElementById('form-success');

            // Disable button during "send"
            submitBtn.disabled = true;
            submitBtn.textContent = 'SENDING...';

            // Simulate sending (replace with real endpoint)
            setTimeout(() => {
                submitBtn.textContent = 'SENT ✓';
                successMsg.classList.add('visible');
                contactForm.reset();

                // Reset button after a moment
                setTimeout(() => {
                    submitBtn.disabled = false;
                    submitBtn.textContent = 'SEND MESSAGE';
                }, 3000);
            }, 800);
        });
    }

    // Typing animation for homepage headline
    const typingWord = document.getElementById('typing-word');
    if (typingWord) {
        const words = ['Digital', 'AI', 'Business', 'Data', 'CRM'];
        let wordIndex = 0;
        let charIndex = words[0].length; // start with 'Digital' fully typed
        let isDeleting = true;
        let typingSpeed = 150;

        function type() {
            const currentWord = words[wordIndex];
            
            if (isDeleting) {
                // Delete characters
                typingWord.textContent = currentWord.substring(0, charIndex - 1);
                charIndex--;
                typingSpeed = 80; // Deleting is faster
            } else {
                // Type characters
                typingWord.textContent = currentWord.substring(0, charIndex + 1);
                charIndex++;
                typingSpeed = 150; // Typing speed
            }

            // Word completed typing
            if (!isDeleting && charIndex === currentWord.length) {
                // Pause at the end of the word
                typingSpeed = 2000;
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                // Word fully deleted
                isDeleting = false;
                // Move to next word
                wordIndex = (wordIndex + 1) % words.length;
                typingSpeed = 500; // Small pause before starting next word
            }

            setTimeout(type, typingSpeed);
        }

        // Start typing loop after an initial pause
        setTimeout(type, 1500);
    }
});
