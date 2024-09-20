# JSON de respuesta (el mismo que mencionaste antes)
response = "entities": {"multi_tool_action:multi_tool_action": [{"body": "crea", "confidence": 0.999, "end": 4, "entities": [], "id": "835340812042471", "name": "multi_tool_action", "role": "multi_tool_action", "start": 0, "suggested": True, "type": "value", "value": "crea"}], "multi_tool_object:multi_tool_object": [{"body": "usuario", "confidence": 0.9995, "end": 15, "entities": [], "id": "1198248304758453", "name": "multi_tool_object", "role": "multi_tool_object", "start": 8, "type": "value", "value": "usuario"}], "wit$message_body:message_body": [{"body": "arnau", "confidence": 0.999, "end": 21, "entities": [], "id": "1935945100152787", "name": "wit$message_body", "role": "message_body", "start": 16, "suggested": True, "type": "value", "value": "arnau"}]}, "intents": [], "text": "crea el usuario arnau", "traits": {}

# Acceder al valor "joel" del campo wit$message_subject:message_subject
message_subject_value = response["entities"]["wit$message_subject:message_subject"][0]["value"]

print(f"El valor del sujeto del mensaje es: {message_subject_value}")
