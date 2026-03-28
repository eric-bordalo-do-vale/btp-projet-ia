// WebLLM Chatbot Integration
let chatEngine = null;
let isModelLoading = false;
let chatHistory = [];
let webGPUAvailable = false;
let mlcEngineLoaded = false;
let chatbotInitialized = false;
const CHAT_HISTORY_KEY = 'chatbot_history';

// Check WebGPU availability
async function checkWebGPUSupport() {
    try {
        if (!navigator.gpu) {
            webGPUAvailable = false;
            return false;
        }
        const adapter = await navigator.gpu.requestAdapter();
        webGPUAvailable = !!adapter;
        return webGPUAvailable;
    } catch (error) {
        console.warn('WebGPU check failed:', error);
        webGPUAvailable = false;
        return false;
    }
}

// Initialize chatbot and load model
async function initChatbotAI() {
    try {
        console.log('[Chatbot] Initializing...');
        
        // Skip WebLLM loading - use simulated mode by default
        // This ensures the chatbot works immediately without waiting for CDN
        isModelLoading = false;
        updateChatbotUI('ready');
        loadChatHistory();
        
        // Display welcome message
        setTimeout(() => {
            const messages = document.getElementById('chatbox-messages');
            if (messages && messages.children.length === 0) {
                displayMessage('Bonjour! 👋 Je suis votre assistant La Tour. Comment puis-je vous aider?', 'assistant');
            }
        }, 500);
        
        console.log('[Chatbot] Ready (simulated mode)');
        return true;
    } catch (error) {
        console.error('Failed to initialize chatbot:', error);
        handleInitError(error);
        return false;
    }
}

// Load WebLLM script dynamically
function loadWebLLMScript() {
    return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm@0.2.0/lib/index.js';
        script.async = true;
        script.onload = resolve;
        script.onerror = reject;
        document.head.appendChild(script);
    });
}

// Load chat history for authenticated user
function loadChatHistory() {
    const currentUser = getCurrentUser();
    if (!currentUser) return;

    const historyKey = `${CHAT_HISTORY_KEY}_${currentUser.email}`;
    const stored = localStorage.getItem(historyKey);
    
    if (stored) {
        try {
            chatHistory = JSON.parse(stored);
            renderChatHistory();
        } catch (e) {
            console.error('Failed to parse chat history:', e);
            chatHistory = [];
        }
    }
}

// Save chat history
function saveChatHistory() {
    const currentUser = getCurrentUser();
    if (!currentUser) return;

    const historyKey = `${CHAT_HISTORY_KEY}_${currentUser.email}`;
    localStorage.setItem(historyKey, JSON.stringify(chatHistory));
}

// Get current user from localStorage
function getCurrentUser() {
    const userData = localStorage.getItem('user');
    if (!userData) return null;
    try {
        return JSON.parse(userData);
    } catch (e) {
        return null;
    }
}

// Ask AI to generate response
async function askAI(userMessage) {
    if (!userMessage.trim()) {
        console.log('[Chatbot] Empty message, ignoring');
        return;
    }
    
    console.log('[Chatbot] askAI called with:', userMessage);
    
    // Check authentication
    const user = getCurrentUser();
    console.log('[Chatbot] Current user:', user);
    
    if (!user) {
        console.log('[Chatbot] User not authenticated');
        displayMessage('Vous devez être authentifié pour utiliser le chatbot.', 'error');
        return;
    }

    try {
        // Add user message to history
        chatHistory.push({ role: 'user', content: userMessage });
        saveChatHistory();
        console.log('[Chatbot] Message added to history, total:', chatHistory.length);
        
        // Display user message
        console.log('[Chatbot] Displaying user message');
        displayMessage(userMessage, 'user');
        clearInput();
        
        // Show typing indicator
        console.log('[Chatbot] Showing typing indicator');
        showTypingIndicator();
        
        // Generate response (simulated mode by default)
        console.log('[Chatbot] Generating response...');
        const aiResponse = generateSimulatedResponse(userMessage);
        console.log('[Chatbot] Generated response:', aiResponse);
        
        // Simulate delay (1-3 seconds)
        const delayMs = 1000 + Math.random() * 2000;
        console.log('[Chatbot] Waiting', delayMs, 'ms before showing response');
        await new Promise(resolve => setTimeout(resolve, delayMs));
        
        console.log('[Chatbot] Removing typing indicator');
        removeTypingIndicator();
        
        // Add AI response to history
        chatHistory.push({ role: 'assistant', content: aiResponse });
        saveChatHistory();
        console.log('[Chatbot] Response added to history, total:', chatHistory.length);
        
        // Display AI response
        console.log('[Chatbot] Displaying AI response');
        displayMessage(aiResponse, 'assistant');
        
        console.log('[Chatbot] Done - conversation complete');
        
    } catch (error) {
        console.error('[Chatbot] Error:', error);
        removeTypingIndicator();
        displayMessage('Erreur lors de la génération de la réponse. Veuillez réessayer.', 'error');
    }
}

// Generate simulated AI response (fallback mode)
function generateSimulatedResponse(userMessage) {
    const lowerMessage = userMessage.toLowerCase();
    
    // Dynamic responses
    if (lowerMessage.includes('heure') || lowerMessage.includes('quelle heure') || lowerMessage.includes('time')) {
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        return `Il est actuellement ${hours}:${minutes}. ⏰`;
    }
    
    if (lowerMessage.includes('date') || lowerMessage.includes('jour') || lowerMessage.includes('today')) {
        const now = new Date();
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        const dateStr = now.toLocaleDateString('fr-FR', options);
        return `Nous sommes le ${dateStr}. 📅`;
    }
    
    // Keyword responses
    const responses = {
        'bonjour': 'Bonjour! 👋 Comment puis-je vous aider avec votre apprentissage?',
        'aide': 'Je suis là pour répondre à vos questions sur le code, les concepts de programmation, et bien plus. Posez votre question!',
        'comment': 'N\'hésitez pas à me poser n\'importe quelle question! Je suis ici pour vous aider.',
        'merci': 'De rien! 😊 Y a-t-il autre chose que je peux faire pour vous?',
        'javascript': 'JavaScript est un langage de programmation puissant pour le développement web et bien au-delà! Avez-vous une question spécifique?',
        'python': 'Python est un excellent choix! C\'est un langage polyvalent utilisé en développement web, data science, IA, et plus. Comment puis-je vous aider?',
        'web': 'Le développement web est passionnant! HTML, CSS, JavaScript - les technologies fondamentales du web. Quel aspect vous intéresse?',
        'mentor': 'Vous cherchez un mentor? Visitez la section "Trouver un mentor" pour rencontrer nos experts dans différents domaines!',
        'rdv': 'Vous pouvez planifier un rendez-vous avec un mentor via la section "Trouver un mentor". Ils sont disponibles pour vous aider!',
        'ça va': 'Ça va très bien, merci de demander! 😊 Et vous, comment allez-vous?',
        'qui es-tu': 'Je suis votre assistant La Tour! 🤖 Je suis là pour vous aider avec vos questions sur la programmation, l\'apprentissage, et bien plus.',
        'ton nom': 'Je m\'appelle La Tour Assistant! Je suis votre assistant intelligent de la plateforme La Tour.',
        'merci beaucoup': 'Avec plaisir! 😊 N\'hésitez pas si vous avez d\'autres questions!',
    };
    
    for (const [keyword, response] of Object.entries(responses)) {
        if (lowerMessage.includes(keyword)) {
            return response;
        }
    }
    
    // Default intelligent response
    const defaultResponses = [
        'C\'est une bonne question! Je suis actuellement en mode simulation. Pour des réponses plus complètes, consultez nos mentors ou la documentation sur la plateforme.',
        'Intéressant! Vous pouvez trouver plus d\'informations en visitant la section "Trouver un mentor" ou en explorant les ressources disponibles.',
        'Je comprends votre question. N\'hésitez pas à me poser d\'autres questions ou à contacter un mentor pour plus d\'aide!',
        'Bonne question! Comment puis-je vous aider davantage?',
    ];
    
    return defaultResponses[Math.floor(Math.random() * defaultResponses.length)];
}

// Display message in chat
function displayMessage(content, role) {
    const messagesContainer = document.getElementById('chatbox-messages');
    if (!messagesContainer) return;
    
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message chat-message-${role}`;
    
    if (role === 'user') {
        messageDiv.innerHTML = `<div class="message-content user-message">${escapeHtml(content)}</div>`;
    } else if (role === 'assistant') {
        messageDiv.innerHTML = `<div class="message-content assistant-message">${escapeHtml(content)}</div>`;
    } else if (role === 'error') {
        messageDiv.innerHTML = `<div class="message-content error-message">${escapeHtml(content)}</div>`;
    }
    
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Render entire chat history
function renderChatHistory() {
    const messagesContainer = document.getElementById('chatbox-messages');
    if (!messagesContainer) return;
    
    messagesContainer.innerHTML = '';
    
    chatHistory.forEach(msg => {
        displayMessage(msg.content, msg.role);
    });
    
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Show typing indicator
function showTypingIndicator() {
    const messagesContainer = document.getElementById('chatbox-messages');
    if (!messagesContainer) return;
    
    const typingDiv = document.createElement('div');
    typingDiv.id = 'typing-indicator';
    typingDiv.className = 'chat-message chat-message-assistant';
    typingDiv.innerHTML = '<div class="message-content assistant-message"><span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span></div>';
    
    messagesContainer.appendChild(typingDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Remove typing indicator
function removeTypingIndicator() {
    const typingDiv = document.getElementById('typing-indicator');
    if (typingDiv) {
        typingDiv.remove();
    }
}

// Clear input field
function clearInput() {
    const input = document.getElementById('user-message');
    if (input) {
        input.value = '';
    }
}

// Update chatbot UI state
function updateChatbotUI(state) {
    const sendBtn = document.getElementById('send-btn');
    const userInput = document.getElementById('user-message');
    
    if (!sendBtn || !userInput) return;
    
    if (state === 'loading') {
        sendBtn.disabled = true;
        userInput.disabled = true;
        sendBtn.textContent = '⏳ Chargement...';
    } else if (state === 'ready') {
        sendBtn.disabled = false;
        userInput.disabled = false;
        sendBtn.textContent = 'Envoyer';
    } else if (state === 'error') {
        sendBtn.disabled = true;
        userInput.disabled = true;
        sendBtn.textContent = '❌ Erreur';
    }
}

// Show initialization warning
function showInitializationWarning() {
    const warning = document.createElement('div');
    warning.className = 'webgpu-warning';
    warning.innerHTML = `
        <strong>⚠️ Initialisation en cours...</strong><br>
        <small>Le chatbot IA se charge. Veuillez attendre quelques secondes. 
        Pour une expérience optimale, utilisez Chrome 113+, Edge 113+ ou Firefox 118+ avec WebGPU activé.</small>
    `;
    
    const container = document.getElementById('chatbox-messages');
    if (container) {
        container.innerHTML = '';
        container.appendChild(warning);
    }
}

// Show model loading error
function showModelLoadingError() {
    const warning = document.createElement('div');
    warning.className = 'webgpu-warning';
    warning.innerHTML = `
        <strong>⚠️ Le modèle n'a pas pu être chargé</strong><br>
        <small>Le chatbot fonctionne en mode simulé. Pour utiliser l'IA complète, assurez-vous que WebGPU est activé sur votre navigateur.</small>
    `;
    
    const container = document.getElementById('chatbox-messages');
    if (container) {
        container.innerHTML = '';
        container.appendChild(warning);
    }
    
    // Display initial greeting in sim mode
    setTimeout(() => {
        displayMessage('Bonjour! 👋 Je suis votre assistant La Tour. Comment puis-je vous aider?', 'assistant');
    }, 500);
}

// Show WebGPU warning
function showWebGPUWarning() {
    const warning = document.createElement('div');
    warning.className = 'webgpu-warning';
    warning.innerHTML = `
        <strong>⚠️ WebGPU non disponible</strong><br>
        <small>Votre navigateur ne supporte pas WebGPU. Le chatbot fonctionne en mode simulé. 
        Pour une expérience optimale, utilisez Chrome 113+, Edge 113+ ou Firefox 118+ avec WebGPU.</small>
    `;
    
    const container = document.getElementById('chatbox-messages');
    if (container) {
        container.innerHTML = '';
        container.appendChild(warning);
    }
    
    // Display initial greeting in sim mode
    setTimeout(() => {
        displayMessage('Bonjour! 👋 Je suis votre assistant La Tour. Comment puis-je vous aider?', 'assistant');
    }, 500);
    
    updateChatbotUI('ready');
}

// Handle initialization errors
function handleInitError(error) {
    console.error('Chatbot init error:', error);
    
    if (!navigator.gpu) {
        showWebGPUWarning();
    } else {
        const errorMsg = 'Le chatbot IA n\'a pas pu être initialisé. Veuillez rafraîchir la page.';
        const container = document.getElementById('chatbox-messages');
        if (container) {
            container.innerHTML = `<div class="chat-message"><div class="message-content error-message">${errorMsg}</div></div>`;
        }
        updateChatbotUI('error');
    }
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Show message helper
function showMessage(text, type = 'info') {
    displayMessage(text, type);
}

// Setup event listeners for chatbot widget
function setupChatbotListeners() {
    // Prevent multiple initializations
    if (chatbotInitialized) {
        console.log('[Chatbot] Already initialized, skipping setupChatbotListeners');
        return;
    }
    chatbotInitialized = true;
    
    const sendBtn = document.getElementById('send-btn');
    const userInput = document.getElementById('user-message');
    const toggleBtn = document.getElementById('chatbot-toggle-btn');
    const widget = document.getElementById('chatbot-widget');
    const closeBtn = document.getElementById('chatbot-close-btn');
    
    console.log('[Chatbot] Setting up listeners...', { sendBtn, userInput, toggleBtn, widget, closeBtn });
    
    if (sendBtn) {
        sendBtn.addEventListener('click', () => {
            console.log('[Chatbot] Send button clicked');
            const message = userInput.value;
            if (message.trim()) {
                console.log('[Chatbot] Sending message:', message);
                askAI(message);
            }
        });
    }
    
    if (userInput) {
        userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                console.log('[Chatbot] Enter key pressed');
                const message = userInput.value;
                if (message.trim()) {
                    console.log('[Chatbot] Sending message via Enter:', message);
                    askAI(message);
                }
            }
        });
    }
    
    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            console.log('[Chatbot] Toggle button clicked');
            if (widget) {
                console.log('[Chatbot] Before toggle - classes:', widget.className);
                widget.classList.toggle('open');
                console.log('[Chatbot] After toggle - classes:', widget.className);
            }
        });
    }
    
    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            console.log('[Chatbot] Close button clicked');
            if (widget) {
                widget.classList.remove('open');
                console.log('[Chatbot] Widget closed');
            }
        });
    }
    
    console.log('[Chatbot] Listeners setup complete');
}

// Hide widget (for dedicated chatbot page)
function hideChatbotWidget() {
    const widget = document.getElementById('chatbot-widget');
    if (widget) {
        widget.style.display = 'none';
    }
}

// Show widget (for other pages)
function showChatbotWidget() {
    const widget = document.getElementById('chatbot-widget');
    if (widget) {
        widget.style.display = 'flex';
    }
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', function() {
    console.log('[Chatbot] DOMContentLoaded - checking for user');
    
    function tryInitializeChatbot() {
        const currentUser = getCurrentUser();
        console.log('[Chatbot] Checking user:', currentUser ? currentUser.email : 'NOT logged in');
        
        if (currentUser) {
            console.log('[Chatbot] User authenticated, initializing chatbot');
            // Only initialize for authenticated users
            setupChatbotListeners();
            
            // Load chat history immediately
            loadChatHistory();
            
            // Initialize model asynchronously (don't block UI)
            setTimeout(() => {
                initChatbotAI();
            }, 500);
            
            return true;
        }
        return false;
    }
    
    // Try immediately
    if (!tryInitializeChatbot()) {
        // If not authenticated yet, check every 500ms for up to 30 seconds
        let attempts = 0;
        const checkInterval = setInterval(() => {
            attempts++;
            console.log('[Chatbot] Attempt', attempts, 'to find user');
            
            if (tryInitializeChatbot()) {
                clearInterval(checkInterval);
                console.log('[Chatbot] Successfully initialized after login');
            } else if (attempts > 60) {
                clearInterval(checkInterval);
                console.log('[Chatbot] User never logged in within 30 seconds');
            }
        }, 500);
    }
});
