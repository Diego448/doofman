from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import Optional

class UserRoles(int, Enum):
    ADMIN = 1
    GUEST = 2

class PaymentType(int, Enum):
    CASH = 1
    TRANSFER = 2
    CARD = 3

class Status(int, Enum):
    ACTIVE = 1
    INACTIVE = 2

class AppointmentStatus(int, Enum):
    SCHEDULED = 1
    COMPLETED = 2
    CANCELLED = 3

class User(BaseModel):
    name: str
    role: UserRoles
    password: str

class UserUpdate(BaseModel):
    name: Optional[str]
    role: Optional[UserRoles]
    password: Optional[str]

class Appointment(BaseModel):
    date: datetime
    notes: str
    patient_id: str
    status: AppointmentStatus

class AppointmentUpdate(BaseModel):
    date: Optional[datetime]
    notes: Optional[str]
    patient_id: Optional[str]
    status: Optional[AppointmentStatus]

class Payment(BaseModel):
    amount: int
    date: datetime
    type: PaymentType
    patient_id: str

class Consult(BaseModel):
    patient_id: str
    notes: str
    appointment_id: str
    cost: int

class Patient(BaseModel):
    name: str
    telephone_number: str
    email: str
    status: Status

class PatientUpdate(BaseModel):
    name: Optional[str]
    telephone_number: Optional[str]
    email: Optional[str]
    status: Optional[Status]