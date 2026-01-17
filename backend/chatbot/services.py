import json
from datetime import datetime

class HealthcareChatbot:
    def __init__(self):
        self.responses = {
            "greeting": "👋 Hello! I'm CareBot from Jarrurat Care. I can help you with volunteering, donations, healthcare services, and more. How can I assist you today?",
            "volunteer": "🤝 **Volunteering Opportunities:**\n\n1. **Medical Professionals** - Doctors, nurses, paramedics\n2. **Logistics Support** - Transportation, setup, distribution\n3. **Tech Support** - Website, app, IT help\n4. **Counseling** - Mental health support\n5. **Education** - Health awareness workshops\n\n📝 **How to join:** Fill the registration form on this page!",
            "donate": "💰 **Donation Options:**\n\n• **Online:** jarruratcare.org/donate\n• **Bank Transfer:** Details on website\n• **In-kind:** Medical supplies, equipment\n• **Monthly:** Set up recurring donations\n\n💝 Every donation helps provide free healthcare to underserved communities.",
            "services": "🏥 **Our Healthcare Services:**\n\n1. **Free Medical Camps** - Regular health checkups\n2. **Vaccination Drives** - Immunization programs\n3. **Mental Health Counseling** - Professional support\n4. **Health Education** - Workshops & awareness\n5. **Emergency Support** - Mobile medical units\n6. **Telemedicine** - Remote consultations",
            "contact": "📞 **Contact Information:**\n\n• **Email:** support@jarruratcare.org\n• **Phone:** +91 9876543210\n• **Address:** Healthcare Center, Mumbai, India\n• **Hours:** Mon-Sat, 9AM-6PM\n\nWe respond within 24 hours!",
            "impact": "📊 **Our Impact (2025):**\n\n• 500+ Active volunteers\n• 50+ Medical camps organized\n• 10,000+ Patients treated\n• 5,000+ Vaccinations administered\n• 100+ Rural villages served\n\nJoin us to make a bigger impact!",
            "default": "I'm here to help Jarrurat Care in healthcare outreach. You can ask me about:\n\n• Volunteering opportunities\n• Donation methods\n• Healthcare services\n• Contact information\n• Our impact and statistics\n\nWhat would you like to know? 😊"
        }
    
    def get_response(self, user_message):
        user_msg = user_message.lower().strip()
        
        # Check for keywords
        if any(word in user_msg for word in ['hello', 'hi', 'hey', 'greetings']):
            return self.responses["greeting"]
        elif any(word in user_msg for word in ['volunteer', 'join', 'help', 'register', 'participate']):
            return self.responses["volunteer"]
        elif any(word in user_msg for word in ['donate', 'money', 'fund', 'contribute', 'sponsor']):
            return self.responses["donate"]
        elif any(word in user_msg for word in ['service', 'provide', 'medical', 'health', 'treatment', 'camp']):
            return self.responses["services"]
        elif any(word in user_msg for word in ['contact', 'email', 'phone', 'call', 'address']):
            return self.responses["contact"]
        elif any(word in user_msg for word in ['impact', 'statistic', 'number', 'achieve', 'result']):
            return self.responses["impact"]
        else:
            return self.responses["default"]