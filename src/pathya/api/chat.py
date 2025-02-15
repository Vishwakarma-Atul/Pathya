from fastapi import APIRouter
from ..models.schemas import ChatRequest, ChatResponse
from ..services.intent_matcher import match_intent
from ..services.query_handler import handle_query

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chatbot(request: ChatRequest):
    intent, extracted_values = match_intent(request.message)
    if not intent:
        return ChatResponse(response="Sorry, I didn't understand that.")
    
    response_text = handle_query(intent, extracted_values, request.customer_id)
    return ChatResponse(response=response_text)
