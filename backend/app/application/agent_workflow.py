from typing import TypedDict
from langgraph.graph import StateGraph, END

# Definimos el estado que viajará a través del grafo del agente
class AgentState(TypedDict):
    document_text: str
    client_budget: float
    viability_score: int
    summary: str
    recommended_action: str
    status: str

def analyze_bid_node(state: AgentState):
    """Nodo que simula la evaluación técnica y financiera del agente sobre el Bid."""
    text = state["document_text"]
    budget = state["client_budget"]
    
    # Lógica base de análisis simulada para el MVP (Limpieza y reglas de negocio)
    word_count = len(text.split())
    score = 85 if budget > 10000 else 60
    
    status = "success" if score >= 70 else "review_needed"
    summary = f"Analizado documento de {word_count} palabras. Viabilidad calculada con base en presupuesto de {budget} USD."
    action = "Proceder con la redacción de la propuesta comercial." if status == "success" else "Requiere revisión humana detallada."

    return {
        "viability_score": score,
        "summary": summary,
        "recommended_action": action,
        "status": status
    }

def create_bid_workflow():
    """Construye y compila el grafo de LangGraph para el flujo del agente."""
    workflow = StateGraph(AgentState)
    
    # Añadir nodo principal de análisis
    workflow.add_node("analyzer", analyze_bid_node)
    
    # Definir punto de entrada y salida
    workflow.set_entry_point("analyzer")
    workflow.add_edge("analyzer", END)
    
    return workflow.compile()