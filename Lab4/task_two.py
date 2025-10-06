# Model-Based Medical Diagnosis Agent

class MedicalDiagnosisAgent:
    def __init__(self):
        # Rules (Knowledge Base)
        self.rules = {
            "Acute Appendicitis": {
                "symptoms": {"fever", "abdominal pain", "iliac fossa pain", "vomiting"},
                "tests": {"tlc high", "neutrophils high", "esr high"},
                "treatment": "Surgery"
            },
            "Pneumonia": {
                "symptoms": {"fever", "cough", "sputum", "chest pain"},
                "tests": {"tlc high", "neutrophils high", "esr high", "xray patch"},
                "treatment": "Antibiotics"
            }
        }
        # State (remembers everything entered so far)
        self.state = {"symptoms": set(), "tests": set()}

    def update_state(self, percept):
        """Update state with new symptoms or tests"""
        self.state["symptoms"].update(percept.get("symptoms", set()))
        self.state["tests"].update(percept.get("tests", set()))

    def match_rule(self):
        """Check if current state matches any disease"""
        for disease, data in self.rules.items():
            if data["symptoms"].issubset(self.state["symptoms"]) and \
               data["tests"].issubset(self.state["tests"]):
                return f"\n✅ Diagnosis: {disease}\n💊 Treatment: {data['treatment']}"
        return "\n⚠️ Diagnosis not confirmed yet. Need more information."

    def act(self, percept):
        """Main function: updates state, checks rules, returns action"""
        self.update_state(percept)        # Add new info
        return self.match_rule()          # Try to diagnose


# ---------------- Main Program ----------------
print("=== Medical Diagnosis System (Model-Based Agent) ===")

agent = MedicalDiagnosisAgent()

# Take input multiple times (like real doctor asks step by step)
while True:
    kind = input("\nEnter 'symptom', 'test', or 'quit': ").lower()

    if kind == "quit":
        print("\nExiting system. Stay healthy!")
        break

    elif kind == "symptom":
        symptoms_input = input("Enter symptoms (comma separated): ").lower().split(",")
        symptoms_input = {s.strip() for s in symptoms_input}
        print(agent.act({"symptoms": symptoms_input}))

    elif kind == "test":
        tests_input = input("Enter test results (comma separated): ").lower().split(",")
        tests_input = {t.strip() for t in tests_input}
        print(agent.act({"tests": tests_input}))

    else:
        print("Invalid input! Please enter 'symptom', 'test', or 'quit'.")
