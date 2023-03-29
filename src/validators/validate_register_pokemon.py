from cerberus import Validator
from src.error_handling.validation_error import ValidationError

def validate_register_pokemon_request_body(request_body):
    schema = {
        "name_pokemon": {"type": "string", "required": True},
        "attack_force": {"type": "string", "required": True},
        "attack_value": {"type": "number", "required": True}
    }
    validator = Validator(schema)
    is_valid = validator.validate(request_body)

    if not is_valid:
        raise ValidationError({"message": "Invalid request body", "errors": validator.errors})

    return {
        "is_valid": is_valid,
        "error": validator.errors
    }
