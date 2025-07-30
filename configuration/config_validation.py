from pydantic import BaseModel, Field, model_validator
from typing import List, Optional, Literal, Any

class FieldProperties(BaseModel):
    unique: Optional[bool] = True
    is_camel_case: Optional[bool] = True
    choices: Optional[List[str]] = None
    default_value: Optional[Any] = None
    format: Optional[str] = None   

class FieldConfig(BaseModel):
    field_name: str
    field_type: Literal["int", "string", "float", "bool", "datetime", "dict", "List"]
    field_properties: Optional[FieldProperties] = Field(default_factory=FieldProperties)
    field_keys: Optional[List[str]] = None

    @model_validator(mode="after")
    def validate_dict_keys(self) -> 'FieldConfig':
        if self.field_type == "dict" and not self.field_keys:
            raise ValueError(f"'field_keys' must be provided for dict type field: {self.field_name}")
        return self

class OutputDetails(BaseModel):
    file_format: str
    file_path: str
    delimiter: Optional[str] = None

class ConfigModel(BaseModel):
    num_records: int
    fields: List[FieldConfig]
    output_details: List[OutputDetails]
