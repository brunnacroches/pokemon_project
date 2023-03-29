from src.error_handling.validation_error import ValidationError
import traceback

# obter mais informações sobre o erro para ajudar na depuração, você pode 
# incluir a mensagem de erro original e o rastreamento de pilha no 
# dicionário de resposta.

def error_handler_method(error):
    error_message = str(error)
    error_traceback = traceback.format_exc()

    if isinstance(error, ValidationError):
        print("Handle my custom error")
        return {
            "status_code": 400,
            "data": error.message,
            "error_message": error_message,
            "traceback": error_traceback
        }

    if isinstance(error, ZeroDivisionError):
        print('Treat division by zero')
        return {
            "status_code": 400,
            "data": "Division by zero is not allowed",
            "error_message": error_message,
            "traceback": error_traceback
        }
    
    else:
        print('An unknown error occurred')
        return {
            "status_code": 500,
            "data": "An unknown error occurred",
            "error_message": error_message,
            "traceback": error_traceback
        }
